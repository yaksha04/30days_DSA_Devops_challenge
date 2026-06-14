What is NGINX?

NGINX is a high-performance:

Web Server
Reverse Proxy
Load Balancer
API Gateway
Caching Server

Originally created by Igor Sysoev to solve the C10K problem (handling 10,000+ simultaneous connections efficiently).

Today, NGINX is one of the most widely used web servers in the world and is commonly used by companies such as Netflix, Cloudflare, and Dropbox.

Why Do We Need NGINX?

Imagine you have a web application.

Without NGINX:

User
  ↓
Application Server

Problems:

Application handles all traffic
Slow performance
No load balancing
No caching
SSL termination burden

With NGINX:

User
  ↓
NGINX
  ↓
Application Server

Benefits:

✅ Faster response

✅ Better security

✅ Load balancing

✅ SSL handling

✅ Static file serving

✅ High availability

Main Uses of NGINX
1. Web Server

Serves:

HTML
CSS
JavaScript
Images
Videos

Example:

User → NGINX → index.html

Instead of your application serving files, NGINX serves them directly.

2. Reverse Proxy
Most Important Interview Topic

Forward Proxy:

Client → Proxy → Internet

Reverse Proxy:

Client → NGINX → Backend Servers

Users never directly access backend servers.

Example:

Internet
   ↓
NGINX
   ↓
Spring Boot App

Advantages:

Security
Load balancing
SSL termination
Hides backend IPs
3. Load Balancer

Suppose:

App Server 1
App Server 2
App Server 3

NGINX distributes traffic.

Users
  ↓
NGINX
 ├─ Server1
 ├─ Server2
 └─ Server3
Load Balancing Algorithms
Round Robin (Default)
Request1 → S1
Request2 → S2
Request3 → S3

Most common.

Least Connections
Send traffic to server
having lowest active connections.

Useful when requests have different durations.

IP Hash
Same client IP
always reaches same server.

Useful for sessions.

4. SSL/TLS Termination

Without NGINX:

User
 ↓ HTTPS
Application

Application handles encryption.

With NGINX:

User
 ↓ HTTPS
NGINX
 ↓ HTTP
Application

NGINX decrypts traffic.

Benefits:

Better performance
Centralized certificate management
5. Caching Server

Instead of generating same response repeatedly:

User
 ↓
NGINX Cache
 ↓
Backend

Frequently requested content is served from cache.

Benefits:

Faster response
Reduced backend load
6. API Gateway

For Microservices:

User
 ↓
NGINX
 ├─ User Service
 ├─ Payment Service
 └─ Order Service

Single entry point.

NGINX Architecture
Master Process

Responsible for:

Reading configuration
Managing worker processes
Reloading configuration
Master Process
Worker Processes

Handle:

Requests
Connections
Traffic
Master
 ├─ Worker1
 ├─ Worker2
 ├─ Worker3
 └─ Worker4

Workers do actual work.

Why NGINX Is Fast?

Traditional servers:

1 Thread = 1 Connection

10000 users

↓

10000 threads

↓

Huge memory usage

NGINX uses:

Event Driven Architecture

One worker handles thousands of connections.

Worker
 ├─ Conn1
 ├─ Conn2
 ├─ Conn3
 └─ Conn10000

This is the biggest reason behind NGINX performance.

Important NGINX Directives
worker_processes
worker_processes auto;

Automatically creates workers based on CPU cores.

worker_connections
worker_connections 1024;

Maximum connections per worker.

events Block
events {
    worker_connections 1024;
}

Connection settings.

http Block
http {
}

HTTP configuration.

server Block

Equivalent to virtual host.

server {
    listen 80;
}
location Block

URL matching.

location /api {
}

Handles requests to /api.

NGINX Configuration Structure
events {
}

http {

    server {

        listen 80;

        location / {
            root /var/www/html;
        }

    }
}

Interviewers often ask you to explain this hierarchy.

Reverse Proxy Configuration
server {

    listen 80;

    location / {

        proxy_pass http://localhost:8080;

    }

}

Flow:

User
 ↓
NGINX
 ↓
Spring Boot

Very common DevOps interview question.

Load Balancer Configuration
upstream backend {

    server 10.0.0.1;
    server 10.0.0.2;
    server 10.0.0.3;

}

server {

    location / {

        proxy_pass http://backend;

    }

}
Static Content Serving
location / {

    root /var/www/html;

    index index.html;

}

NGINX directly serves files.

NGINX Logs
Access Log

Records all requests.

Location:

/var/log/nginx/access.log

Example:

IP - GET /index.html 200
Error Log

Stores failures.

Location:

/var/log/nginx/error.log

Example:

502 Bad Gateway
Common Errors
404
Page Not Found
403
Permission Denied
500
Internal Server Error
502 Bad Gateway

Most asked in DevOps interviews.

Meaning:

NGINX
 ↓
Cannot reach backend

Possible causes:

Application down
Wrong port
Firewall issue
504 Gateway Timeout

Backend too slow.

NGINX in DevOps Projects
Docker
NGINX Container
 ↓
Application Container
Kubernetes

Used as:

Ingress Controller
Reverse Proxy
Load Balancer

Popular implementation: NGINX Ingress Controller

CI/CD

NGINX often serves deployed applications after Jenkins/GitHub Actions deployment.

Frequently Asked Interview Questions
1. What is NGINX?

A high-performance web server, reverse proxy, load balancer, and caching server.

2. Difference between Apache and NGINX?
Apache	NGINX
Thread/Process Based	Event Driven
More Memory	Less Memory
Good Dynamic Content	Excellent Static Content
Lower Concurrency	High Concurrency
3. What is Reverse Proxy?

A server that receives client requests and forwards them to backend servers while hiding backend details.

4. What is Load Balancing?

Distributing incoming traffic across multiple backend servers.

5. What is Upstream in NGINX?

Group of backend servers.

upstream backend {
 server 10.0.0.1;
 server 10.0.0.2;
}
6. What is SSL Termination?

NGINX handles HTTPS encryption/decryption before forwarding requests to backend applications.

7. Explain Master and Worker Processes.
Master process manages configuration and workers.
Worker processes handle requests and connections.
8. What is a 502 Bad Gateway error?

NGINX received an invalid response or no response from the backend server.

9. How do you test NGINX configuration?
nginx -t
10. How do you reload NGINX without downtime?
nginx -s reload

or

systemctl reload nginx
