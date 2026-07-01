1. HCL Syntax: Providers, Resources, Variables, Outputs

Terraform uses HCL (HashiCorp Configuration Language), a declarative language used to describe infrastructure.

Instead of writing how to create infrastructure, you describe what infrastructure you want.

Example:

provider "aws" {
  region = "ap-south-1"
}

resource "aws_instance" "web" {
  ami           = "ami-0abcdef12345"
  instance_type = "t2.micro"
}

variable "instance_name" {
  type    = string
  default = "my-server"
}

output "public_ip" {
  value = aws_instance.web.public_ip
}
Provider

A provider is a plugin that lets Terraform communicate with a platform.

Examples:

AWS
Azure
Google Cloud
Kubernetes
Docker
GitHub

Example:

provider "aws" {
  region = "us-east-1"
}

Terraform downloads the provider during:

terraform init
Resource

A resource is anything Terraform creates or manages.

Examples:

EC2
VPC
S3 Bucket
Security Group
IAM User

Syntax

resource "<TYPE>" "<NAME>" {

}

Example

resource "aws_s3_bucket" "logs" {
  bucket = "company-log-storage"
}

Here

Resource Type:

aws_s3_bucket

Local Name:

logs

Reference:

aws_s3_bucket.logs.id
Variables

Variables make code reusable.

Without variables:

instance_type = "t2.micro"

With variables:

variable "instance_type" {
  default = "t2.micro"
}

Use:

instance_type = var.instance_type

Override values:

terraform apply \
-var="instance_type=t3.medium"

or

terraform.tfvars
instance_type = "t3.large"
Outputs

Outputs expose values after deployment.

Example

output "server_ip" {
  value = aws_instance.web.public_ip
}

Output:

server_ip = 13.234.100.22

Useful for:

EC2 IP
Load Balancer DNS
Database endpoint
VPC ID
2. terraform init, plan, apply, destroy

Terraform lifecycle consists of four primary commands.

terraform init

Initializes the project.

terraform init

It:

Downloads providers
Creates .terraform/
Installs plugins
Initializes backend

Think of it as:

"Prepare Terraform."

Run only when:

Starting project
Adding provider
Changing backend
terraform plan

Shows what Terraform will do.

terraform plan

Output example:

+ create EC2
+ create Security Group

Plan: 2 to add.

Nothing changes.

Only previews.

terraform apply

Actually creates infrastructure.

terraform apply

Terraform:

Reads configuration
Compares with state
Creates resources
Updates state
terraform destroy

Deletes everything managed by Terraform.

terraform destroy

Output:

Destroy complete!

Only removes Terraform-managed resources.

Complete Workflow
Write HCL

↓

terraform init

↓

terraform plan

↓

terraform apply

↓

Infrastructure Created

↓

terraform destroy
3. State File: What It Is and Why It Matters

Terraform keeps track of infrastructure in a state file.

File:

terraform.tfstate

It stores:

Resource IDs
Attributes
Dependencies
Current infrastructure

Example

Instead of asking AWS every time,

Terraform remembers:

EC2 ID

i-02345

Public IP

13.125.xx.xx

AMI

ami-123
Why State Matters

Without state Terraform wouldn't know:

What already exists
What changed
What to update
What to delete

Terraform compares:

Configuration

vs

State

vs

Actual Infrastructure

Then calculates the difference.

This is called the execution plan.

Problems with Local State

If multiple engineers use:

terraform.tfstate

Problems:

Lost state
Overwritten state
Conflicts
Corruption

Hence remote state.

4. Remote State: S3 + DynamoDB Locking

Production teams never store state locally.

Typical architecture:

Developer

↓

Terraform

↓

S3 Bucket
(terraform.tfstate)

↓

DynamoDB Table
(State Lock)
S3

Stores:

terraform.tfstate

Benefits:

Centralized
Versioning
Backup
Shared
DynamoDB Locking

Imagine:

Developer A

terraform apply

At the same time

Developer B

terraform apply

Without locking:

State Corruption

DynamoDB creates a lock.

Example:

Lock Acquired

↓

Terraform Running

↓

Lock Released

Only one apply can happen at a time.

Backend example

terraform {
  backend "s3" {
    bucket         = "company-tf-state"
    key            = "prod/network.tfstate"
    region         = "ap-south-1"
    dynamodb_table = "terraform-lock"
  }
}
5. Terraform Modules — Reusable Components

