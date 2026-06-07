Easy Level Viva Questions (Beginner)
Vagrant
Q1. What is Vagrant?

Answer: Vagrant is a tool used to create and manage virtual machines in a simple and automated way.

Q2. Why is Vagrant used?

Answer: It helps developers create consistent development environments across different systems.

Q3. Which virtualization software is used with Vagrant in this lab?

Answer: VirtualBox.

Q4. Which command initializes a Vagrant project?
vagrant init
Q5. Which command starts a Vagrant machine?
vagrant up
Q6. How do you connect to a Vagrant VM?
vagrant ssh
Q7. How do you stop a Vagrant VM?
vagrant halt
Q8. How do you delete a Vagrant VM?
vagrant destroy
Docker Basics
Q9. What is Docker?

Answer: Docker is a containerization platform used to package applications and their dependencies into containers.

Q10. What is a container?

Answer: A lightweight isolated environment that runs an application and its dependencies.

Q11. What is the difference between VM and Container?
VM	Container
Has its own OS	Shares host OS kernel
Heavy	Lightweight
Slower startup	Fast startup
Q12. What command checks Docker installation?
docker run hello-world
Q13. What is Docker Hub?

Answer: A cloud repository used to store and share Docker images.

Q14. How do you search an image?
docker search nginx
Q15. How do you download an image?
docker pull nginx
Q16. How do you list local images?
docker images
Q17. How do you list running containers?
docker ps
Q18. How do you stop a container?
docker stop <container-id>
Q19. How do you start a stopped container?
docker start <container-id>
Q20. What command removes an image?
docker rmi nginx
Dockerfile
Q21. What is a Dockerfile?

Answer: A text file containing instructions to build a Docker image.

Q22. Which instruction specifies the base image?
FROM ubuntu
Q23. Which instruction copies files?
COPY
Q24. Which instruction changes working directory?
WORKDIR
Q25. Which command builds an image?
docker build -t image-name .
Docker Compose
Q26. What is Docker Compose?

Answer: A tool used to define and manage multi-container Docker applications.

Q27. Which file is used by Docker Compose?
docker-compose.yml
Q28. Which command starts compose services?
docker-compose up -d
Q29. Which command stops compose services?
docker-compose down
Kubernetes
Q30. What is Kubernetes?

Answer: An orchestration platform used to deploy, manage, and scale containers.

Q31. What is Minikube?

Answer: A single-node Kubernetes cluster for local testing.

Q32. What is kubectl?

Answer: Command-line tool used to interact with Kubernetes clusters.

Q33. Which command shows pods?
kubectl get pods
Q34. Which command shows deployments?
kubectl get deployments
Q35. What is a Pod?

Answer: Smallest deployable unit in Kubernetes that contains one or more containers.

Medium Level Viva Questions
Vagrant
Q36. What is a Vagrantfile?

Answer: It is a configuration file used to define VM settings like CPU, memory, networking, and provisioning.

Q37. How can you allocate CPU to a Vagrant VM?
config.vm.provider "virtualbox" do |v|
  v.cpus = 2
end
Q38. How can you allocate memory?
v.memory = 1024
Q39. What is provisioning?

Answer: Automatic execution of scripts during VM creation.

Q40. Why is shell provisioning used?

Answer: To install software and configure systems automatically.

Docker
Q41. What is the difference between Docker Image and Container?

Image: Template used to create containers.

Container: Running instance of an image.

Q42. What is an Alpine image?

Answer: A lightweight Linux distribution commonly used in Docker.

Q43. Why do we use detached mode (-d)?

Answer: To run containers in the background.

Q44. What does -it mean?
i = Interactive
t = Terminal
Q45. How do you view container logs?
docker logs <container-id>
Q46. What are Docker volumes?

Answer: Persistent storage used by containers.

Q47. Why are Docker volumes needed?

Answer: To prevent data loss when containers are deleted.

Q48. How do you create a volume?
docker volume create myvol
Q49. What is port mapping?

Answer: Mapping host ports to container ports.

Example:

docker run -p 80:80 nginx
Q50. What does EXPOSE do?

Answer: It documents which ports the container listens on.

Docker Compose
Q51. Why use Docker Compose?

Answer: To manage multiple containers using one configuration file.

Q52. What is depends_on?

Answer: Defines service startup dependency.

