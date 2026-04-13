1. Multi-Stage Builds
Multi-stage builds allow you to use multiple FROM statements in a single Dockerfile. This is the gold standard for creating slim, secure production images.

How it works: You use a large image (with compilers and tools) to build your app, then copy only the compiled binary or static assets into a tiny production image (like Alpine or Scratch).

Key Benefit: It drastically reduces the attack surface and image size.

Dockerfile
# Stage 1: Build
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# Stage 2: Production
FROM nginx:stable-alpine
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
2. Docker Networking
Docker uses "drivers" to manage how containers talk to each other and the outside world.

Network Driver	Use Case	Behavior
Bridge	Default (Single Host)	Containers get private IPs; ports must be mapped to the host to be reachable externally.
Host	Performance-Critical	Removes isolation between container and host; the container uses the host’s IP and ports directly.
Overlay	Multi-Host (Swarm/K8s)	Enables communication between containers running on different physical or virtual machines.
None	High Security	No external or internal network access.
3. Storage: Volumes vs. Bind Mounts
Containers are ephemeral (data is lost when the container is deleted). Persistence requires volumes.

Volumes: Managed by Docker (usually in /var/lib/docker/volumes). This is the preferred method because it is independent of the host’s directory structure and easier to back up.

Bind Mounts: Maps a specific path on the host (e.g., /home/user/code) to the container. Great for development because changes on your host reflect in the container instantly.

4. Docker Compose
Compose is a tool for defining and running multi-container applications. Instead of long docker run commands, you use a docker-compose.yml file.

Orchestration: It handles the creation of networks and volumes automatically.

Dependency Management: You can ensure a database starts before the web server using depends_on.

5. Image Optimization Techniques
Beyond multi-stage builds, use these tactics to keep your CI/CD pipelines fast:

Order Layers by Frequency of Change: Put commands that change least (like RUN apt-get update) at the top. Put code COPY commands at the bottom. This maximizes Layer Caching.

Combine RUN Commands: Every RUN creates a new layer. Instead of three RUN commands, use && to combine them into one to save space.

Use .dockerignore: Prevent heavy folders like node_modules or .git from being sent to the Docker daemon during the build.

Choose Small Base Images: Always opt for -alpine or -slim variants when possible.

Note: A typical Ubuntu base image might be 70MB, while an Alpine Linux base is only 5MB.
