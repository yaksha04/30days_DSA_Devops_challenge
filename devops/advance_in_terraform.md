1. Terraform Import (Managing Existing Infrastructure)

Normally, Terraform creates new resources.

But what if an AWS resource already exists?

Example:

EC2 Instance
↓

Created manually from AWS Console

Terraform doesn't know about it.

Use:

terraform import

Example

terraform import aws_instance.web i-0123456789abcdef0

This imports the EC2 instance into the Terraform state.

Important: terraform import does not generate your .tf code. It only updates the state file. You still need to write the corresponding resource block manually.

Workflow:

Existing Infrastructure

↓

terraform import

↓

Terraform State Updated

↓

Write .tf Configuration

↓

terraform plan

Interview Question

Why use terraform import?

To bring existing manually created infrastructure under Terraform management without recreating it.

2. Terraform Taint and Replace

Sometimes a resource becomes corrupted.

Example

EC2

↓

Configuration Broken

Instead of deleting it manually, Terraform can recreate it.

Older approach (deprecated)
terraform taint aws_instance.web

Then

terraform apply

Terraform destroys and recreates the resource.

Modern approach (recommended)
terraform apply -replace="aws_instance.web"

Benefits

More explicit
Doesn't permanently mark the state as tainted
Recommended in current Terraform versions

Example

Old EC2

↓

Destroy

↓

Create New EC2
3. Provisioners (Use Sparingly)

Provisioners execute commands after resource creation.

Example

resource "aws_instance" "web" {

  provisioner "remote-exec" {
    inline = [
      "sudo apt update",
      "sudo apt install nginx -y"
    ]
  }
}

Types

local-exec
remote-exec
file

Example uses

Copy files
Install packages
Run scripts
Why use sparingly?

Provisioners are not idempotent and can make deployments less reliable.

Better alternatives:

User Data
Cloud-init
Configuration management tools (e.g., Ansible)
Image baking (e.g., Packer)

Interview Tip

Provisioners should be the last resort, not the first choice.

4. Terraform Cloud and Sentinel Policies
Terraform Cloud

Terraform Cloud provides:

Remote state storage
State locking
Team collaboration
Version history
Remote execution
CI/CD integration

Example workflow

Developer

↓

Git Push

↓

Terraform Cloud

↓

Plan

↓

Approval

↓

Apply
Sentinel

Sentinel is a policy-as-code framework used with Terraform Cloud.

Example policies

Only approved AWS regions
No public S3 buckets
Only approved instance types
Mandatory resource tags

Example rule

EC2

↓

t2.micro

✓ Allowed
EC2

↓

m5.8xlarge

✗ Denied

Benefits

Governance
Compliance
Security guardrails
5. Terragrunt (DRY Infrastructure)

Terraform often leads to duplicated code.

Example

dev/

prod/

stage/

Each contains nearly identical Terraform code.

Terragrunt solves this using DRY (Don't Repeat Yourself).

Example

Common Configuration

↓

Terragrunt

↓

Dev

Prod

Stage

Advantages

Shared configuration
Less duplication
Easier maintenance
Built-in remote state configuration
Dependency management between modules

Example

include {
  path = find_in_parent_folders()
}
6. Dynamic Blocks and Expressions

Sometimes nested blocks repeat.

Instead of writing:

ingress { ... }

ingress { ... }

ingress { ... }

Use a dynamic block.

Example

dynamic "ingress" {
  for_each = var.ports

  content {
    from_port = ingress.value
    to_port   = ingress.value
  }
}

If

ports = [22,80,443]

Terraform automatically generates three ingress rules.

Common Expressions
Conditional Expression
instance_type = var.env == "prod" ? "t3.large" : "t2.micro"
For Expression
[for s in var.servers : s.name]

Produces

web

api

db
Splat Expression
aws_instance.web[*].id

Returns IDs of all matching instances.

Functions
length()

upper()

lower()

join()

split()

lookup()

merge()

contains()

format()

These simplify configuration and reduce repetition.

7. Terraform Graph Command

Terraform builds a dependency graph internally.

View it using

terraform graph

Example

VPC

↓

Subnet

↓

EC2

↓

ALB

Uses

Understand dependencies
Troubleshoot resource ordering
Visualize infrastructure

Often converted into diagrams with Graphviz.

8. State Manipulation Commands

The Terraform state tracks managed resources.

terraform state mv

Moves a resource inside the state.

Example

terraform state mv aws_instance.web aws_instance.frontend

Useful after renaming resources without recreating them.

terraform state rm

Removes a resource from the state without deleting it from the cloud provider.

Example

terraform state rm aws_instance.web

Result

Terraform

↓

Stops Managing Resource

↓

EC2 Still Exists

Useful before importing or handing management to another tool.

terraform state pull

Downloads the current remote state.

terraform state pull

Useful for:

Inspecting state
Debugging
Creating backups
terraform state push

Uploads a state file to the backend.

terraform state push terraform.tfstate

Use this carefully, as it can overwrite the remote state.

Interview Questions
1. What does terraform import do?

It imports an existing infrastructure resource into the Terraform state so Terraform can manage it. It does not generate the corresponding .tf configuration.

2. What replaced terraform taint?

The recommended approach is:

terraform apply -replace="RESOURCE_ADDRESS"

It explicitly recreates a resource during the apply operation.

3. Why are provisioners discouraged?

Because they are not reliably idempotent, can fail unpredictably, and mix infrastructure provisioning with configuration management. User data, cloud-init, Ansible, or prebuilt images are generally better choices.

4. What is Terragrunt?

Terragrunt is a wrapper around Terraform that reduces code duplication, simplifies remote state configuration, and helps manage multiple environments and module dependencies.

5. What is Sentinel?

Sentinel is a policy-as-code framework used with Terraform Cloud to enforce organizational rules, such as restricting regions, requiring tags, or preventing insecure resources.

6. What is the purpose of terraform graph?

It visualizes Terraform's dependency graph, helping you understand resource relationships and troubleshoot dependency issues.

7. What is the difference between terraform state rm and deleting a resource?
terraform state rm removes the resource only from Terraform's state; the actual cloud resource remains intact.
Deleting a resource via terraform destroy or terraform apply removes both the state entry and the real infrastructure.
