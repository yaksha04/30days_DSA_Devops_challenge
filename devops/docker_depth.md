Overcoming Manual Complexity: Manually running containers with docker run is error-prone due to long flag lists for networking, ports, and volumes
. Compose provides a declarative, automated, and reproducible way to manage the entire application stack
.
The YAML Blueprint: A docker-compose.yml file is generally divided into three primary sections: Services (computing components), Networks (communication layer), and Volumes (persistence layer)
.
Key Service Options:
Image vs. Build: image pulls a pre-built image from a registry, while build tells Compose to create an image dynamically from a local Dockerfile
.
Ports: Maps a container's internal ports to the host machine (e.g., "5000:5000")
.
Restart Policies: unless-stopped is often preferred, ensuring containers restart on failure but not if manually stopped
.
Profiles: Profiles allow for the selective startup of services. This is useful for grouping services required only for specific tasks, such as debugging or testing, in a single file
.
2. Networking and Persistence
Default Networking: By default, Compose places all services on a single private network where they communicate using service names as hostnames (e.g., a web app connecting to a database named db)
.
Bridge vs. Overlay Drivers: The bridge driver is standard for local networks, while overlay is used for multi-host networks in Docker Swarm
.
Data Persistence:
Bind Mounts: Maps a local physical path to the container, enabling live reloading where code changes appear immediately
.
Named Volumes: Docker manages the storage location (typically in /var/lib/docker/volumes), ensuring data survives even if a container is deleted
.
3. Startup Order and Health Checks
A common "trap" in Docker Compose is assuming depends_on waits for a service to be ready
.
The Dependency Issue: By default, Compose only waits until a container is running, not until the internal process (like a database) is ready to accept connections
.
The Solution: Use the condition attribute within depends_on. By setting condition: service_healthy, you force a dependent service to wait until the primary service's healthcheck passes
.
Healthcheck Implementation: You define a test command (e.g., pg_isready for PostgreSQL) and specify intervals, timeouts, and retries
.
4. Microservices Design and "SEED(S)"
Successful microservices require an explicit, end-to-end system design to avoid unmanageable complexity
.
The SEED(S) Process: This evolutionary methodology (Seven Essential Evolutions of Design for Services) includes:
Identifying Actors: Specific archetypes representing user needs
.
Identifying Jobs (JTBD): Understanding the "Jobs to be Done" using the Job Story format ("When [circumstance], I want to [motivation], so I can [goal]")
.
Interaction Patterns: Using UML Sequence Diagrams (often in PlantUML) to visualize events
.
Deriving Actions and Queries: Separating service endpoints into "Commands" (state-modifying) and "Queries" (lookups with no side effects)
.
Specifications: Formally describing contracts using the OpenAPI Specification (OAS)
.
Service Boundaries: Boundaries should be loosely coupled (independent deployability) and highly cohesive (related features grouped together)
.
Universal Sizing Formula: Start with a few coarse-grained services aligned with Bounded Contexts and split them only when coordination dependencies become a bottleneck
.
5. Advanced Data Management Patterns
Microservices must embed their own data to ensure independent deployability
.
Data Delegate Pattern: If multiple services need the same data, hide that data behind a single "authoritative" delegate service instead of allowing direct database sharing
.
Saga Transactions: Because ACID transactions are difficult across distributed systems, Sagas use a sequence of local transactions and compensating transactions (undo steps) to handle failures
.
Event Sourcing: Instead of storing the current state, this pattern stores a log of immutable facts (events). The state is a derivative calculated via projections
.
CQRS: Command Query Responsibility Segregation separates the data storage system from the queryability indices, allowing each to be optimized independently
.
6. DevOps and Infrastructure as Code (IaC)
Infrastructure should be treated like application code to ensure speed and safety
.
Immutable Infrastructure: Components must never be changed after creation. Updates are made by destroying and re-creating the component with new properties to avoid "server drift"
.
Terraform: A primary tool for IaC that allows for declarative environment definitions using modules to ensure code is DRY (Don't Repeat Yourself)
.
CI/CD Pipelines: All changes must be applied through automated tools like GitHub Actions, preventing manual command-line errors
.
GitOps: Utilizing tools like Argo CD to manage microservice deployments into Kubernetes. GitOps uses a Git repository as the single source of truth for the system's desired state
.
7. Developer Workspace Guidelines
To ensure a high-quality developer experience, organizations should adopt specific principles:
Docker as the Only Dependency: The only things needed on a host machine should be Docker and Docker Compose; everything else (runtimes, libraries) should be containerized
.
The Rule of Twos: Practice heterogeneity by using at least two different technology stacks in production (e.g., Node.js and Python) to ensure the infrastructure supports diverse needs
.
Makefiles: Common targets (e.g., make start, make test, make migrate) should be codified to provide a uniform experience across different microservice repositories
