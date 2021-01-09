#tophire
command to install the requirements
pip install -r requirements.txt


command to run the script
python2.7 get_instances_info.py --r us-east-2 --t m4.xlarge

options:

--r - region where instances are running
--t - the instance type required

the script gives the list of instances in the default VPC from the region specified
