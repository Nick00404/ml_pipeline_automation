#!/bin/bash
# Deploy project to an AWS EC2 instance using SSH and Docker Compose
ssh -i your-key.pem ec2-user@your-ec2-instance 'docker-compose -f /path/to/docker-compose.yml up -d'
