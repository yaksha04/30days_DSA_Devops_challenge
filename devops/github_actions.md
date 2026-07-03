What is a GitHub Actions Workflow?

A workflow is an automated process written in YAML that GitHub executes whenever a specified event occurs.

Think of it like this:

Developer pushes code
          │
          ▼
GitHub detects event
          │
          ▼
Workflow starts
          │
          ▼
Build
          │
          ▼
Run Tests
          │
          ▼
Security Scan
          │
          ▼
Create Docker Image
          │
          ▼
Deploy to Server

Instead of doing these manually, GitHub Actions automates everything.

Workflow YAML Structure

Every workflow lives inside

.github/workflows/

Example:

.github/workflows/ci.yml

Basic structure

name: CI Pipeline

on:
  push:

jobs:
  build:

    runs-on: ubuntu-latest

    steps:

      - uses: actions/checkout@v4

      - name: Install dependencies
        run: npm install

      - name: Run tests
        run: npm test

Let's understand every section.

1. name
name: CI Pipeline

Just gives your workflow a readable name.

GitHub UI shows

✔ CI Pipeline

instead of

ci.yml
2. on

This tells GitHub

WHEN should this workflow run?

Example

on:
  push:

Means

Run whenever code is pushed.

Think

Event occurs
↓

Workflow starts
3. jobs

A workflow contains one or more jobs.

Example

jobs:

  build:

  test:

  deploy:

Visual

Workflow

├── Build Job

├── Test Job

└── Deploy Job

Each job runs on a separate machine.

4. runs-on

Specifies the runner machine.

Example

runs-on: ubuntu-latest

GitHub starts

Ubuntu VM

Your code runs there.

Can also use

windows-latest

macos-latest

ubuntu-22.04
5. steps

Each job contains steps.

Example

steps:

- Checkout code

- Install packages

- Run tests

- Build Docker image

- Deploy

Each step executes sequentially.

Step 1

↓

Step 2

↓

Step 3

↓

Done
Step Types

There are two kinds.

A. run

Runs shell commands.

Example

- run: echo Hello

or

- run: python app.py
B. uses

Uses an existing GitHub Action.

Example

- uses: actions/checkout@v4

Instead of writing code yourself, you reuse someone else's action.

Complete Flow
Workflow

↓

Triggered

↓

Job

↓

Runner starts

↓

Step 1

↓

Step 2

↓

Step 3

↓

Success
Triggers

The on: section defines workflow triggers.

Push Trigger
on:
  push:

Runs whenever code is pushed.

git push

↓

Workflow starts

Specific branch

on:
  push:

    branches:

      - main

Only runs for

main

Multiple branches

branches:

- main

- develop

