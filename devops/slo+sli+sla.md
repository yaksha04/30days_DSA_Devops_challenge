1. SLA — Service Level Agreement

An SLA is a formal business promise made to customers about service quality.

It is usually a legal or contractual agreement.

Example:

“Our service will maintain 99.9% uptime monthly.”

If the company fails:

customer may get compensation
credits/refunds may happen
trust damage occurs
Example of SLA

Suppose a cloud company says:

99.95% uptime guaranteed
support response within 1 hour
backup retention for 30 days

This becomes an SLA.

Important Point

SLA is customer-facing.

It is not mainly for engineers.
It is for:

clients
customers
enterprises
contracts
Common SLA Metrics
Metric	Meaning
Availability	uptime guarantee
Response time	API/service speed
Support response	ticket handling time
Recovery time	outage restoration
Example

If a company offers:

99.9% uptime

That means maximum downtime allowed is approximately:

30 days×24 hours/day×(1−0.999)≈0.72 hours

≈ 43 minutes/month downtime.

2. SLO — Service Level Objective

An SLO is an internal engineering target.

It defines the performance goal engineers try to maintain.

Example:

95% API requests should respond within 200ms
error rate should stay below 1%
uptime target = 99.95%
Important Difference

SLO is:

engineering-focused
operational target
internal

SLA is:

business/legal promise
external/customer-facing
Relationship Between SLA and SLO

Usually:

SLO is stricter than SLA.

Example:

Type	Value
SLA	99.9% uptime
SLO	99.95% uptime

Reason:
Engineering keeps buffer space to avoid violating SLA.

3. Alert (Often called SLI-based Alerting)

Alerts are notifications triggered when systems behave badly.

Examples:

CPU too high
API latency too high
pod crash
disk full
error rate spike
What is SLI?

Before alerts, understand SLI.

SLI — Service Level Indicator

An SLI is the actual measured metric.

Examples:

request latency
uptime %
error rate
throughput
Full Flow

SLI → measured metric
SLO → target for metric
SLA → customer promise

Real Example

Suppose you run an e-commerce API.

SLI

Actual measured latency:

180ms average
SLO

Goal:

95% requests under 200ms
SLA

Customer promise:

99.9% availability
Alert

Trigger if:

latency > 500ms
error rate > 5%
uptime dropping
Easy Analogy

Imagine a delivery company.

Concept	Meaning
SLA	“We promise delivery in 2 days.”
SLO	Internal goal: “Deliver within 1 day.”
SLI	Actual measured delivery time
Alert	“Truck breakdown detected.”
Why SLOs Matter in Real Engineering

Without SLOs:

teams optimize random things
no clear reliability target
alerts become noisy
burnout increases

Good SLOs help:

prioritize incidents
reduce alert fatigue
improve reliability
balance speed vs stability
Error Budget (Very Important)

Error budget is deeply connected with SLOs.

Formula:

Error Budget=100%−SLO

Example:

SLO = 99.9%

Allowed failure:

100%−99.9%=0.1%

Meaning:
System can fail for 0.1% time safely.

If budget exceeds:

deployments may stop
reliability work prioritized

Google SRE teams use this heavily.

Alert Types
1. Threshold Alerts

Simple rule-based.

Example:

CPU > 90%
2. Anomaly Alerts

Detect unusual patterns.

Example:

sudden traffic spike

Often ML-based.

3. SLO-Based Alerts

Modern SRE approach.

Alert only when user experience suffers.

Example:

p95 latency exceeds SLO for 10 mins

Much better than noisy CPU alerts.

Popular Monitoring & Alerting Stack
Monitoring
Prometheus
Grafana
Datadog
Alerting
Alertmanager
PagerDuty
Opsgenie
Example Architecture

Application → Metrics → Prometheus → Alertmanager → Slack/PagerDuty

Interview-Level Understanding

Very commonly asked in:

DevOps
SRE
Platform Engineering
Observability
Cloud roles

Typical questions:

Difference between SLA and SLO?
What is an SLI?
Why are SLO-based alerts better?
What is error budget?
How would you reduce alert fatigue?
One-Line Summary
Term	Meaning
SLI	What you measure
SLO	What engineers target
SLA	What business promises
Alert	Warning when system degrades
