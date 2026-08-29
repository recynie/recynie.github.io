---
title: "pi-goal: `/goal` extention for pi coding agent"
excerpt: "`/goal` extention for practical usage, featuring (1) interactive clarification with user before goal proposal and (2) independent verification after goal completion."
collection: portfolio
permalink: /portfolio/pi-goal/
public: true
---

Repository: [pi-goal](https://github.com/recynie/pi-goal)

What is it?
=======

`pi-goal` is a pi extention for long-horizen/multi-loop execution.

Use `pi-goal` when
- the task is complex and (maybe) unclear,
- you want agents to operate autonomously for long periods without human intervention.

Workflow: 
1. You discuss your request, refine it, and propose a goal with the agent
2. The agent continously persuing the goal for multiple agent-loops
3. When the agent thinks the goal is completed, it submit the result to an independent verifier
4. The verifier checks the result and workspace and returns a pass/fail result
5. Pass: the goal completes; Fail: enter a new agent-loop (max 25 loops)

A Comparison between `pi-goal` and Codex `/goal`
=======

Codex `/goal` centers on long-horizen execution, it injects the goal into prompt until the agent returns a predefined "promise word" when it thinks the goal is completed.

This pattern has some risks:
- The Goal is proposed by user, thus agnet can be misaligned with user. If agent misunderstands the goal, the result will be far from the real request from user.
- Completion is determined by agent. Agent can over-claim what it does, leading to a false completion.

`pi-goal` solves these risk with simple logic:
- Agent refines the Goal together with user, which promises alignment between user and agent. (Inspired by Matt Pocock [grill-me](https://github.com/mattpocock/skills/tree/main#1-the-agent-didnt-do-what-i-want).)
- Completion is determined by a verifier with fresh context, which promises the completion is determined by an independent agent.

In addition, `pi-goal` keeps the logic simple and easy to understand: There is no complex concept or contract to remember, no additional files in workspace.

Design
=======

The project treats long-running agent work as a lifecycle with three distinct responsibilities: the user defines and approves the desired outcome, the main agent chooses how to achieve it, and an independent verifier decides whether the outcome has actually been reached. Separating these responsibilities prevents the implementation plan from silently redefining the goal and prevents the worker's own narrative from becoming the sole evidence of completion.

The central abstraction is a GoalSpec containing a main goal, independently verifiable subtasks, additional acceptance details, and optional worker-only suggestions. The goal and acceptance criteria remain stable during execution, while the agent can revise its internal plan as it learns from the workspace. Only the user can initiate changes to an approved GoalSpec. This preserves a clear distinction between **what must become true** and **how the agent intends to make it true**.

The implementation maintains one current Goal for each session branch. Its lifecycle covers refinement, active execution, pause, verification, and terminal states. State is persisted in the Pi session so that the Goal can be restored after reload, context compaction, session resumption, or branch navigation. Automatic continuation keeps the worker progressing across model turns, while safety limits pause the Goal when the loop exceeds its turn budget, repeatedly makes no visible progress, or encounters an unrecoverable runtime failure.

A key systems concern is the ordering of asynchronous actions. A user may request a pause or edit while the worker is running, and a worker submission may race with a verifier result or a new user decision. `pi-goal` handles these events through settled-boundary serialization: tools and interface actions first record transition intents, then the controller commits them after the current worker or verifier run settles. User actions have priority over submission, verification, and continuation. This ordering prevents stale work from advancing a Goal after its governing decision has changed.

Verification runs in a fresh in-memory agent session. The verifier receives the approved acceptance criteria, the exact final result shown to the user, and tools for inspecting the workspace. It does not inherit the worker's conversation, execution plan, optional implementation suggestions, or previous verifier context. This creates contextual independence rather than a security sandbox: the verifier has enough capability to inspect artifacts and run tests, while avoiding the assumptions and self-confirming narrative accumulated during implementation. A failed verification returns actionable details to the main agent and reopens the execution loop under the same approved Goal.

Several broader insights follow from this design:

- **Persistence does not guarantee alignment.** A longer agent loop can pursue a misunderstood objective more thoroughly.
- **Clarification should produce a durable contract.** Goal refinement becomes operationally useful when it results in explicit, verifiable outcomes that govern later work.
- **Goals and plans need different owners.** The user controls the acceptance boundary, while the agent retains flexibility over implementation.
- **Completion is an independent judgment problem.** A fresh verifier reduces anchoring on the worker's reasoning and claims.
- **Lifecycle correctness depends on systems design.** Ordering, ownership, interruption handling, persistence, and recovery are as important as prompting.
- **Verification is most useful as feedback.** A failed check identifies remaining gaps and sends them back into execution instead of merely rejecting the result.

At a higher level, `pi-goal` explores how agent autonomy can remain accountable. It frames long-horizon execution as a small system of specification, action, and judgment, connected by explicit state transitions and authority boundaries. The aim is not simply to keep an agent working longer, but to keep its work tied to a shared definition of success and require independent evidence before that success is accepted.