Q53. What is an environment variable?

Answer: Configuration value passed to applications.

Docker Swarm
Q54. What is Docker Swarm?

Answer: Docker's native container orchestration platform.

Q55. What is a Swarm Manager?

Answer: Controls cluster operations and scheduling.

Q56. What is a Worker Node?

Answer: Executes containers assigned by the manager.

Q57. Command to initialize swarm?
docker swarm init
Q58. Command to view nodes?
docker node ls
Q59. What is a service in Swarm?

Answer: A desired state definition for running containers.

Q60. What is scaling?

Answer: Increasing or decreasing container replicas.

Kubernetes
Q61. Difference between Pod and Container?

Container: Runs application.

Pod: Wraps one or more containers.

Q62. What is Deployment?

Answer: Kubernetes object used to manage Pods.

Q63. Why use Deployments?

Answer: For scaling, updates, and self-healing.

Q64. What is a Service?

Answer: Exposes Pods through a stable network endpoint.

Q65. What is LoadBalancer Service?

Answer: Exposes applications externally.

Advanced Industry-Level Viva Questions
Containerization
Q66. Why did containers become popular over virtual machines?

Answer:

Faster startup
Lower resource usage
Better scalability
Higher deployment speed
Q67. Explain container isolation.

Answer:
Docker uses:

Namespaces
Control Groups (cgroups)
Linux Kernel Features

to isolate processes and resources.

Q68. Why is Alpine Linux widely used in Docker?

Answer:

Small size (~5 MB)
Faster downloads
Reduced attack surface
Lower storage consumption
Q69. What are Docker image layers?

Answer:
Each Dockerfile instruction creates a layer. Layers improve caching and reduce build time.

Q70. What is a multi-stage Docker build?

Answer:
A technique to reduce image size by separating build and runtime environments.

Docker Volumes
Q71. Difference between Bind Mount and Volume?
Volume	Bind Mount
Managed by Docker	Managed by Host
Portable	Host-dependent
Preferred in Production	Mostly Development
Q72. Why should databases use volumes?

Answer: Database data must persist even after container deletion.

Docker Networking
Q73. How do containers communicate?

Answer:
Through Docker networks such as:

Bridge
Host
Overlay
Macvlan
Q74. What is Overlay Network in Swarm?

Answer: A distributed network allowing containers on different nodes to communicate.

Docker Swarm
Q75. How does Swarm provide High Availability?

Answer:
If a container crashes, Swarm automatically recreates it.

Q76. What is Desired State?

Answer: The target number of replicas defined by the user.

Q77. What happens if a worker node fails?

Answer: Swarm reschedules workloads on healthy nodes.

Kubernetes
Q78. Why is Kubernetes preferred over Docker Swarm?

Answer:

Better scaling
Self-healing
Auto-scaling
Large ecosystem
Production-grade orchestration
Q79. What is self-healing in Kubernetes?

Answer: Kubernetes automatically recreates failed pods.

Q80. What is rolling update?

Answer: Updating applications without downtime.

Q81. What is the role of kubelet?

Answer: Agent running on each node responsible for pod execution.

Q82. What is etcd?

Answer: Distributed key-value store that stores Kubernetes cluster state.

Q83. What is a ReplicaSet?

Answer: Ensures a specified number of pod replicas remain running.

Q84. Difference between Deployment and ReplicaSet?

Answer:
Deployment manages ReplicaSets and provides rolling updates.

Q85. What is Kubernetes Service Discovery?

Answer: Mechanism through which pods locate and communicate with each other.

DevOps Industry Questions
Q86. Where is Docker used in CI/CD?

Answer:

Build stage
Testing stage
Deployment stage
Environment consistency
Q87. How would you deploy a microservice architecture?

Answer:

Dockerize services
Push images to registry
Deploy using Kubernetes
Monitor using Prometheus and Grafana
Q88. Why is Kubernetes important for DevOps Engineers?

Answer:
It automates deployment, scaling, recovery, networking, and container management.

Q89. What monitoring tools are commonly used with Kubernetes?

Answer:

Prometheus
Grafana
ELK Stack
Loki
Q90. Design a production container platform.

Answer:

GitHub/GitLab
Jenkins
Docker
Docker Registry
Kubernetes
Prometheus
Grafana
Terraform
AWS/GCP/Azure
