1. ECS Task Definitions and Services
What is ECS?

Amazon Elastic Container Service (ECS) is AWS's managed container orchestration platform.

Think of ECS as AWS's own version of Kubernetes, but much simpler.

Instead of managing containers manually,

ECS does things like

Run containers
Restart failed containers
Scale containers
Load balancing
Rolling updates
ECS Components
ECS Cluster
│
├── Service
│     │
│     ├── Task
│     │      │
│     │      ├── Container 1
│     │      └── Container 2
│     │
│     └── Task
│
└── EC2/Fargate
What is a Task Definition?

A Task Definition is like a Docker Compose file for ECS.

It tells ECS

"How should this application run?"

It is a JSON specification.

Example

{
  "family":"nginx-app",

  "containerDefinitions":[

    {
      "image":"nginx:latest",

      "cpu":256,

      "memory":512,

      "portMappings":[
          {
             "containerPort":80
          }
      ]
    }
  ]
}
Task Definition contains
Docker Image
nginx:latest

or

123456789.dkr.ecr.ap-south-1.amazonaws.com/app:v1
CPU
256

means

0.25 vCPU
Memory
512 MB
Ports
80
Environment variables
DB_HOST=mysql
Secrets

Can fetch directly from

AWS Secrets Manager
AWS Systems Manager Parameter Store
IAM Role

Each task can have its own IAM permissions.

Example

Only this container
↓

Can access S3
↓

Cannot access DynamoDB

Very secure.

What is a Task?

Task = Running instance of Task Definition.

Exactly like

Docker Image
↓

docker run

↓

Running Container

Similarly

Task Definition

↓

Task
What is ECS Service?

Service manages Tasks.

Without Service

Run Task

↓

Container crashes

↓

Dead forever

With Service

Container crashes

↓

Service detects

↓

Starts new task
Service Responsibilities
Desired count
Want 5 containers

↓

One dies

↓

Creates another
Load Balancer Integration

Automatically registers tasks with

Application Load Balancer

Internet

↓

ALB

↓

Task1

↓

Task2

↓

Task3
Auto Scaling

Example

CPU > 70%

↓

Increase Tasks

↓

5 → 10
Rolling Deployment
Version 1

↓

Replace

↓

Version 2

↓

One container at a time

No downtime.

Interview Question

Difference between Task and Service?

Answer

Task is one running instance of an application.

Service manages multiple Tasks and ensures the desired number are always running.

2. Fargate vs EC2 Launch Type

When creating ECS cluster,

AWS asks

EC2

or

Fargate?
EC2 Launch Type

You manage EC2 machines.

EC2

↓

Docker

↓

ECS Agent

↓

Containers

You maintain

OS
Security patches
Scaling
Storage
AMIs
Advantages

Cheaper at scale.

GPU supported.

Custom AMIs.

Daemon containers.

Full control.

Disadvantages

Need maintenance.

Need scaling.

Need monitoring.

Need patching.

Fargate

Serverless containers.

No EC2.

Your Container

↓

AWS manages servers

You only upload container.

AWS does everything.

Advantages

No servers.

Automatic scaling.

Simple.

Pay only when task runs.

Great for startups.

Disadvantages

More expensive.

Limited customization.

No SSH.

No daemon containers.

Interview Table
Feature	EC2	Fargate
Manage servers	Yes	No
SSH	Yes	No
OS control	Yes	No
Simplicity	Medium	Very High
Cost at scale	Lower	Higher
Startup	Slower	Faster
Best for	Large workloads	Small/medium apps
Interview Answer

Choose EC2 when you need full control, specialized hardware, or lower cost at large scale.

Choose Fargate when you want to avoid server management and focus on deploying containers quickly.

3. EKS Cluster Architecture

Amazon Elastic Kubernetes Service (EKS) is AWS's managed Kubernetes offering.

User

↓

kubectl

↓

API Server

↓

Scheduler

↓

Controller

↓

Worker Nodes

↓

Pods
Control Plane (Managed by AWS)

AWS manages:

API Server
Scheduler
Controller Manager
etcd

You don't patch or maintain these components.

Worker Nodes

You manage:

EC2 nodes (managed node groups)
Or use Fargate for serverless pods

Each worker node runs:

kubelet
kube-proxy
container runtime (typically containerd)
Pod Lifecycle
Deployment

↓

ReplicaSet

↓

Pod

↓

Container
Networking

