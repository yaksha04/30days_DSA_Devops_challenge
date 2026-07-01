1. Continuous Integration (CI)
Definition

Continuous Integration (CI) is the practice of frequently merging code changes into a shared repository (usually several times a day), where every merge automatically triggers a pipeline that builds and tests the application.

Instead of developers working separately for weeks, everyone integrates code continuously.

Goal
Detect bugs early
Reduce merge conflicts
Keep the codebase always working
Automate testing
Traditional Development (Without CI)

Imagine four developers.

Developer A --------\
Developer B ---------\

Developer C -----------> Merge after 3 weeks

Developer D --------/

Problems:

Huge merge conflicts
Difficult debugging
Multiple broken features
Last-minute integration failures
Development With CI
Developer A --> Push

            \
Developer B --> Push ---> CI Pipeline

            /

Developer C --> Push

Developer D --> Push

Every push automatically triggers:

Code Push

↓

Compile

↓

Run Unit Tests

↓

Run Linting

↓

Security Scan

↓

Build Artifact

Developers immediately know if something broke.

CI Workflow
Write Code

↓

Commit

↓

Push to Git

↓

Pipeline Starts

↓

Install Dependencies

↓

Compile

↓

Run Tests

↓

Quality Checks

↓

Success / Failure Notification
Popular CI Tools
Jenkins
GitHub Actions
GitLab CI/CD
CircleCI
Travis CI
Azure Pipelines
Bitbucket Pipelines
Example

Developer pushes:

git add .
git commit -m "Added login feature"
git push

Pipeline automatically runs:

Install packages

↓

Build application

↓

Run tests

↓

Code quality

↓

Create Docker image

No human intervention.

Benefits
Faster feedback
Better code quality
Early bug detection
Less merge conflicts
Automated testing
Stable main branch
2. Continuous Delivery vs Continuous Deployment

These are often confused.

Continuous Delivery

Definition:

Software is always ready for production, but deployment requires manual approval.

Pipeline:

Code

↓

Build

↓

Test

↓

Deploy to Staging

↓

Manual Approval

↓

Production

Developer clicks:

Deploy

Examples:

Banking applications
Government software
Healthcare
Insurance

Because humans verify before release.

Example
Git Push

↓

CI Pipeline

↓

Docker Image

↓

Deploy to Test

↓

QA Testing

↓

Manager Approval

↓

Deploy Production
Continuous Deployment

Everything is fully automatic.

If all tests pass:

Production Deployment Happens Automatically

Pipeline:

Push

↓

Build

↓

Tests

↓

Deploy Production

No manual approval.

Example

Netflix-style deployment

Developer Push

↓

Pipeline

↓

Tests

↓

Production

Users immediately receive the update.

Difference Table
Feature	Continuous Delivery	Continuous Deployment
Human approval	Yes	No
Production deployment	Manual	Automatic
Risk	Lower	Higher
Speed	Medium	Very Fast
Suitable for	Banks, Healthcare	SaaS, Startups
Interview Question

Can every company use Continuous Deployment?

No.

Industries like finance, healthcare, defense, and government usually require manual approvals because of compliance, audits, and regulations.

3. Pipeline Stages

A CI/CD pipeline is a sequence of automated steps.

Source

↓

Build

↓

Test

↓

Deploy

Let's understand each.

Stage 1 — Source

This is where code comes from.

Examples:

GitHub
GitLab
Bitbucket
Azure Repos

Trigger:

git push

↓

Webhook

↓

Pipeline Starts
Stage 2 — Build

Convert source code into a runnable package.

Examples:

Java

Source Code

↓

Maven

↓

JAR

Python

Requirements

↓

Install Packages

↓

Package

Docker

Dockerfile

↓

Docker Image
Build Output
Source Code

↓

Compiled Binary

↓

Docker Image

↓

ZIP

↓

WAR

↓

JAR

These outputs are called artifacts.

Stage 3 — Test

Automated testing.

Examples:

Unit Tests
Login()

↓

Check Password
Integration Tests
Frontend

↓

Backend

↓

Database
End-to-End Tests
User Login

↓

Dashboard Opens

↓

Logout
Other Pipeline Checks

Linting

flake8

eslint

pylint

Security

Trivy

Bandit

Snyk

Code Coverage

pytest --cov
Stage 4 — Deploy

Deploy application.

Possible targets:

Docker

↓

Kubernetes

↓

AWS EC2

↓

