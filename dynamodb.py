import os
import json
user = os.getlogin()
os.chdir("C:\\Users\\" + user + '\\OneDrive - Jisc\\GitHub\\chatbot')

# after IAM user setup on AWS
import boto3
#create key/secret for boto3 using IAM

from AWS_keys import *
#get AWS_KEY_ID and AWS_SECRET from another script so not uploaded to GitHub
#Ideally needs to be put in as environment variable
# -------------------------------------------------------------------

# To use dynamodb, use the below
# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/dynamodb.html
# Im using this guide


# Update DynamoDB table using JSON already created
json_file_path = os.path.join("C:\\Users\\" + user + '\\OneDrive - Jisc\\GitHub\\chatbot\\intents_utterances.json')
f = open(json_file_path)
json_obj = json.loads(f.read())


# Get the dynamodb resource.
dynamodb = boto3.resource('dynamodb', region_name='eu-west-2', #This is Europe (London)
                          # Set up AWS credentials
                          aws_access_key_id=AWS_KEY_ID,
                          aws_secret_access_key=AWS_SECRET)


# Create the DynamoDB table.
try:
    table = dynamodb.create_table(
    TableName='intents_utterances2',
    KeySchema=[
        {
            'AttributeName': 'name',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'identifier',
            'KeyType': 'RANGE'
        }  
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'name',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'identifier',
            'AttributeType': 'S'
        }     
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
    )
except:
   print('table already exists')
   pass   

# Wait until the table exists.
table.wait_until_exists()

# Print out some data about the table.
print(table.item_count)


# manually add and item to the table  
if (len(dynamodb.Table('intents_utterances2').get_item(Key={'name':'JISC_101', 'identifier':'F2VCNJR01B'})) > 1):
    print('Item already exists in table')
else :
    table.put_item(   
        Item={
            "name":"JISC_101",
            "identifier":"F2VCNJR01B",
            "description":"Helps staff find out more about Jisc's products and services",
            "parentIntentSignature":None,
            "sampleUtterances":[{"utterance":"what does jisc do"},{"utterance":"where can I find out more about what jisc does"},{"utterance":"what products and services does jisc offer"},{"utterance":"where is the jisc 101 page"}],"intentConfirmationSetting":None,"intentClosingSetting":None,"inputContexts":None,"outputContexts":None,"kendraConfiguration":None,"dialogCodeHook":None,
            "fulfillmentCodeHook":{"fulfillmentUpdatesSpecification":None,"postFulfillmentStatusSpecification":{"failureResponse":None,"timeoutResponse":None,"successResponse":{"allowInterrupt":True,"messageGroupsList":[{"message":{"imageResponseCard":None,"ssmlMessage":None,"customPayload":None,"plainTextMessage":{"value":"To find out more about what Jisc do including how and why please see this link which is the Jisc 101 page  - https://jisc365.sharepoint.com/sites/intranet/SitePages/Explaining-Jisc.aspx?etag=%22%7B48EABC0C-CAC8-470A-BE47-4B4BEF934FF8%7D%2C222%22&OR=Teams-HL&CT=1654526897397&params=eyJBcHBOYW1lIjoiVGVhbXMtRGVza3RvcCIsIkFwcFZlcnNpb24iOiIyNy8yMjA1MDEwMTAwOSJ9"}},"variations": None}]}},"enabled":False},
            "slotPriorities":[]
        }
    )

# loop over dict keys which are each eleement that needs added to the table
loop = json_obj.keys()
for i in range(len(json_obj.keys())):
    item = list(json_obj.keys())[i]
    if (len(dynamodb.Table('intents_utterances2').get_item(Key={'name':item,'identifier':json_obj[item]['identifier']})) > 1):
        print('item already exists in the table')
    else:
        print('adding item:', item,' to the table')
        res = dynamodb.Table('intents_utterances2').put_item(Item = json_obj[item])
        if res["ResponseMetadata"]["HTTPStatusCode"] == 200 :
            print('Success')
        else:
            print('Fail')

# -------------------------------------------------------------------