A module is a reusable collection of Terraform code.

Without modules:

EC2 code

Repeated

10 times

With modules:

EC2 Module

↓

Reusable Everywhere

Folder

modules/

    ec2/

        main.tf

        variables.tf

        outputs.tf

Call module

module "webserver" {
  source = "./modules/ec2"

  instance_type = "t2.micro"
}

Benefits:

Reusable
Standardized
Easier maintenance
Less duplication
Team collaboration
Types of Modules
Root Module

Current directory.

terraform apply

runs here.

Child Module

Imported module.

module "network" {

}
Registry Module

Downloaded from the public registry.

Example:

module "vpc" {
  source = "terraform-aws-modules/vpc/aws"
}
6. Data Sources vs Resources

This is a very common interview question.

Resource

Creates or manages infrastructure.

Example

resource "aws_instance" "web" {

}

Terraform creates the EC2 instance.

Data Source

Reads existing infrastructure.

Example

data "aws_ami" "ubuntu" {

}

Terraform finds the latest Ubuntu AMI but does not create it.

Example

Already existing VPC

Production VPC

Instead of creating another:

data "aws_vpc" "prod" {

}

Now reference:

data.aws_vpc.prod.id
Difference
Resource	Data Source
Creates infrastructure	Reads existing infrastructure
Managed by Terraform	Not created by Terraform
Can update/delete	Read-only
Changes state	Reads values into state for reference without creating the object
7. Count vs for_each for Multiple Resources

Both create multiple resources.

But they work differently.

count

Uses numeric indexes.

Example

resource "aws_instance" "web" {
  count = 3
}

Creates:

web[0]

web[1]

web[2]

Reference

aws_instance.web[1].id
Problems

If middle resource deleted:

0

1

2

becomes

0

2

Terraform may recreate resources because indexes shift.

for_each

Uses keys instead of indexes.

Example

resource "aws_instance" "web" {

  for_each = {
    dev  = "t2.micro"
    test = "t2.small"
    prod = "t3.medium"
  }

  instance_type = each.value
}

Resources:

web["dev"]

web["test"]

web["prod"]

Much safer.

Keys don't change.

Difference
count	for_each
Numeric index	Key-based
Best for identical resources	Best for unique resources
Index shifting problem	Stable resource identities
Uses count.index	Uses each.key and each.value

Rule of thumb:

Use count when creating a fixed number of nearly identical resources.
Use for_each when resources have unique names, configurations, or identities.
8. Terraform Workspace Concept

A workspace lets you manage multiple state files from the same Terraform configuration.

Example:

Same code

↓

Dev

↓

QA

↓

Staging

↓

Production

Each workspace has its own state.

Example

default

dev

test

prod

Commands

Create workspace

terraform workspace new dev

List

terraform workspace list

Switch

terraform workspace select prod

Show current

terraform workspace show
Example

Current workspace:

dev

Creates:

Dev EC2

Switch:

terraform workspace select prod

Run:

terraform apply

Now it creates:

Production EC2

Same code.

Different state.

When to Use Workspaces

Use workspaces when:

You want separate state for environments (for example, dev, test, and prod) while keeping the infrastructure configuration mostly the same.
You need isolated deployments without duplicating Terraform code.

For significantly different infrastructure between environments, many teams prefer separate directories or repositories instead of relying only on workspaces.

Frequently Asked Interview Questions
Q1. Why is terraform plan important?

It previews the execution plan by comparing the configuration, current state, and actual infrastructure, allowing you to review changes before they are applied.

Q2. Why shouldn't terraform.tfstate be committed to Git?

The state file can contain sensitive information (such as resource IDs, IPs, and sometimes secrets) and often changes frequently, causing merge conflicts. Teams typically use a remote backend like S3 instead.

Q3. Why use modules?

Modules promote code reuse, consistency, easier maintenance, and standardized infrastructure across projects.

Q4. What is the difference between count and for_each?

count uses numeric indexes and is best for identical resources. for_each uses unique keys, making it more stable and suitable for resources with distinct identities.

Q5. What is the purpose of a remote backend?

A remote backend centralizes the Terraform state, enables collaboration, supports state locking (for example, with DynamoDB on AWS), and helps prevent state corruption during concurrent operations.
