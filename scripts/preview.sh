#!/usr/bin/env bash
set -euo pipefail

readonly SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
readonly PROJECT_DIR="$(dirname -- "$SCRIPT_DIR")"
readonly IMAGE_NAME="academicpages-preview"
readonly CONTAINER_NAME="academicpages-preview"

command -v podman >/dev/null 2>&1 || {
  echo "Error: podman is not installed." >&2
  exit 1
}

if podman container exists "$CONTAINER_NAME"; then
  echo "Error: container '$CONTAINER_NAME' already exists." >&2
  echo "Stop it with: podman stop $CONTAINER_NAME" >&2
  exit 1
fi

echo "Building $IMAGE_NAME..."
podman build -t "$IMAGE_NAME" "$PROJECT_DIR"

echo "Starting Jekyll at http://localhost:4000 ..."
exec podman run --rm \
  --userns=keep-id \
  --name "$CONTAINER_NAME" \
  -p 4000:4000 \
  -v "$PROJECT_DIR:/usr/src/app:Z" \
  -e JEKYLL_ENV=docker \
  "$IMAGE_NAME"
