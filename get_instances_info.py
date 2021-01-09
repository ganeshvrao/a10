import boto3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--r", help="AWS region containing instances", type=str, required=True)
parser.add_argument("--t", help="Instance type to be identified ", type=str, required=True)
args = parser.parse_args()
aws_region = args.r
instance_type = args.t

required_instances = []


def get_default_vpc(region):
    vpc_client = boto3.client('ec2', region_name=region)
    vpc_describe = vpc_client.describe_vpcs()
    vpc_list = vpc_describe['Vpcs']
    for vpc in vpc_list:
        if vpc['IsDefault']:
            return vpc['VpcId']


def get_instances_based_on_instance_type(region, default_vpc, instance_type):
    ec2_resource = boto3.resource('ec2', region_name=region)
    for instance in ec2_resource.instances.all():
        curr_instance_id = instance.id
        curr_vpc_id = instance.vpc_id
        curr_instance_type = instance.instance_type
        if curr_vpc_id == default_vpc and curr_instance_type == instance_type:
            global required_instances
            print(curr_instance_id)
            required_instances.append(curr_instance_id)


default_vpc = get_default_vpc(aws_region)
get_instances_based_on_instance_type(aws_region, default_vpc, instance_type)
print('The list of instances in region {0} of instance type {1}'.format(aws_region, instance_type))
print('\n'.join(map(str, required_instances)))

