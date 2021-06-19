# Challenge 1
#### Assumptions:
- User has access to AWS account and has permissions to create resources.
- User is aware of developing, using and running terraform scripts.
- user has installed and configured machine to run terraform scripts.
- The application is 3 tier and simple. Does not require any load-balancing, scaling and uses default vpc, subnets and security groups.
#### Language and Modules used:
- Terraform HCL.
- The following providers and resources are used in the script:
    - AWS, VPC, subnets, nat_gateways, security_groups, internet_gateway, db-instance, ec2-instance.
#### Inputs:
- The image name, region and instance type serve as the inputs for the modules. Details on each module can be found in the [official site](https://registry.terraform.io/providers/hashicorp/aws/latest).

#### Results : 
- To create an 3 tier infrastructure with presentation layer, application layer and db layer.

#### Design Details:
- The network is necessary to be able to connect to the instance services. Not going into the details and the infrastructure has been configured to use the default configuration provided by aws for configuring the network.
- The ec2 instances hosts the application and tomcat server. 
- The application connects to a mysql db server running in the same vpc.


