1. Why Branching Strategies Exist

Without a strategy:

Developers overwrite each other's work.
Unstable code reaches production.
Releases become difficult.
Bug fixes delay new features.
Merge conflicts increase.

A branching strategy provides a structured workflow.

2. GitFlow

GitFlow is a structured branching model introduced by Vincent Driessen. It works well for projects with scheduled releases.

Branch Structure
                    feature/login
                   /
main ------------develop-----------------------
                 \          \
                  \          feature/payment
                   \
                    release/v1.2
                         \
                          hotfix/v1.2.1
Main Branches
main (or master)
Always production-ready
Contains stable releases only
Every commit is deployable

Example:

main

v1.0 ---- v1.1 ---- v1.2 ---- v1.3

Never develop directly here.

develop

Integration branch.

All completed features merge here first.

feature1
      \
feature2 ---> develop
      /
feature3

Testing happens on develop.

Supporting Branches
Feature Branch

Created from:

develop

Example

git checkout develop

git checkout -b feature/login

Development

develop

↓

feature/login

↓

Coding

↓

Merge back into develop

Delete after merging.

Release Branch

When enough features are complete:

develop

↓

release/v1.2

Purpose

Final testing
Version bump
Documentation
Bug fixes only

No new features.

After release

release/v1.2

↓

main

↓

develop

Both branches receive the release changes.

Hotfix Branch

Production bug?

Example

main

↓

hotfix/payment-crash

Fix

↓

Merge into

main

develop

This keeps both branches synchronized.

Complete GitFlow Example
main
  |
  |--------------------------v1.0-----------------------------
  |                          ^
  |                          |
develop-----------------------|-------------------------------
    |         |              |
    |         |              |
 feature/A  feature/B     release/v1.0
                              |
                           bug fixes
                              |
                           merge to main
                              |
                         merge back to develop
Advantages
Excellent release management
Stable production
Multiple versions supported
Predictable workflow
Disadvantages
Many branches
Frequent merges
Complex for small teams
Slower deployments
Best For
Enterprise software
Banking
Telecom
Long release cycles
Desktop applications
3. GitHub Flow

GitHub Flow is much simpler.

Structure

main

↓

feature branch

↓

Pull Request

↓

Review

↓

Merge

↓

Deploy

Only one permanent branch:

main

Example

git checkout main

git pull

git checkout -b feature/login

Develop

↓

Commit

↓

Push

↓

Create Pull Request

↓

CI runs

↓

Review

↓

Merge

↓

Deploy

Diagram

main
  |
  |---------------------------
   \
    feature/login
           |
        Pull Request
           |
        Code Review
           |
         CI Checks
           |
        Merge
           |
         Deploy
Advantages
Very simple
Continuous deployment friendly
Easy onboarding
Minimal merge conflicts
Ideal for cloud-native applications
Disadvantages
Less suited to maintaining multiple production versions
Can be challenging for long-lived release branches
Best For
SaaS products
Startups
DevOps teams
CI/CD pipelines
Daily deployments
4. Trunk-Based Development

Used by organizations like Google and Netflix.

Only one long-lived branch:

main

Feature branches exist briefly (often a few hours) or developers commit directly to main if allowed by team policy.

Example

main

↓

Developer A

↓

Commit

↓

CI

↓

Developer B

↓

Commit

↓

CI

Typical flow

main
  |
  |----commit
  |
  |----commit
  |
  |----commit
  |
  |----commit

Small commits.

Frequent merges.

Continuous integration.

Feature Flags

Incomplete features are hidden.

Instead of

Long feature branch

Use

Small merge

↓

Feature Flag

↓

Hidden from users
Advantages
Tiny merge conflicts
Fast releases
Continuous deployment
Easy rollback
Better CI performance
Disadvantages
Requires strong automated testing
Requires disciplined developers
Not ideal without CI/CD
Best For
Mature DevOps teams
Microservices
Cloud-native systems
High deployment frequency
5. Comparison
Feature	GitFlow	GitHub Flow	Trunk-Based
Permanent branches	main, develop	main	main
Complexity	High	Low	Low
CI/CD	Moderate	Excellent	Excellent
Release frequency	Scheduled	Frequent	Continuous
Feature branches	Long-lived	Short-lived	Very short-lived
Best for	Enterprise	SaaS	Elite DevOps teams
6. Branch Naming Conventions

Good names make repositories easier to understand.

Feature
feature/login

feature/payment-api

feature/user-profile
Bug Fix
bugfix/login-error

bugfix/token-refresh
Hotfix
hotfix/payment-crash

hotfix/security-patch
Release
release/v1.5

release/2.0
Chore
chore/docker-update

chore/dependency-upgrade
Documentation
docs/api

docs/readme
Refactor
refactor/auth

refactor/database

Many teams include issue IDs.

feature/JIRA-234-login

bugfix/TICKET-91
7. When to Use Each Strategy
GitFlow

Use when

Quarterly releases
Large enterprise
Multiple release versions
Dedicated QA
Long testing cycles

Examples

Banking
Healthcare
ERP software
GitHub Flow

Use when

Daily deployments
CI/CD pipeline
Small teams
SaaS
Startup

Examples

Web applications
APIs
Internal tools
Trunk-Based

Use when

Multiple deployments daily
Excellent automated testing
Mature DevOps culture
Feature flags available

Examples

Large-scale cloud services
Microservices platforms
8. Protecting the main/master Branch

Production branches should never allow unrestricted direct pushes.

Common protections:

No direct pushes
Pull request required
At least one or two approvals
Passing CI required
Resolve conversations before merge
Signed commits (optional)
Linear history or squash merge (optional)
Restrict force pushes
Restrict branch deletion

Example workflow

Developer

↓

Feature Branch

↓

Pull Request

↓

CI

↓

Review

↓

Merge

↓

main

This helps prevent accidental or unreviewed changes from reaching production.

9. Branch Policies Across Platforms
GitHub

Features include:

Protected branches
Required pull requests
Required reviewers
Required status checks (CI)
Code owner reviews
Conversation resolution
Restrict force pushes
Restrict branch deletion

Typical setup:

Settings

↓

Branches

↓

Add Branch Protection Rule

↓

main
GitLab

Supports:

Protected branches
Merge requests
Approval rules
Required pipeline success
Push/merge permissions by role
Code Owners

Typical flow:

Settings

↓

Repository

↓

Protected Branches
Azure DevOps

Branch policies include:

Minimum reviewers
Linked work items
Build validation
Status checks
Merge strategy restrictions
Required comment resolution
Automatic reviewers

Typical path:

Repos

↓

Branches

↓

Branch Policies
DevOps Interview Questions
Question	Expected Answer
Why not commit directly to main?	It risks breaking production, bypasses review, and skips quality gates.
Which workflow is most CI/CD friendly?	GitHub Flow and Trunk-Based Development.
Which workflow is best for enterprise products with scheduled releases?	GitFlow.
Why use feature branches?	They isolate work, simplify reviews, and reduce the impact of unfinished changes.
Why protect the main branch?	To ensure only reviewed, tested, and approved code reaches production.
Why use feature flags with Trunk-Based Development?	They allow incomplete features to be merged safely while keeping them hidden from users.
