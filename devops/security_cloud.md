# Availability Zones vs Regions

AWS infrastructure is divided into Regions and Availability Zones (AZs).

## Region

A Region is a geographical area containing multiple isolated data centers.

Examples:

* Mumbai (ap-south-1)
* Singapore (ap-southeast-1)
* Frankfurt (eu-central-1)

Characteristics:

* Physically separated locations
* Independent power, networking, and infrastructure
* Used for global deployment and disaster recovery

Example:

User in India → Mumbai Region

User in Europe → Frankfurt Region

---

## Availability Zone (AZ)

An Availability Zone is one or more data centers within a Region.

Example:

Mumbai Region
├── ap-south-1a
├── ap-south-1b
└── ap-south-1c

Characteristics:

* Isolated from other AZs
* Connected through high-speed private networking
* Designed to prevent a single data center failure from affecting the entire application

Example:

Web Server → AZ-1a

Database → AZ-1b

If AZ-1a fails, the application can continue running from another AZ.

---

## Region vs Availability Zone

| Feature        | Region                       | Availability Zone              |
| -------------- | ---------------------------- | ------------------------------ |
| Scope          | Geographic area              | Data center(s) within a region |
| Distance       | Hundreds of kilometers apart | Usually within the same region |
| Use Case       | Disaster Recovery            | High Availability              |
| Latency        | Higher                       | Very Low                       |
| Failure Impact | Regional Disaster            | Data Center Failure            |

---

# RTO vs RPO

These are two of the most important disaster recovery metrics.

---

## RTO (Recovery Time Objective)

RTO defines how quickly a system must be restored after a failure.

Question:

"How long can the business remain unavailable?"

Example:

RTO = 1 Hour

Meaning:

If the application crashes at 10:00 AM, it must be restored by 11:00 AM.

Lower RTO requires:

* Automation
* Backup infrastructure
* Fast failover mechanisms

---

## RPO (Recovery Point Objective)

RPO defines how much data loss is acceptable.

Question:

"How much data can the business afford to lose?"

Example:

RPO = 15 Minutes

Meaning:

If a disaster occurs at 10:00 AM, data loss should not exceed the last 15 minutes.

Lower RPO requires:

* Frequent backups
* Continuous replication
* Real-time synchronization

---

## RTO vs RPO Example

Banking Application:

RTO = 5 Minutes
RPO = 0 Minutes

Reason:

* Service must recover quickly
* No transaction loss allowed

Blog Website:

RTO = 4 Hours
RPO = 1 Hour

Reason:

* Some downtime is acceptable
* Minor data loss may be tolerated

---

# Active-Passive vs Active-Active

These are disaster recovery architectures.

---

## Active-Passive

One environment serves traffic.

The second environment remains on standby.

Architecture:

Active Server
↓
Serves Users

Passive Server
↓
Waiting for Failure

If Active fails:

Traffic shifts to Passive.

Advantages:

* Lower cost
* Easier management
* Simpler architecture

Disadvantages:

* Resources remain underutilized
* Failover may take time

Use Cases:

* Small and medium businesses
* Cost-sensitive applications

---

## Active-Active

Both environments serve traffic simultaneously.

Architecture:

Users
↓      ↓
Server A  Server B

Both process requests.

If one fails:

Remaining server continues serving traffic.

Advantages:

* High availability
* Better performance
* Near-zero downtime

Disadvantages:

* Higher cost
* More complexity

Use Cases:

* Banking
* E-commerce
* Large SaaS platforms

---

## Active-Passive vs Active-Active

| Feature     | Active-Passive | Active-Active |
| ----------- | -------------- | ------------- |
| Cost        | Lower          | Higher        |
| Utilization | Partial        | Full          |
| Complexity  | Lower          | Higher        |
| Downtime    | Some           | Minimal       |
| Scalability | Limited        | High          |

---

# Health Checks and Failover

Health checks continuously monitor application availability.

Question:

"Is the server healthy?"

Common checks:

* HTTP response checks
* TCP connectivity checks
* Database connectivity checks
* Application endpoint checks

Example:

GET /health

Response:

200 OK

Healthy

If the response fails repeatedly:

Server marked unhealthy.

---

## Failover

Failover automatically redirects traffic to healthy resources.

Example:

Primary Server
↓
Health Check Fails
↓
Load Balancer Detects Failure
↓
Traffic Redirected
↓
Secondary Server

Result:

Application remains available.

AWS services supporting failover:

* Route 53
* Elastic Load Balancer
* Auto Scaling Groups
* Multi-AZ RDS

---

# Fault Tolerance Design Patterns

Fault tolerance means the system continues working even when components fail.

Goal:

Eliminate single points of failure.

---

## Pattern 1: Redundancy

Multiple copies of resources.

Example:

Two Web Servers
Two Databases
Multiple AZs

If one fails, another takes over.

---

## Pattern 2: Load Balancing

Distribute traffic across multiple servers.

Benefits:

* Better performance
* High availability
* Automatic failover

Example:

Users
↓
Load Balancer
↓       ↓
Web1    Web2

---

## Pattern 3: Auto Scaling

Automatically add or remove servers based on demand.

Benefits:

* Improved reliability
* Handles sudden traffic spikes
* Prevents overload

---

## Pattern 4: Database Replication

Maintain multiple copies of data.

Primary Database
↓
Replica Database

If Primary fails:

Replica becomes Primary.

---

## Pattern 5: Queue-Based Architecture

Use services like SQS between components.

Benefits:

* Loose coupling
* Better fault isolation
* Improved reliability

Example:

Application
↓
Queue
↓
Worker

If Worker fails:

Messages remain safely stored.

---

## Pattern 6: Circuit Breaker

Prevent cascading failures.

Example:

Service A calls Service B.

If Service B becomes unhealthy:

Circuit Breaker stops requests temporarily.

Benefits:

* Prevents resource exhaustion
* Improves resilience

---

# Multi-AZ Deployment

Multi-AZ means deploying resources across multiple Availability Zones within the same Region.

Example:

Mumbai Region

AZ-1a
└─ Web Server

AZ-1b
└─ Web Server

Load Balancer
└─ Distributes Traffic

If AZ-1a fails:

Traffic automatically shifts to AZ-1b.

Users experience little or no downtime.

---

## Multi-AZ Database Example

Primary RDS Database
↓
Synchronous Replication
↓
Standby RDS Database

If Primary fails:

AWS automatically promotes Standby.

Benefits:

* High availability
* Automatic failover
* Minimal downtime
* No manual intervention

---

# Interview Revision

Availability Zone: One or more isolated data centers within a Region.

Region: Geographic area containing multiple Availability Zones.

RTO: Maximum acceptable recovery time after a disaster.

RPO: Maximum acceptable data loss after a disaster.

Active-Passive: One system serves traffic while another waits for failure.

Active-Active: Multiple systems serve traffic simultaneously.

Health Check: Continuous monitoring of resource health.

Failover: Automatic traffic redirection to healthy resources.

Fault Tolerance: Ability to continue operating despite failures.

Multi-AZ: Deploying resources across multiple Availability Zones for high availability.
