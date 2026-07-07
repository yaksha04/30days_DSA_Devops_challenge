1. Template Structure

A CloudFormation template is written in YAML or JSON.

AWSTemplateFormatVersion: '2010-09-09'
Description: Sample EC2

Parameters:
Mappings:
Conditions:
Resources:
Outputs:
Parameters

Parameters make templates reusable.

Instead of hardcoding values, users provide them during deployment.

Example

Parameters:
  InstanceType:
    Type: String
    Default: t2.micro

During stack creation

InstanceType = t3.small

CloudFormation substitutes the value automatically.

Common parameter types

String
Number
CommaDelimitedList
AWS::EC2::KeyPair::KeyName
AWS::EC2::Subnet::Id
Mappings

Mappings store fixed lookup values.

Example

Mappings:
  RegionMap:
    us-east-1:
      AMI: ami-12345
    ap-south-1:
      AMI: ami-67890

Use

ImageId:
  Fn::FindInMap:
    - RegionMap
    - !Ref AWS::Region
    - AMI

Useful for

Region-specific AMIs
Environment settings
Instance sizes
Resources

The heart of every template.

Every AWS service is created here.

Example

Resources:
  MyBucket:
    Type: AWS::S3::Bucket

  MyEC2:
    Type: AWS::EC2::Instance

CloudFormation creates these resources automatically.

Outputs

Expose useful information after deployment.

Example

Outputs:
  BucketName:
    Value: !Ref MyBucket

Can display

Bucket names
Instance IDs
Public IPs
Load Balancer DNS

Outputs are also used for cross-stack references.

2. Stacks and StackSets
Stack

A Stack = one deployed CloudFormation template.

Example

network-stack

Creates:
VPC
Subnets
Route Tables

Another stack

app-stack

Creates:
EC2
ALB
Security Groups

Each template deployment becomes a separate stack.

StackSets

Deploy the same stack to

Multiple AWS accounts
Multiple AWS regions

Example

Deploy IAM roles to

50 AWS accounts

with one operation.

Very common in enterprise organizations.

3. Change Sets

A Change Set previews changes before deployment.

Without Change Set

Update Stack

↓

CloudFormation immediately updates

With Change Set

Update Template

↓

Preview

↓

Accept

↓

Deploy

Example preview

Modify EC2

Replace RDS

Create S3 bucket

Benefits

Prevent accidental deletion
Review updates
Safer production deployments
4. Drift Detection

Sometimes someone manually changes AWS resources.

Example

CloudFormation says

EC2 = t2.micro

Someone changes manually

EC2 = t3.medium

Now

CloudFormation

≠

Actual Infrastructure

This is called configuration drift.

Drift Detection checks whether resources still match the template.

Possible results

IN_SYNC

DRIFTED

NOT_CHECKED

Important interview point:

Infrastructure should ideally be managed only through Infrastructure as Code, not manually.

5. CloudFormation vs Terraform
Feature	CloudFormation	Terraform
Vendor	AWS	HashiCorp
Cloud support	AWS only	AWS, Azure, GCP, Kubernetes, GitHub, etc.
Language	YAML/JSON	HCL
State	AWS manages stack state	terraform.tfstate
Multi-cloud	No	Yes
Third-party providers	Limited	Thousands
Learning curve	Easier for AWS	Slightly harder
Best for	AWS-only environments	Multi-cloud environments
Interview answer

Use CloudFormation when:

Company only uses AWS
Deep AWS integration
Native AWS support

Use Terraform when:

Multi-cloud
Hybrid cloud
Large enterprise environments
6. AWS CDK Basics

CDK = Cloud Development Kit

Instead of YAML

You write infrastructure using programming languages.

Supported languages

Python
Java
TypeScript
Java
C#

Example

bucket = s3.Bucket(self, "MyBucket")

CDK automatically generates CloudFormation templates.

Flow

Python Code

↓

CDK

↓

CloudFormation Template

↓

AWS Resources

Advantages

Loops
Functions
Classes
Reusable code
IDE autocomplete
Easier maintenance
7. Resource Dependencies

CloudFormation automatically detects dependencies.

Example

Resources:

  MyBucket:
    Type: AWS::S3::Bucket

  BucketPolicy:
    Type: AWS::S3::BucketPolicy
    Properties:
      Bucket: !Ref MyBucket

Because of

!Ref MyBucket

CloudFormation knows

Bucket

↓

Bucket Policy

No manual ordering needed.

8. DependsOn

Sometimes CloudFormation cannot infer dependencies.

Use

DependsOn

Example

Resources:

  InternetGateway:
    Type: AWS::EC2::InternetGateway

  AttachGateway:
    Type: AWS::EC2::VPCGatewayAttachment

  Route:
    Type: AWS::EC2::Route
    DependsOn: AttachGateway

Order

Create Internet Gateway

↓

Attach to VPC

↓

Create Route

Without DependsOn, CloudFormation may attempt to create the route before the gateway is attached, causing the deployment to fail.

9. Cross-Stack References

Large infrastructures are often split into multiple stacks.

Example

Stack A

VPC
Subnets

↓

Export Outputs

↓

Stack B

EC2
ALB
RDS
Stack A
Outputs:
  VPCID:
    Value: !Ref MyVPC
    Export:
      Name: MyVPC
Stack B
VpcId:
  Fn::ImportValue: MyVPC

Benefits

Modular infrastructure
Reusable network stack
Easier maintenance
Teams can manage separate stacks independently
Interview Questions

Q1. What is a Stack?
A stack is a deployed CloudFormation template that manages a collection of AWS resources as a single unit.

Q2. What is a Change Set?
It previews the changes CloudFormation will make before updating a stack, allowing you to review modifications safely.

Q3. What is Drift Detection?
It identifies whether the actual AWS resources have diverged from the CloudFormation template due to manual changes.

Q4. When would you use DependsOn?
When CloudFormation cannot automatically determine the correct creation order between resources.

Q5. CloudFormation or Terraform—which is better?
Neither is universally better. CloudFormation is a strong choice for AWS-only environments with native integration, while Terraform is preferred for multi-cloud or hybrid infrastructure because it supports many providers.

Q6. What does AWS CDK do?
It lets you define infrastructure using familiar programming languages and synthesizes that code into CloudFormation templates for deployment.
