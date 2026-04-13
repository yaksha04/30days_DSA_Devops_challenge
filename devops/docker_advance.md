1. Docker BuildKit
BuildKit is the next-generation build engine for Docker. It is faster, more efficient, and provides features that standard builds lack.

Parallelism: It resolves the dependency graph of your Dockerfile and builds independent stages simultaneously.

Secret Mounts: Allows you to use credentials (like SSH keys or API tokens) during the build without them ever being stored in the final image layers.

Cache Imports/Exports: You can store your build cache in a remote registry, making CI/CD builds significantly faster.

How to enable: Set the environment variable DOCKER_BUILDKIT=1.

2. Resource Limits
By default, a container has no resource constraints and can consume as much of the host’s CPU and RAM as the kernel allows. In production, this can lead to "noisy neighbor" issues where one container crashes the whole host.

Memory Limits: --memory="512m" (Hard limit; the container is killed if it exceeds this).

CPU Limits: --cpus="1.5" (The container is guaranteed at most 1.5 CPUs of the host's total capacity).

In Compose:

YAML
deploy:
  resources:
    limits:
      cpus: '0.50'
      memory: 512M
3. Health Checks
A container being "Up" doesn't mean the application is actually working. A Health Check tells Docker how to test if the app is truly ready to handle traffic.

Instruction: HEALTHCHECK --interval=30s --timeout=3s CMD curl -f http://localhost/health || exit 1

Outcome: Docker will mark the container as starting, then healthy or unhealthy. Orchestrators (like Swarm or Kubernetes) use this to decide when to restart a container or route traffic to it.

4. Docker Security & Secrets
Security in Docker follows the principle of "Least Privilege."

Non-Root User: By default, containers run as root. Always create a service user in your Dockerfile:

Dockerfile
RUN useradd -m myuser
USER myuser
Docker Secrets: Avoid using environment variables for passwords or API keys (they show up in docker inspect). Docker Secrets encrypt sensitive data at rest and only mount them into the container's memory at /run/secrets/.

Read-Only Filesystem: Use the --read-only flag to prevent attackers from modifying the container’s binaries or configuration files at runtime.

5. Private Registries
While Docker Hub is great for public images, enterprises use private registries to ensure security and proximity.

Self-Hosted: You can run the official registry:2 image to host your own.

Cloud-Native: AWS ECR, Azure ACR, or Google Artifact Registry.

Workflow: 1.  docker tag my-app:v1 my-registry.com/my-app:v1
2.  docker login my-registry.com
3.  docker push my-registry.com/my-app:v1

Advanced Comparison: Secrets vs. Env Vars
Feature	Environment Variables	Docker Secrets
Storage	Plain text in configuration	Encrypted at rest (in Swarm)
Visibility	Visible via docker inspect	Hidden from inspect
Delivery	Injected at runtime	Mounted as a virtual file
Use Case	Non-sensitive config (Port, Host)	Sensitive data (DB Password, Keys)
