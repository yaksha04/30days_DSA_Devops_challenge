1. AWS Lambda Execution Model & Cold Starts
What is Lambda?

Lambda is a serverless compute service where AWS runs your code without you managing servers.

You only upload code.

AWS handles:

Server provisioning
OS
Scaling
Availability
Security patches

You pay only for execution time.

Lambda Execution Lifecycle

Suppose a user uploads a photo.

User
   │
   ▼
API Gateway
   │
   ▼
Lambda Function
   │
   ▼
Resize Image
   │
   ▼
Store in S3

Now understand what happens internally.

Step 1: Event Arrives

Example

HTTP Request
S3 Upload
SQS Message
Cron Event

AWS receives the event.

Step 2: Execution Environment

AWS checks:

"Do I already have a running environment?"

If YES

Reuse existing container

If NO

Create new environment

This environment contains

Runtime (Python, Java, Node)
Memory
CPU
Network
Temporary storage
Step 3: Initialization Phase

AWS loads

Code
Libraries
Dependencies
Environment Variables

Example

import boto3

client = boto3.client("s3")

All imports happen during initialization.

Step 4: Invoke Handler

Example

def lambda_handler(event, context):
    return "Hello"

Only handler executes for every request.

Step 5: Freeze

After execution

AWS doesn't destroy immediately.

It freezes the environment.

Execution Completed

↓

Freeze Container

↓

Wait
Step 6: Reuse

If another request arrives

Reuse Same Container

No initialization required.

This is called

Warm Start

Cold Start

Cold Start means

AWS had to create a new execution environment before running code.

Request

↓

No Existing Container

↓

Create Runtime

↓

Load Dependencies

↓

Run Handler

Extra startup time occurs.

Warm Start
Request

↓

Existing Container

↓

Run Handler Immediately

Much faster.

Why Cold Starts Happen
First invocation
Scaling to new instances
Long inactivity
Deployment of new code
Runtime updates
Factors Affecting Cold Starts
Runtime

Fast

Python
Node.js

Slower

Java
.NET
Package Size

Small package

20MB

Loads faster.

Large package

300MB

Takes longer.

VPC

Earlier

Lambda inside a VPC had higher cold starts because ENIs had to be attached.

AWS has improved this significantly, but VPC-attached Lambdas can still introduce some additional startup overhead depending on networking.

Memory

More memory

↓

More CPU

↓

Faster initialization

Reducing Cold Starts
1. Keep package small

Remove unnecessary libraries.

2. Lazy loading

Instead of

import pandas

Load only when needed.

3. Provisioned Concurrency

AWS keeps execution environments warm.

No cold start.

Always Ready

Costs extra.

4. Use lightweight runtimes

Python

Node.js

Usually start faster than Java.

Interview Questions
What is a cold start?

Cold start is the additional latency introduced when Lambda creates a new execution environment because no warm environment is available.

What causes cold starts?
New instance creation
Scaling
Idle timeout
New deployment
Difference between Cold and Warm Start
Cold	Warm
New environment	Existing environment
Initialization	No initialization
Slower	Faster
2. Lambda Layers & Extensions
Lambda Layers

Layers allow you to share common code or libraries across multiple Lambda functions.

Imagine 100 functions all need NumPy.

Without Layers

Lambda 1
 NumPy

Lambda 2
 NumPy

Lambda 3
 NumPy

Huge duplication.

With Layers

Layer
 ├── NumPy
 ├── boto3 helpers
 ├── Common Utils

↓

Attached to many Lambdas
Benefits
Smaller deployment packages
Easier updates
Shared libraries
Reusable code
Example
Layer

requests
numpy
pandas

Every Lambda imports them.

Lambda Extensions

Extensions add extra capabilities to the Lambda execution environment without modifying your application code.

Examples

Monitoring
Logging
Security agents
Secrets retrieval

Common use cases:

Sending logs to observability platforms
Collecting metrics and traces
Fetching secrets before invocation
Interview

Difference?

Layer

Shared code

Extension

Additional runtime capability
3. Event Sources

Lambda is event-driven.

API Gateway
Client

↓

API Gateway

↓

Lambda

Used for

REST APIs

GraphQL

Backend APIs

SQS
Application

↓

SQS Queue

↓

Lambda

Lambda polls SQS and processes messages asynchronously.

Benefits

Reliable
Retry support
Decoupling
S3
Upload File

↓

S3 Event

↓

Lambda

Common examples

Resize images
Generate thumbnails
Virus scan
Data processing
Amazon DynamoDB Streams Streams

Whenever a table changes

INSERT

UPDATE

DELETE

A stream record is created.

Lambda reads stream records.

Useful for

Auditing
Replication
Notifications
Event-driven architectures
Interview

Which event source is synchronous?

API Gateway

Which are asynchronous?

SQS
S3
DynamoDB Streams
4. Lambda Concurrency & Throttling
What is Concurrency?

Concurrency = Number of Lambda invocations executing simultaneously.

Example

100 requests arrive.

100 Concurrent Executions

AWS creates as many execution environments as needed (within limits).

