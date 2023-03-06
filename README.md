# Data_Analytics_Bootcamp_EMR
This repository contain steps to follow for deployment of MWAA based ETL on EMR Serverless and Spark on EMR 

### 1. EMR-Serverless Access Request, Create Bucket, Create Execution Role.

#### 1.1 Download mwaa_emr_serverless cloud formation template and deploy it in the Isengard Account you will use for the bootcamp. 

- Download the cloudformation template using this link : https://raw.githubusercontent.com/aws-samples/emr-serverless-samples/main/cloudformation/mwaa_emr_serverless.yaml 

#### 1.2 Get Output of the CloudFormation job : 

```
ApplicationArn	arn:aws:emr-serverless:eu-west-1:251746365760:/applications/00f89ajt2beo8v0p
ApplicationId	00f89ajt2beo8v0p
JobRoleArn	arn:aws:iam::251746365760:role/mwaa-cloudformation-EMRServerlessJobRole-1XTYXZWPVTSJ6
S3Bucket	mwaa-cloudformation-emrserverlessbucket-1iahcnuqk2oln
```

#### 1.3 The Cloudformation template will also create a VPC 

You can get the VPC name in Events section of CloudFormation Template).

#### 1.4 Create Cloud9 instance 

Using the VPC name issued of the deployment of CloudFormation. We will use Cloud9 instance for submitting dags to MWAA.  

```
aws s3 cp requirements.txt s3://mwaa-cloudformation-emrserverlessbucket-1iahcnuqk2oln/
aws s3 cp example_emr_serverless.py s3://mwaa-cloudformation-emrserverlessbucket-1iahcnuqk2oln/airflow/dags/
```

### 2. Spark on EMR 

#### 2.1 Connect on Master Node using SSM (https://aws.amazon.com/fr/blogs/big-data/securing-access-to-emr-clusters-using-aws-systems-manager/) 
#### 2.2 Launch Spark job on EMR Cluster 
##### 2.2.1 EMR Steps 
##### 2.2.2 Spark Submit 
