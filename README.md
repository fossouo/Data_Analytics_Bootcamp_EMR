# Data_Analytics_Bootcamp_EMR
This repository contain steps to follow for deployment of MWAA based ETL on EMR Serverless and Spark on EMR 

### EMR-Serverless Access Request, Create Bucket, Create Execution Role.

#### Download mwaa_emr_serverless cloud formation template and deploy it in the Isengard Account you will use for the bootcamp. 

- Download the cloudformation template using this link : https://raw.githubusercontent.com/aws-samples/emr-serverless-samples/main/cloudformation/mwaa_emr_serverless.yaml 

#### Get Output of the CloudFormation job : 

```
ApplicationArn	arn:aws:emr-serverless:eu-west-1:251746365760:/applications/00f89ajt2beo8v0p
ApplicationId	00f89ajt2beo8v0p
JobRoleArn	arn:aws:iam::251746365760:role/mwaa-cloudformation-EMRServerlessJobRole-1XTYXZWPVTSJ6
S3Bucket	mwaa-cloudformation-emrserverlessbucket-1iahcnuqk2oln
```

#### The Cloudformation template will also create a VPC 

You can get the VPC name in Events section of CloudFormation Template).

#### Create Cloud9 instance 

Using the VPC name issued of the deployment of CloudFormation. We will use Cloud9 instance for submitting dags to MWAA.  
