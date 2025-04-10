#!/bin/bash

# Update and install basic tools
sudo yum update -y
sudo yum install -y unzip curl wget git

# Install AWS CLI v2
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
rm -rf aws awscliv2.zip

# Confirm AWS CLI installed
aws --version

# Install SSM Agent (Amazon Linux/RHEL-based)
sudo yum install -y amazon-ssm-agent
sudo systemctl enable amazon-ssm-agent
sudo systemctl start amazon-ssm-agent

# Confirm SSM Agent status
sudo systemctl status amazon-ssm-agent

# Optional: Install CloudWatch Agent
sudo yum install -y amazon-cloudwatch-agent

echo " Setup complete: AWS CLI, SSM Agent, and basic tools are ready."
