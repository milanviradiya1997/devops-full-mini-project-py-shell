#!/bin/bash
set -e

IMAGE_NAME="devops-mini-app"
CONTAINER_NAME="devops_py_shell_app"

echo "🔹 Building Docker image"
docker build -t $IMAGE_NAME .

echo "🔹 Removing old container"
docker rm -f $CONTAINER_NAME || true

echo "🔹 Running new container"
docker run -d -p 80:80 --name $CONTAINER_NAME $IMAGE_NAME

echo "✅ Docker deployment completed"