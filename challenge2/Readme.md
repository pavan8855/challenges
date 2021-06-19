# Challenge 2
#### Assumptions:
- User has access to cloud instances and configured to enable metadata read.
- User is aware of using cloud instances.
- user has installed and configured machine to run python scripts.
#### Language and Modules used:
- Python to script the logic for aws.
- NodeJS for GCP.
- The following modules are used in the script:
    - ec2_metadata: to read the ec2 instance metadata.
    - gcp-metadata : to read the gcp instance metadata
#### Inputs:
- The ec2_metadata module accepts most of the metadata keys. More information can be found on the [github page](https://github.com/adamchainz/ec2-metadata).
- The gcp_metadata provides library to be imported and used in the nodejs application. more information can be found on the [github page](https://github.com/googleapis/gcp-metadata).

#### Results : 
- To display the value of a key queried.