- release/*
Pull Request Trigger
on:
  pull_request:

Runs when

Developer creates PR

↓

CI runs

↓

Merge allowed only if CI passes

Very common interview question.

Only for main

on:

  pull_request:

    branches:

      - main
Schedule Trigger

Cron jobs.

Example

on:

  schedule:

    - cron: '0 2 * * *'

Runs every day

2 AM UTC

Useful for

Cleanup
Database backup
Dependency updates
Nightly tests

Cron format

Minute

Hour

Day

Month

Weekday

Example

30 5 * * *

↓

5:30 AM daily
workflow_dispatch

Manual trigger.

on:

  workflow_dispatch:

Now GitHub UI shows

Run Workflow

button.

Useful for

Deploy whenever you want

OR

Run testing manually

You can also pass inputs.

workflow_dispatch:

  inputs:

    environment:

      type: choice

      options:

      - staging

      - production

Then select

staging

production

before running.

Multiple Triggers
on:

  push:

  pull_request:

  workflow_dispatch:

Runs on

Push

OR

PR

OR

Manual
GitHub Marketplace Actions

Instead of writing everything yourself, GitHub provides reusable Actions.

Example

Checkout Repository

Setup Node

Setup Python

Docker Login

Upload Artifact

Cache Packages

Marketplace is like

Play Store

or

NPM Registry

for CI/CD tasks.

Example

- uses: actions/checkout@v4

This action downloads repository code.

Without it

Runner has NO source code.

Setup Python

- uses: actions/setup-python@v5

  with:

    python-version: 3.11

GitHub installs Python.

Setup Java

- uses: actions/setup-java@v4

Docker Login

- uses: docker/login-action@v3
Reusable Actions

You can create your own.

Example

Organization

↓

Reusable Docker Build Action

↓

Every project uses same action

Instead of copying

100 lines YAML

across repositories.

Secrets

Never hardcode passwords.

Bad

PASSWORD=abc123

Anyone can read.

Instead

GitHub

Settings

↓

Secrets

↓

Actions

↓

New Secret

Example

AWS_ACCESS_KEY

AWS_SECRET_KEY

DOCKER_PASSWORD

SSH_KEY

Accessing Secrets

env:

  PASSWORD: ${{ secrets.DB_PASSWORD }}

or

run: echo "${{ secrets.API_KEY }}"

(Although printing secrets is masked in logs and generally should be avoided.)

Interview Question

Why use Secrets?

Answer

Because they are encrypted, securely stored, masked in logs, and prevent exposing sensitive credentials in the repository.

Environment Variables

Environment variables store configuration values that are not necessarily secret.

Example

env:

  APP_NAME: my-app

  REGION: us-east-1

Access

run: echo $APP_NAME

Difference

Environment Variable	Secret
Visible	Hidden
Non-sensitive	Sensitive
App name	Password
Region	API Key
Matrix Builds

One of GitHub Actions' most powerful features.

Suppose

You support

Python 3.9

Python 3.10

Python 3.11

Instead of writing

Job 1

Job 2

Job 3

Use matrix.

strategy:

  matrix:

    python-version:

      - 3.9

      - 3.10

      - 3.11

Then

- uses: actions/setup-python@v5

  with:

    python-version: ${{ matrix.python-version }}

GitHub automatically creates

Job 1

Python 3.9

↓

Job 2

Python 3.10

↓

Job 3

Python 3.11

All run in parallel.

Huge time saver.

Multiple matrices

matrix:

  os:

    - ubuntu-latest

    - windows-latest

  python:

    - 3.10

    - 3.11

Creates

Ubuntu + 3.10

Ubuntu + 3.11

Windows + 3.10

Windows + 3.11

Automatically.

Self-hosted Runners

Normally GitHub provides runners.

GitHub

↓

Ubuntu VM

↓

Workflow

But suppose you need

GPU
Internal network access
Large memory
Licensed software
Company firewall access

Then use your own machine.

Your Server

↓

Runner software installed

↓

GitHub sends job

↓

Runner executes

Example

runs-on: self-hosted

Or use labels:

runs-on:
  - self-hosted
  - linux
  - x64
Advantages
Full control over hardware and software.
Can access private/internal resources.
No GitHub-hosted time limits for eligible setups.
Disadvantages
You manage updates, security, and scaling.
If the runner is offline, jobs won't run.
Caching Dependencies (actions/cache)

Imagine a Node.js project.

Every workflow does:

npm install

Suppose it downloads 1 GB every time.

Build 1

↓

Download

↓

5 minutes

Build 2

↓

Download again

↓

5 minutes

Wasteful.

Instead, cache dependencies.

- uses: actions/cache@v4

  with:

    path: ~/.npm

    key: npm-${{ hashFiles('package-lock.json') }}
First Run
No cache

↓

Download packages

↓

Store cache
Second Run
Cache exists

↓

Restore packages

↓

Skip download

Build becomes much faster.

Common cache locations:

npm: ~/.npm
pip: ~/.cache/pip
Maven: ~/.m2/repository
Gradle: ~/.gradle/caches
Interview Question

Why is hashFiles('package-lock.json') used?

Because if dependencies change, the lock file changes, generating a new cache key. GitHub then creates a fresh cache instead of reusing outdated dependencies.

Artifacts

Artifacts are files produced during one job that you want to:

Download later from the workflow.
Pass to another job in the same workflow.

Example

Build Job

↓

Creates

app.jar

↓

Upload Artifact

↓

Test Job downloads

↓

Deploy Job downloads
Upload Artifact
- uses: actions/upload-artifact@v4

  with:

    name: app-build

    path: build/

Uploads the build/ directory.

Download Artifact
- uses: actions/download-artifact@v4

  with:

    name: app-build

The files are restored into the runner for that job.

Why use artifacts?

Without artifacts:

Build Job

↓

Creates binary

↓

Runner destroyed

↓

Deploy Job starts

↓

Binary is gone

Remember: each job runs on a fresh runner.

Artifacts solve this.

Build

↓

Upload

↓

GitHub stores artifact

↓

Deploy

↓

Download artifact

↓

Deploy
Putting It All Together

A typical production CI/CD pipeline looks like this:

Developer Pushes Code
          │
          ▼
Trigger (push / pull_request)
          │
          ▼
Checkout Repository
          │
          ▼
Restore Cache
          │
          ▼
Install Dependencies
          │
          ▼
Matrix Build (Python 3.10, 3.11)
          │
          ▼
Run Unit Tests
          │
          ▼
Build Application
          │
          ▼
Upload Artifact
          │
          ▼
Deploy Job Downloads Artifact
          │
          ▼
Deploy to Staging/Production
Interview Cheat Sheet
Topic	Key Point
Workflow	A YAML file defining automated CI/CD processes.
on	Specifies the events that trigger the workflow (push, PR, schedule, manual).
Jobs	Independent units of work that run on separate runners.
Steps	Sequential tasks within a job.
run	Executes shell commands.
uses	Reuses existing GitHub Actions.
Secrets	Encrypted credentials (API keys, passwords, tokens).
Environment Variables	Configuration values shared with jobs or steps.
Matrix Build	Runs the same job across multiple versions or operating systems in parallel.
Self-hosted Runner	Your own machine executes workflows instead of GitHub-hosted infrastructure.
Cache	Speeds up workflows by reusing downloaded dependencies across runs.
Artifacts	Store and transfer build outputs between jobs or allow later download.
Common Interview Questions
Why does every workflow usually start with actions/checkout?
Because runners start with an empty workspace. actions/checkout downloads your repository so subsequent steps can access the code.
What's the difference between cache and artifacts?
Cache: Speeds up future workflow runs by reusing dependencies.
Artifacts: Preserve build outputs (binaries, reports, logs) for later jobs or downloads.
Can jobs share files directly?
No. Jobs run on separate, fresh runners. Use artifacts to transfer files between jobs.
When would you choose a self-hosted runner?
When you need specialized hardware (GPUs), access to internal networks, custom software, or greater control over the execution environment.
