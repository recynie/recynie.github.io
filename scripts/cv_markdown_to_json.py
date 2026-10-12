#!/usr/bin/env python3
"""
Script to convert markdown CV to JSON format
Author: Yuan Chen
"""

import os
import re
import json
import yaml
import argparse
from datetime import datetime, date
from pathlib import Path
import glob

# Custom JSON encoder to handle date objects
class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        return super().default(obj)

def parse_markdown_cv(md_file):
    """Parse the markdown CV file and extract sections."""
    with open(md_file, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove YAML front matter
    content = re.sub(r'^---.*?---\s*', '', content, flags=re.DOTALL)
    
    # CV sections use setext headings; ordinary prose is not a heading.
    headings = list(re.finditer(r'^([^\n]+)\n=+\s*$', content, re.MULTILINE))
    return {
        heading.group(1).strip(): content[heading.end():
            headings[index + 1].start() if index + 1 < len(headings) else len(content)].strip()
        for index, heading in enumerate(headings)
    }


def parse_config(config_file):
    """Parse the Jekyll _config.yml file for additional information."""
    if not os.path.exists(config_file):
        return {}
    
    with open(config_file, 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
    
    return config

def extract_author_info(config):
    """Extract author information from the config file."""
    author_info = {
        "name": config.get('name', ''),
        "email": "",
        "phone": "",
        "website": config.get('url', ''),
        "summary": "",
        "location": {
            "address": "",
            "postalCode": "",
            "city": "",
            "countryCode": "CN",
            "region": ""
        },
        "profiles": []
    }
    
    # Extract author details if available
    if 'author' in config:
        author = config.get('author', {})
        
        # Override name if author name is available
        if author.get('name'):
            author_info['name'] = author.get('name')
        
        # Add email
        if author.get('email'):
            author_info['email'] = author.get('email')
        
        # Add location
        if author.get('location'):
            author_info['location']['city'] = author.get('location', '').split(',')[0].strip()
            author_info['location']['region'] = 'Liaoning'
        
        # Add employer as part of summary
        if author.get('employer'):
            author_info['summary'] = f"Undergraduate in Artificial Intelligence at {author.get('employer')}"
        
        # Add bio to summary if available
        if author.get('bio'):
            if author_info['summary']:
                author_info['summary'] += f". {author.get('bio')}"
            else:
                author_info['summary'] = author.get('bio')
        
        # Add social profiles
        profiles = []
        
        # Academic profiles
        if author.get('googlescholar'):
            profiles.append({
                "network": "Google Scholar",
                "username": "",
                "url": author.get('googlescholar')
            })
        
        if author.get('orcid'):
            profiles.append({
                "network": "ORCID",
                "username": "",
                "url": author.get('orcid')
            })
        
        if author.get('researchgate'):
            profiles.append({
                "network": "ResearchGate",
                "username": "",
                "url": author.get('researchgate')
            })
        
        # Social media profiles
        if author.get('github'):
            profiles.append({
                "network": "GitHub",
                "username": author.get('github'),
                "url": f"https://github.com/{author.get('github')}"
            })
        
        if author.get('linkedin'):
            profiles.append({
                "network": "LinkedIn",
                "username": author.get('linkedin'),
                "url": f"https://www.linkedin.com/in/{author.get('linkedin')}"
            })
        
        if author.get('twitter'):
            profiles.append({
                "network": "Twitter",
                "username": author.get('twitter'),
                "url": f"https://twitter.com/{author.get('twitter')}"
            })
        
        author_info['profiles'] = profiles
    
    return author_info

def parse_education(education_text):
    """Parse education section from markdown."""
    lines = re.findall(r'^- (.+)$', education_text, re.MULTILINE)
    institution, program = lines
    match = re.fullmatch(r'Undergraduate in (.+), (\d{4})[–-](\d{4})', program)
    area, start, end = match.groups()
    return [{
        "institution": institution,
        "area": area,
        "studyType": "Undergraduate",
        "startDate": start,
        "endDate": end,
        "gpa": None,
        "courses": []
    }]


def parse_research(research_text):
    """Parse project headings, advisors, and contribution bullets."""
    entries = []
    months = {"Apr.": "04", "May": "05", "Oct.": "10", "Dec.": "12"}

    def iso_month(value):
        if value == "Present":
            return ""
        month, year = value.split()
        return f"{year}-{months[month]}"

    pattern = r'^\*\*(.+?)\*\* \((.+?) – (.+?)\)\n(.*?)(?=^\*\*[^\n]+?\*\* \(|\Z)'
    for title, start, end, body in re.findall(pattern, research_text, re.MULTILINE | re.DOTALL):
        advisor = re.search(r'\*\*Advisor:\*\* (.+)', body).group(1)
        bullets = re.findall(r'^- (.+)$', body, re.MULTILINE)
        entries.append({
            "company": "Dalian University of Technology",
            "position": title,
            "website": "",
            "startDate": iso_month(start),
            "endDate": iso_month(end),
            "summary": f"Advisor: {advisor}. {bullets[0]}",
            "highlights": bullets[1:]
        })
    return entries


def parse_work_experience(work_text):
    """Parse work experience section from markdown."""
    work_entries = []
    
    # Extract work entries
    entries = re.findall(r'\* (.*?)(?=\n\*|\Z)', work_text, re.DOTALL)
    
    for entry in entries:
        lines = entry.strip().split('\n')
        if not lines:
            continue
            
        # Parse position and company
        first_line = lines[0].strip()
        position_match = re.match(r'(.*?), (.*?)(?:, |$)', first_line)
        
        if position_match:
            position, company = position_match.groups()
            
            # Extract dates if available
            date_match = re.search(r'(\d{4})\s*-\s*(\d{4}|present)', entry, re.IGNORECASE)
            start_date = date_match.group(1) if date_match else ""
            end_date = date_match.group(2) if date_match else ""
            
            # Extract highlights
            highlights = []
            for line in lines[1:]:
                if line.strip().startswith('*') or line.strip().startswith('-'):
                    highlights.append(line.strip()[1:].strip())
            
            work_entries.append({
                "company": company.strip(),
                "position": position.strip(),
                "website": "",
                "startDate": start_date,
                "endDate": end_date,
                "summary": "",
                "highlights": highlights
            })
    
    return work_entries

def parse_skills(skills_text):
    """Parse skills section from markdown."""
    skills_entries = []
    
    # Extract skill categories
    categories = re.findall(r'(?:^|\n)(\w+.*?):\s*(.*?)(?=\n\w+.*?:|\Z)', skills_text, re.DOTALL)
    
    for category, skills in categories:
        # Extract individual skills
        skill_list = [s.strip() for s in re.split(r',|\n', skills) if s.strip()]
        
        skills_entries.append({
            "name": category.strip(),
            "level": "",
            "keywords": skill_list
        })
    
    return skills_entries

def parse_publications(pub_dir):
    """Parse publications from the _publications directory."""
    publications = []
    
    if not os.path.exists(pub_dir):
        return publications
    
    for pub_file in sorted(glob.glob(os.path.join(pub_dir, "*.md"))):
        with open(pub_file, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Extract front matter
        front_matter_match = re.match(r'^---\s*(.*?)\s*---', content, re.DOTALL)
        if front_matter_match:
            front_matter = yaml.safe_load(front_matter_match.group(1))
            
            # Extract publication details
            pub_entry = {
                "name": front_matter.get('title', ''),
                "publisher": front_matter.get('venue', ''),
                "releaseDate": front_matter.get('date', ''),
                "website": front_matter.get('paperurl', ''),
                "summary": front_matter.get('excerpt', ''),
                "citation": front_matter.get('citation', '')
            }
            
            publications.append(pub_entry)
    
    return sorted(publications, key=lambda item: str(item['releaseDate']), reverse=True)

def parse_talks(talks_dir):
    """Parse talks from the _talks directory."""
    talks = []
    
    if not os.path.exists(talks_dir):
        return talks
    
    for talk_file in sorted(glob.glob(os.path.join(talks_dir, "*.md"))):
        with open(talk_file, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Extract front matter
        front_matter_match = re.match(r'^---\s*(.*?)\s*---', content, re.DOTALL)
        if front_matter_match:
            front_matter = yaml.safe_load(front_matter_match.group(1))
            
            # Extract talk details
            talk_entry = {
                "name": front_matter.get('title', ''),
                "event": front_matter.get('venue', ''),
                "date": front_matter.get('date', ''),
                "location": front_matter.get('location', ''),
                "description": front_matter.get('excerpt', '')
            }
            
            talks.append(talk_entry)
    
    return talks

def parse_teaching(teaching_dir):
    """Parse teaching from the _teaching directory."""
    teaching = []
    
    if not os.path.exists(teaching_dir):
        return teaching
    
    for teaching_file in sorted(glob.glob(os.path.join(teaching_dir, "*.md"))):
        with open(teaching_file, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Extract front matter
        front_matter_match = re.match(r'^---\s*(.*?)\s*---', content, re.DOTALL)
        if front_matter_match:
            front_matter = yaml.safe_load(front_matter_match.group(1))
            
            # Extract teaching details
            teaching_entry = {
                "course": front_matter.get('title', ''),
                "institution": front_matter.get('venue', ''),
                "date": front_matter.get('date', ''),
                "role": front_matter.get('type', ''),
                "description": front_matter.get('excerpt', '')
            }
            
            teaching.append(teaching_entry)
    
    return teaching

def parse_portfolio(portfolio_dir):
    """Parse portfolio items from the _portfolio directory."""
    portfolio = []
    
    if not os.path.exists(portfolio_dir):
        return portfolio
    
    for portfolio_file in sorted(glob.glob(os.path.join(portfolio_dir, "*.md"))):
        with open(portfolio_file, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Extract front matter
        front_matter_match = re.match(r'^---\s*(.*?)\s*---', content, re.DOTALL)
        if front_matter_match:
            front_matter = yaml.safe_load(front_matter_match.group(1))
            
            # Extract portfolio details
            portfolio_entry = {
                "name": front_matter.get('title', ''),
                "category": front_matter.get('collection', 'portfolio'),
                "date": front_matter.get('date', ''),
                "url": front_matter.get('permalink', ''),
                "description": front_matter.get('excerpt', '')
            }
            
            portfolio.append(portfolio_entry)
    
    return portfolio

def create_cv_json(md_file, config_file, repo_root, output_file):
    """Create a JSON CV from markdown and other repository data."""
    # Parse the markdown CV
    sections = parse_markdown_cv(md_file)
    
    # Parse config file
    config = parse_config(config_file)
    
    # Extract author information
    author_info = extract_author_info(config)
    contact = Path(md_file).read_text(encoding='utf-8')
    author_info['phone'] = re.search(r'\*\*Contact:\*\* .+? · (.+?) ·', contact).group(1)
    
    # Create the JSON structure
    cv_json = {
        "basics": author_info,
        "work": parse_research(sections['Research experience']),
        "education": parse_education(sections.get('Education', '')),
        "skills": [
            {"name": name, "level": "", "keywords": keywords.split(', ')}
            for name, keywords in re.findall(r'^- \*\*(.+?):\*\* (.+)$', sections['Skills'], re.MULTILINE)
        ],
        "languages": [],
        "interests": [],
        "references": []
    }
    
    # Academic results and English-language tests come from the current CV.
    performance = sections['Academic performance']
    cv_json['education'][0]['score'] = re.search(r'Academic score: (.+)', performance).group(1)
    cv_json['education'][0]['highlights'] = re.findall(r'^- (.+academic rank: .+)$', performance, re.MULTILINE)
    cv_json['education'][0]['courses'] = re.search(r'\*\*Selected coursework:\*\* (.+)', performance).group(1).split(', ')
    cv_json['languages'] = [{"language": "English", "fluency": re.search(r'\*\*Language tests:\*\* (.+)', performance).group(1)}]
    cv_json['interests'] = [
        {"name": name, "keywords": [description]}
        for name, description in re.findall(r'^- \*\*(.+?):\*\* (.+)$', sections['Research interests'], re.MULTILINE)
    ]
    cv_json['awards'] = [
        {"title": item, "date": "", "awarder": "", "summary": ""}
        for item in re.findall(r'^- (.+)$', sections['Scholarships'], re.MULTILINE)
    ]
    for month, year, description in re.findall(r'^- \*\*(\w+)\. (\d{4}):\*\* (.+)$', sections['Competitions and awards'], re.MULTILINE):
        title, summary = description.split('. ', 1)
        cv_json['awards'].append({"title": title, "date": f"{year}-{'09' if month == 'Sep' else '06'}", "awarder": "", "summary": summary})

    # Add publications
    cv_json["publications"] = parse_publications(os.path.join(repo_root, "_publications"))
    
    # Add talks
    cv_json["presentations"] = parse_talks(os.path.join(repo_root, "_talks")) if 'Presentations' in sections else []
    
    # Add teaching
    cv_json["teaching"] = parse_teaching(os.path.join(repo_root, "_teaching")) if 'Teaching' in sections else []
    
    # Add portfolio
    project_paths = re.findall(r"'/portfolio/([^']+)'", sections['Personal projects'])
    cv_json["portfolio"] = [
        item for item in parse_portfolio(os.path.join(repo_root, "_portfolio"))
        if item['url'] in [f"/portfolio/{path}" for path in project_paths]
    ]
    
    # Extract languages and interests from config if available
    if 'languages' in config:
        cv_json["languages"] = config.get('languages', [])
    
    if 'interests' in config:
        cv_json["interests"] = config.get('interests', [])
    
    # Write the JSON to a file
    with open(output_file, 'w', encoding='utf-8') as file:
        json.dump(cv_json, file, indent=2, ensure_ascii=False, cls=DateTimeEncoder)
        file.write('\n')
    
    print(f"Successfully converted {md_file} to {output_file}")

def main():
    """Main function to parse arguments and run the conversion."""
    parser = argparse.ArgumentParser(description='Convert markdown CV to JSON format')
    parser.add_argument('--input', '-i', required=True, help='Input markdown CV file')
    parser.add_argument('--output', '-o', required=True, help='Output JSON file')
    parser.add_argument('--config', '-c', help='Jekyll _config.yml file')
    
    args = parser.parse_args()
    
    # Get repository root (parent directory of the input file's directory)
    repo_root = str(Path(args.input).parent.parent)
    
    create_cv_json(args.input, args.config, repo_root, args.output)

if __name__ == '__main__':
    main()
