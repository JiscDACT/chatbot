# ----------------------------------------------------------------
# setting up client to use
# after IAM user setup on AWS
# ----------------------------------------------------------------
# Instead of using Python and boto can use AWS CLI which I have downloaded and setup too but
# its just a command line sort of interface so ideally IDE need to be used I would think to save scripts etc
# is webstorm used for this sort of thing? Costs money but relatively cheap.

import boto3

#create key/secret for boto3 using IAM

import AWS_keys

#get AWS_KEY_ID and AWS_SECRET from another script so not uploaded to GitHub

# -------------------------------------------------------------------
# Task upload intent json

#This is to use s3 service

s3 = boto3.client('s3', region_name='us-east-1', #no idea what this region should be, this is north virginia so went with that
                        # Set up AWS credentials
                        aws_access_key_id=AWS_KEY_ID,
                         aws_secret_access_key=AWS_SECRET)

buckets = s3.list_buckets()

print(buckets)

# -------------------------------------------------------------------
# Create new bucket - alex_lex
# Note it doesnt use some symbols and capitals

alex_bucket = s3.create_bucket(Bucket='alex-lex')


# -------------------------------------------------------------------
# upload intent json

s3.upload_file(
Filename='jisc101.json',
Bucket='alex-lex',
Key='jisc101_20_07_2022.json'
)

# check its in

check = s3.list_objects(
    Bucket='alex-lex',
    MaxKeys=1,
    Prefix='jisc101'
)

print(check)
# -------------------------------------------------------------------


