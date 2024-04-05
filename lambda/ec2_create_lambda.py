import boto3

ec2_client = boto3.client('ec2', region_name='ap-south-1')
def lambda_handler(event, context):
    response = ec2_client.run_instances(
       BlockDeviceMappings=[
       {
        'DeviceName': '/dev/xvda',
        'Ebs': {
             'DeleteOnTermination': True,
             'VolumeSize': 8,
             'VolumeType': 'gp3',
             'Encrypted': False,
             'Iops': 3000,
           },
         },
       ],
       ImageId='ami-09298640a92b2d12c',
       InstanceType = 't2.micro',
       MaxCount=1,
       MinCount=1,
       KeyName='tfuser',
       UserData= '''#!/bin/bash
sudo yum update -y
sudo yum install httpd -y
sudo echo "<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>DevOps Learning</title>

</head>

    <header>
        <div class="header-content">
            <div class="header-content-inner">
			<body bgcolor="yellow">
                <h1>Learn Cloud/DevOps with Automation Tools:</h1>
                <hr>
                <p><b> We are moving towards Cloud Computing and DevOps with Automation. There are a variety of tools available on the market. Here are the tools that are easy to learn!</b> </p>
				<p><b> Cloud Technology</b> - AWS/Azure</p>
				<p><b> Source Code Management Systems</b> - GitHub Enterprise, BitBucket </p>
				<p><b> Continuous Integration and Continuous Deployment/Delivery</b> - ArgoCD, Jenkins, GitOps </p>
				<p><b> Software Configuration Management Tool</b> - Ansible </p>
				<p><b> Operating Systems</b> - RHEL 7/8, CentOS, Ubuntu/Debian, Windows </p>
				<p><b> Containerization/Orchestration</b> - Docker, Kubernetes </p>
				<p><b> Monitoring Tools</b> - AppDynamics, DataDog, New Relic, Zabbix </p>
            </div>
        </div
    </header>
	<footer>
	<p>style="color:black;">© Copyright Cloudbird.fun 2023</p>
</footer>
</body>
</html>" > /var/www/html/index.html 
sudo systemctl start httpd
sudo systemctl enable httpd''',
       Monitoring={
            'Enabled': False
       },
       SecurityGroupIds=[
          'sg-0fb1052b659369aa8',
       ],
       SubnetId='subnet-e9190a81',
       TagSpecification=[
        {
    'Tags': [
                {
                    'Name': 'LAMBDA-EC2',
                    'Owner': 'thangadurai.murugan@example.com',
                    'Environment': 'Development',
                    'CostCentre': '10004532',
                },
            ],
        },
       ],
)