Each Pod gets its own IP address using the Amazon VPC CNI.

Interview Difference

EKS vs ECS

ECS	EKS
AWS-specific	Kubernetes standard
Easier	More complex
Less flexible	Highly flexible
Smaller learning curve	Steeper learning curve
AWS APIs	Kubernetes APIs
4. Kubernetes Basics for Interviews

Important objects:

Pod

Smallest deployable unit.

Can contain one or more containers.

Deployment

Maintains desired pod replicas and supports rolling updates.

ReplicaSet

Ensures the requested number of Pods are running. Deployments manage ReplicaSets for you.

Service

Provides stable networking to Pods.

Types:

ClusterIP
NodePort
LoadBalancer
ExternalName
ConfigMap

Stores non-sensitive configuration.

Example

APP_ENV=production
Secret

Stores sensitive information.

Example

Database Password
JWT Secret
API Keys
Namespace

Logical isolation inside a cluster.

Example

default

dev

test

prod
Ingress

Provides HTTP/HTTPS routing into the cluster.

StatefulSet

For databases.

Example

MySQL

Redis

Kafka

Provides stable network identities and persistent storage.

DaemonSet

Runs one Pod on every node.

Used for:

Monitoring agents
Log collectors
Security agents
Common kubectl Commands
kubectl get pods

kubectl describe pod mypod

kubectl logs mypod

kubectl exec -it mypod -- bash

kubectl delete pod mypod

kubectl apply -f deployment.yaml
5. ECR Image Scanning & Lifecycle

Amazon Elastic Container Registry (ECR) stores Docker images.

Docker Build

↓

Push

↓

ECR

↓

ECS/EKS Pull
Image Scanning

Scans container images for known vulnerabilities (CVEs).

Example pipeline:

Developer

↓

Build Docker Image

↓

Push to ECR

↓

Scan Image

↓

Deploy only if scan passes

Benefits:

Detects vulnerable packages
Improves security posture
Can block unsafe releases in CI/CD
Lifecycle Policies

Automatically delete old images.

Example

Keep only latest 10 images

↓

Delete remaining images

Benefits:

Saves storage
Reduces costs
Keeps repositories clean
6. Service Mesh with App Mesh

AWS App Mesh is a service mesh for microservices.

Without a mesh:

Service A

↓

HTTP

↓

Service B

Application code handles retries, timeouts, and observability.

With App Mesh:

App

↓

Envoy Sidecar

↓

Network

↓

Envoy Sidecar

↓

App

Each service gets an Envoy proxy.

The proxy handles:

Retries
Timeouts
Traffic routing
Mutual TLS (mTLS)
Metrics
Distributed tracing

Benefits:

Consistent networking
Better observability
Secure service-to-service communication
Advanced traffic control
7. Blue-Green Deployments on ECS

Normal deployment

Version 1

↓

Replace

↓

Version 2

There is some deployment risk if issues appear during rollout.

Blue-Green Deployment

Blue = current production

Blue

↓

Users

Deploy new version separately:

Green

↓

Testing

Switch traffic after validation:

Users

↓

Green

If problems occur:

Green fails

↓

Switch back

↓

Blue
ECS Blue-Green Flow
ECR

↓

New Image

↓

ECS

↓

Green Tasks

↓

Health Check

↓

ALB shifts traffic

↓

Blue removed

This is commonly orchestrated using AWS CodeDeploy with an Application Load Balancer.

Typical Interview Questions
What is the difference between an ECS Task and a Service?
A Task is a running instance of a Task Definition. A Service manages Tasks, maintains the desired count, performs health checks, integrates with load balancers, and supports deployments.
When would you choose Fargate over EC2?
Use Fargate when you want serverless containers with minimal operational overhead. Use EC2 when you need full control, GPUs, custom AMIs, or better cost efficiency at large scale.
Who manages the EKS control plane?
AWS manages the Kubernetes control plane (API server, etcd, scheduler, and controller manager). Customers manage worker nodes unless using Fargate.
How does ECR improve container security?
By scanning images for known vulnerabilities, integrating with CI/CD pipelines, and using lifecycle policies to remove unused images.
What problem does a service mesh solve?
It moves networking concerns such as retries, traffic routing, encryption, observability, and resilience out of application code into a dedicated proxy layer.
Why use Blue-Green deployment instead of Rolling deployment?
Blue-Green offers near-zero downtime, easy rollback, and reduced deployment risk because the old version remains available until the new version is verified.
