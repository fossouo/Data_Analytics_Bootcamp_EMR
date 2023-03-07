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

#### 2.1 Create EMR Cluster 

* Go to the EMR dashboard and click “Create cluster”. We recommend the following configuration
    * ClusterName: MySpark
    * Launch mode “Cluster”
    * Release: emr-6.9.0
    * Applications: Spark
    * Instance type: m4.xlarge
    * Number of Instances: 3
    * Key pair: course-key (or any other key you want to use, You can create the EC2 key pair using EC2 Service)
* Make sure to select EMR release emr-6.9.0

You can use this link for steps by steps guide in the creation : https://catalog.us-east-1.prod.workshops.aws/workshops/c86bd131-f6bf-4e8f-b798-58fd450d3c44/en-US/cluster-creation/cluster 

#### 2.1 Connect on Master Node using EC2 key pair 

You can copy the Master Node DNS name from EMR Service -> Cluster Name 
```
$ ssh -i ~/.ssh/course-key.pem hadoop@ec2-100-24-206-111.compute-1.amazonaws.com
```

#### 2.2 Launch Spark job on EMR Cluster 
##### 2.2.1 EMR Steps 
```
Admin:~/environment $ aws emr add-steps --cluster-id j-2VLSYP0B5G0RW --steps Type=Spark,Name="Spark Program",ActionOnFailure=CONT
INUE,Args=[--class,org.apache.spark.examples.SparkPi,/usr/lib/spark/examples/jars/spark-examples.jar,10]                         
{
    "StepIds": [
        "s-35569BKW4RMTS"
    ]
}
```
##### 2.2.2 Spark Submit 

* Upload input.txt and wordcount.py to master node using scp command (copy over ssh)
* Upload the input.txt file to HDFS 
```
$ hadoop fs -put input.txt
```
* Run spark-submit command : 
  
```
$ spark-submit wordcount.py 
$ spark-submit --num-executors 2 --executor-cores 4 wordcount.py 
```

You can use this link for steps by steps guide in execution of spark-submit : https://catalog.us-east-1.prod.workshops.aws/workshops/c86bd131-f6bf-4e8f-b798-58fd450d3c44/en-US/spark-etl/cli 