Reserved Concurrency

Guarantees capacity for a function and also limits its maximum concurrency.

Reserved = 50

Maximum = 50
Minimum guaranteed = 50
Provisioned Concurrency

Keeps environments initialized.

No cold start.

Account Limit

Default account concurrency is limited (the exact default can vary by account and region, commonly around 1,000 and can be increased by request).

Example

Limit

1000

Request

1200

Extra

200

↓

Throttled
Throttling

Occurs when concurrency limit is exceeded.

Behavior depends on event source.

API Gateway

Returns error (typically 429 or 502/504 depending on integration and timeout scenarios)

SQS

Messages stay in queue and Lambda retries later.
Interview

Difference?

Reserved

Reserve Capacity

Provisioned

Warm Capacity
5. Lambda@Edge vs CloudFront Functions

Both execute code at edge locations, but they solve different problems.

Feature	Lambda@Edge	CloudFront Functions
Runtime	Full Lambda runtimes	Lightweight JavaScript runtime
Startup	Higher	Extremely low latency
Duration	Up to seconds	Milliseconds
Network access	Can make network calls	No network calls
Use cases	Authentication, image processing, origin request/response customization	Header manipulation, redirects, URL rewrites, cache key changes
Cost	Higher	Lower
CloudFront Functions

Ideal for

Redirect

Header Add

Authentication Token Check

URL Rewrite

Extremely fast.

Lambda@Edge

Suitable for more advanced processing:

Generate dynamic content
Modify origin requests/responses
Perform authentication with external services
Image transformation
Interview

Which is faster?

CloudFront Functions.

Which is more powerful?

Lambda@Edge.

6. AWS Step Functions State Machines

Step Functions orchestrate multiple services into workflows.

Instead of writing orchestration logic inside Lambda code, define the workflow declaratively.

Example

Order Placed

↓

Validate Order

↓

Check Inventory

↓

Payment

↓

Ship

↓

Notify User
State Machine

A workflow consists of states.

Example

Start

↓

Task

↓

Choice

↓

Wait

↓

Parallel

↓

Success
Common State Types
Task

Run a Lambda or another AWS service.

Choice

Decision making.

if payment success

↓

Ship

Else

↓

Refund
Wait

Pause execution.

Useful for retries or delayed processing.

Parallel

Execute multiple branches simultaneously.

Example

Generate Invoice

AND

Send Email

AND

Update Inventory
Fail

Workflow failed.

Succeed

Workflow completed.

Benefits
Visual workflow
Retries
Error handling
Long-running workflows
Reduced application complexity
Interview

Why Step Functions?

Instead of writing orchestration logic in code, you define workflows with built-in retry, branching, error handling, and service integrations.

7. Amazon EventBridge Rules & Event Patterns

EventBridge routes events from AWS services, SaaS applications, or custom applications to targets such as Lambda, SQS, or Step Functions.

S3

EC2

CodePipeline

↓

EventBridge

↓

Rule

↓

Lambda
Rule

A rule determines:

Which events to match
Which target to invoke
Event Pattern

Filters events based on content.

Example

{
  "source": ["aws.s3"],
  "detail-type": ["Object Created"]
}

Only S3 object creation events match.

Scheduled Rules

EventBridge can also trigger jobs on a schedule.

Example

Every day

9 AM

↓

Run Lambda

(Cron or rate expressions are commonly used.)

Targets

A rule can invoke:

Lambda
SQS
SNS
Step Functions
ECS Tasks
Kinesis
API destinations
Interview Questions
What is EventBridge?

A fully managed event bus that routes events from producers to consumers based on rules.

Difference between EventBridge and SQS
EventBridge	SQS
Event routing	Message queue
Filters events	Stores messages
One event can fan out to multiple targets	One message is consumed from a queue
Supports scheduled events	No scheduling capability
⭐ Interview Cheat Sheet (Remember These)
Topic	One-line Answer
Lambda	Serverless compute service that runs code on demand without managing servers.
Cold Start	Extra startup latency when AWS creates a new execution environment.
Warm Start	Reuse of an existing execution environment for faster execution.
Lambda Layer	Reusable package of shared code or libraries for multiple functions.
Lambda Extension	Adds capabilities like logging, monitoring, or security to the execution environment.
API Gateway	Synchronous HTTP trigger for Lambda.
SQS	Queue-based asynchronous Lambda trigger with retries.
S3	Object storage events can trigger Lambda on uploads or deletions.
DynamoDB Streams	Emits table change records that Lambda can process.
Concurrency	Number of Lambda executions running simultaneously.
Throttling	Requests are limited when concurrency quotas are exceeded.
Provisioned Concurrency	Pre-initialized execution environments to reduce or eliminate cold starts.
Reserved Concurrency	Guarantees and limits concurrency for a specific Lambda function.
CloudFront Functions	Ultra-low-latency edge code for lightweight request/response manipulation.
Lambda@Edge	More powerful edge execution for advanced request/response processing.
Step Functions	Workflow orchestration service using state machines.
EventBridge	Event bus that routes events to targets using rules and event patterns.