Azure VM

↓

GCP

↓

Serverless

Deployment Strategies:

Rolling
Blue-Green
Canary
Recreate
Complete Pipeline
Git Push

↓

Checkout Code

↓

Install Dependencies

↓

Compile

↓

Unit Tests

↓

Integration Tests

↓

Security Scan

↓

Build Docker Image

↓

Push Image

↓

Deploy Kubernetes
4. Artifacts and Artifact Storage
What is an Artifact?

An artifact is the output produced by the build stage that is ready to be deployed or shared.

Examples:

app.jar

backend.war

website.zip

docker image

python wheel (.whl)

npm package
Why Store Artifacts?

Without artifact storage:

Need to rebuild every deployment.

With artifact storage:

Build Once

↓

Store

↓

Deploy Same Artifact Everywhere

This ensures that testing and production use the exact same build, reducing inconsistencies.

Artifact Repositories

Common artifact storage solutions:

JFrog Artifactory
Sonatype Nexus Repository
GitHub Packages
AWS CodeArtifact
Container registries such as Docker Hub, Amazon Elastic Container Registry (ECR), and Google Artifact Registry.
Artifact Flow
Build

↓

Artifact Created

↓

Store Repository

↓

Deploy to Dev

↓

Deploy Same Artifact

↓

Deploy to Staging

↓

Deploy Same Artifact

↓

Deploy Production

No rebuilding.

5. Pipeline as Code
Definition

Instead of configuring pipelines through a web UI, the entire pipeline is defined in a version-controlled file stored with the application's source code.

Examples:

Jenkinsfile
.github/workflows/ci.yml
.gitlab-ci.yml
azure-pipelines.yml
Example (GitHub Actions)
name: CI

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Install
        run: pip install -r requirements.txt

      - name: Test
        run: pytest

      - name: Build
        run: docker build -t app .
Advantages
Version controlled
Code review possible
Easy rollback
Reusable
Consistent across environments
Supports automation and Infrastructure as Code practices
6. Fail-Fast Strategy in Pipelines
Definition

A fail-fast pipeline stops execution immediately when a critical step fails instead of continuing with later stages.

Without Fail-Fast
Build ❌

↓

Tests

↓

Security Scan

↓

Deploy

This wastes time and compute resources because later stages cannot succeed after a failed build.

With Fail-Fast
Build ❌

↓

Pipeline Stops

No unnecessary work.

Another Example
Unit Tests ❌

↓

Pipeline Ends

(No Integration Tests)

(No Docker Build)

(No Deployment)
Benefits
Faster feedback to developers
Saves compute time and cost
Prevents invalid deployments
Makes failures easier to diagnose
Encourages fixing issues immediately
7. Idempotency in Deployments
Definition

An operation is idempotent if running it multiple times produces the same final state as running it once.

This is a core principle in reliable deployments and Infrastructure as Code.

Example 1 — Creating a Directory

Bad:

mkdir logs

If the directory already exists:

Error

Good:

mkdir -p logs

Whether you run it once or ten times, the directory exists and no error occurs.

Example 2 — Configuration Management

Desired state:

Nginx Installed

Tool checks:

Already Installed?

↓

Yes

↓

Do Nothing

Running the automation repeatedly does not reinstall Nginx unnecessarily.

Example 3 — Infrastructure as Code

Using Terraform:

terraform apply

↓

EC2 Created

Running again:

terraform apply

↓

No Changes

Terraform compares the desired state with the current state and only applies necessary changes.

Example 4 — Kubernetes

Deployment manifest:

replicas: 3

If the cluster already has three healthy pods:

kubectl apply

↓

No Change

If only two pods are running:

kubectl apply

↓

Creates One More Pod

The system converges to the declared desired state.

Why Idempotency Matters

Without idempotency:

Deploy

↓

Create Database Again

↓

Duplicate Users

↓

Multiple Servers

↓

Production Issues

With idempotency:

Deploy

↓

Current State Checked

↓

Only Missing Changes Applied

↓

Consistent Environment
CI/CD Flow (Complete Picture)
Developer

↓

Git Push

↓

CI Trigger

↓

Checkout Source

↓

Install Dependencies

↓

Build

↓

Unit Tests

↓

Integration Tests

↓

Security Scan

↓

Create Artifact

↓

Store Artifact

↓

Deploy Dev

↓

Deploy Staging

↓

Manual Approval (Continuous Delivery only)

↓

Deploy Production
