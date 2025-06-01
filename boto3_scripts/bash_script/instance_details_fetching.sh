#!/bin/bash

read -p "Enter the instance ID, please: " INSID
echo "You've entered instance ID is: $INSID"
Private_ip=$(aws ec2 describe-instances --instance-ids "$INSID" --query 'Reservations[*].Instances[*].PrivateIpAddress')
Public_ip=$(aws ec2 describe-instances --instance-ids "$INSID" --query 'Reservations[*].Instances[*].PublicIpAddress')
SecurityGroup=$(aws ec2 describe-instances --instance-ids "$INSID" --query 'Reservations[*].Instances[*].SecurityGroups[*].GroupName')

## Outputs
echo "Instance Public IP is: $Public_ip"
echo "Instance Private IP is: $Private_ip"
echo "Instance Security Group is: $SecurityGroup"

