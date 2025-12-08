# Base image with Python 3.11
FROM mcr.microsoft.com/devcontainers/python:3.11

# Install system dependencies (including sqlite3 CLI)
RUN apt-get update && apt-get install -y \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

# Where VS Code will mount your project
WORKDIR /workspace

# Default user is "vscode" provided by the base image
USER vscode
