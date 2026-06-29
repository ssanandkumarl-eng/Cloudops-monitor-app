## CloudOps Monitoring Platform – DevOps CI/CD Project

# 📌 Project Overview

The CloudOps Monitoring Platform is a Dockerized Python Flask-based monitoring solution designed to monitor multiple Linux servers and AWS infrastructure from a centralized dashboard.

The platform consists of three independent services:

- CloudOps Agent
- CloudOps Dashboard
- CloudOps AWS Monitor

The application collects real-time system metrics from Linux servers and displays them through a centralized web interface. The entire deployment process is automated using Docker, Docker Compose, Jenkins CI/CD, GitHub, and AWS EC2.

## 🎯 Project Objectives

- Build a centralized monitoring platform using Python Flask
  Collect server metrics using Monitoring Agents
- Monitor AWS infrastructure
- Containerize all services using Docker
- Orchestrate multi-container deployment using Docker Compose
- Store source code in GitHub
- Automate deployment using Jenkins Freestyle Jobs
- Implement GitHub Webhook Integration
- Deploy on AWS EC2
- Demonstrate a complete DevOps CI/CD workflow

## 🛠️ Technologies Used

Programming & Web

- Linux
- Python Flask
- HTML
- CSS
- JSON
- Git
- GitHub
- Docker
- Jenkins
- AWS EC2
- Elastic IP

## Operating System
~ Ubuntu Linux

## 🏗️ Architecture Diagram

![Architecture](.github/Architecture%20Diagram.png)
## Install Dependencies

```bash
cd cloudops-dashboard

pip install -r requirements.txt
```
## Run Application Locally
```bash
# Agent

cd cloudops-agent

python agent.py

Open

http://localhost:5000/metrics

# Dashboard

cd cloudops-dashboard

python app.py

Open

http://localhost:8000

# AWS monitor

cd cloudops-aws-monitor

python aws_monitor.py

Open

http://localhost:9000
```

## 🐳 Docker Implementation

# Build Docker Image

```bash
## Agent
docker build -t cloudops-agent ./cloudops-agent
## Dashboard
docker build -t cloudops-dashboard ./cloudops-dashboard
## AWS Monitor
docker build -t cloudops-aws-monitor ./cloudops-aws-monitor
```
## Run with Docker Compose

```bash
docker compose up -d
```

## Verify containers

```bash
docker ps
```
## stop services

```bash
docker compose down
```

## ☁️ AWS Deployment

1. EC2 Configuration
2. Ubuntu Server
3. Elastic IP
4. Security Groups Configured
5. Open Ports
6. Service	Port
7. SSH	22
8. Jenkins	8080
9. Dashboard 8000
10. Agent 5000
11. AWS server 9000


## Docker install
```bash
sudo apt update

sudo apt install docker.io -y

sudo systemctl enable docker

sudo systemctl start docker
```
## Docker compose install

```bash
docker compose version

```
## Install Jenkins

```bash
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee \
/usr/share/keyrings/jenkins-keyring.asc > /dev/null

echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
/etc/apt/sources.list.d/jenkins.list > /dev/null

sudo apt update

sudo apt install jenkins -y
```

### Start Services

```bash
sudo systemctl enable docker
sudo systemctl start docker

sudo systemctl enable jenkins
sudo systemctl start jenkins
```

---

## Configure Jenkins Freestyle Job

### Source Code Management

Repository URL:

```text
https://github.com/ssanandkumarl-eng/Cloudops-monitor-app.git
```

## ⚙️ Jenkins Build Script

echo "Starting Build"

docker stop monitoring-app || true

docker rm monitoring-app || true

docker rmi monitoring-app || true

docker build -t monitoring-app .

docker run -d \
 --restart unless-stopped \
 --name monitoring-app \
 -p 5000:5000 \ 
 monitoring-app

## Configure GitHub Webhook

Webhook URL

```text
http://<EC2-PUBLIC-IP>:8080/github-webhook/
```

Content Type:

```text
application/json
```

Event:

```text
Just the push event
```

## 🔄 CI/CD Workflow

1. Developer modifies source code.
2. Changes are pushed to GitHub.
3. GitHub Webhook triggers Jenkins.
4. Jenkins pulls latest code.
5. Docker image is rebuilt.
6. Existing container is removed.
7. New container is deployed automatically.
8. CloudOps becomes available automatically.
9. Dashboard starts collecting live metrics from agents.

## Project screenshots

## AWS
![EC2-1](.github/AWS%20ec2.png)
## JENKINS
![Jenkins Dashboard](.github/)
![Build success](.github)
## DOCKER
![Docker container](.github)
## GITHUB
![Github Repo](.github)
## AWS server
![AWS Server Dashboard](.github)
## Cloudops Monitor
![Monitor](.github)
## 🔍 Challenges Faced & Resolutions

# Jenkins Node Offline Due to Disk Space

## Issue

Built-In Node offline due to temporary disk space monitoring.

## Resolution

Reviewed Jenkins node monitoring settings

Verified root volume space

Brought node back online

Continued deployment successfully



# Docker Permission Denied

## Issue

Permission denied while trying to connect to the Docker daemon socket

## Resolution

sudo usermod -aG docker jenkins
sudo systemctl restart jenkins

## Docker Compose Not Found

# Issue

Jenkins build failed because Docker Compose plugin was missing.

# Resolution

Installed latest Docker Compose plugin.


## 🚀 Features

> Real-time Monitoring platform
> Dockerized Deployment
> Automated CI/CD Pipeline
> GitHub Webhook Integration
> AWS Cloud Deployment
> Jenkins Automation
> Auto-Restarting Containers
> Version Controlled Source Code

## Project Outcome

✅ Multi-Container Monitoring Platform

✅ Dockerized application

✅ Automated Jenkins Deployment

✅ GitHub to Jenkins integration

✅ Centralized Monitoring Dashboard

✅ AWS EC2 hosting
   
✅ AWS Infrastructure Monitoring

## 👨‍💻 Author

ANANDKUMAR 

DevOps Engineer Aspirant 

GitHub: https://github.com/ssanandkumarl-eng/linux-monitoring-dashboard 

LinkedIn: 