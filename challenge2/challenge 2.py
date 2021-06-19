# challenge 2

#the ec2_metadata provides the functionality to retrieve the instance metadata details from within the machine.
# query the object with the required metadata key to retrieve the data.

from ec2_metadata import ec2_metadata

print(ec2_metadata.region)
print(ec2_metadata.instance_id)

