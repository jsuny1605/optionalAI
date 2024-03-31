import time
import boto3

# Specify the region you want to use
region = 'us-east-1'

# Create an EC2 client with the specified region
ec2 = boto3.client('ec2', region_name=region)

response = ec2.run_instances(
    ImageId='ami-0fe630eb857a6ec83',
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    KeyName='macbook'
)
instance_id = response['Instances'][0]['InstanceId']
print("Successfully launch RHEL EC2 instance with Instance ID:  " + instance_id)
ec2.create_tags(
    Resources=[instance_id],
    Tags=[{'Key': 'Name', 'Value': 'RHEL-Linux-Machine'}]
)
time.sleep(60)
response = ec2.terminate_instances(InstanceIds=[instance_id])
state = response['TerminatingInstances'][0]['CurrentState']['Name']
print(f"Instance {instance_id} is now {state}")

