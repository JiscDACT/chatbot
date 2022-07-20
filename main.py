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


#This is to use s3 service

s3 = boto3.client('s3', region_name='us-east-1', #no idea what this region should be, this is north virginia so went with that
                        # Set up AWS credentials
                        aws_access_key_id=AWS_KEY_ID,
                         aws_secret_access_key=AWS_SECRET)

buckets = s3.list_buckets()

print(buckets)

# -------------------------------------------------------------------
# To use dynamodb, use the below
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html
# Im using this guide


# Get the dynamodb resource.
dynamodb = boto3.resource('dynamodb', region_name='us-east-1',
                          # Set up AWS credentials
                          aws_access_key_id=AWS_KEY_ID,
                          aws_secret_access_key=AWS_SECRET)


# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='intents_utterances',
    KeySchema=[
        {
            'AttributeName': 'intent',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'utterances',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'intent',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'utterances',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

# Wait until the table exists.
table.wait_until_exists()

# Print out some data about the table.
print(table.item_count)

# add items

table.put_item(
   Item={
        'intent': 'JISC_101',
        'utterances': "where can I find out more about what jisc does"
    }
)