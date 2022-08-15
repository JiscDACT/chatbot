# Build, deploy, and manage bots using boto3
# Collect the following info
# Your bot ID
# Your alias ID
# Your locale ID (language code)
# -----------------------------------------------------------------------------------------------------------------------
# Runtime API
# -----------------------------------------------------------------------------------------------------------------------

import uuid

# str(uuid.uuid4())
# uuid.uuid4().hex
# Just creating unique ID number for session ID, pretty sure it can be anything but used this anyway

# Setup
botId = 'MYCSXHKEKY'
botAliasId = 'GVOI7JIYSF'
localeId = 'en_GB'
sessionId = uuid.uuid4().hex
from AWS_keys import *

import boto3

# LexV2 client uses 'lexv2-runtime'
client = boto3.client('lexv2-runtime', region_name='eu-west-2',
                      aws_access_key_id=AWS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET)

print(client)
# https://aws.amazon.com/blogs/machine-learning/interact-with-an-amazon-lex2v2-bot-with-the-aws-cli-aws-sdk-for-python-and-aws-sdk-dotnet/
# Interacting with your bot

# Submit text

response = client.recognize_text(
    botId=botId,
    botAliasId=botAliasId,
    localeId=localeId,
    sessionId=sessionId,
    text='I need help with Python')

import json

print(json.dumps(response, indent=4, sort_keys=True))

# -----------------------------------------------------------------------------------------------------------------------
# Resources:
# https://aws.amazon.com/blogs/machine-learning/interact-with-an-amazon-lex2v2-bot-with-the-aws-cli-aws-sdk-for-python-and-aws-sdk-dotnet/
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-runtime.html
# -----------------------------------------------------------------------------------------------------------------------
# Model Building Service API
# -----------------------------------------------------------------------------------------------------------------------
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lexv2-models.html
# -----------------------------------------------------------------------------------------------------------------------
# Firstly create the bot
# -----------------------------------------------------------------------------------------------------------------------
# Only need to create the bot once

client = boto3.client('lexv2-models', region_name='eu-west-2',
                      aws_access_key_id=AWS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET)

created_bot_response = client.create_bot(
    botName='programmatic_alex',
    description='new starter bot',
    roleArn='arn:aws:iam::240624597515:role/aws-service-role/lexv2.amazonaws.com/AWSServiceRoleForLexV2Bots_RUVXLDJJZK',
    dataPrivacy={
        'childDirected': False
    },
    idleSessionTTLInSeconds=300  # seconds so 5 mins
)

# Amazon Resource Names (ARNs) uniquely identify AWS resources
# https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html
# ARN you can construct manually but I just got it from webinterface by clicking around!

print(response)
# -----------------------------------------------------------------------------------------------------------------------
# Create a bot Locale
# -----------------------------------------------------------------------------------------------------------------------
# botid of the new bot : KA6ARFQ5CT
# Only need to create a Bot locale once

response = client.create_bot_locale(
    # botId=created_bot_response['botId'],
    botId='KA6ARFQ5CT',
    botVersion='DRAFT',
    localeId='en_GB',
    description='Bot locale',
    nluIntentConfidenceThreshold=0.8
)
print(response)

# -----------------------------------------------------------------------------------------------------------------------

# Create intent
# The brackets in this are quite frankly a headache - can use a json editor but doesnt massively help tbh

response = client.create_intent(
    intentName='PYTHON_SETUP',
    description='Helps users find out how to setup Python',
    sampleUtterances=[
        {
            'utterance': 'I cant setup PyCharm'
        },
        {
            'utterance': 'I cant setup Python'
        },
        {
            'utterance': 'where can I get help setting up Python'
        },
        {
            'utterance': 'where can I get help using Python'
        },
    ],
    dialogCodeHook={
        'enabled': False
    },
    fulfillmentCodeHook={
        'enabled': False,
        'postFulfillmentStatusSpecification': {
            'successResponse': {
                'messageGroups': [
                    {
                        'message': {
                            'plainTextMessage': {
                                'value': 'DACT have Sharepoint pages to offer help and advice'
                            }
                        }
                    }
                ]
            }
        }
    },

    #botId=created_bot_response['botId'],
    botId='KA6ARFQ5CT',
    botVersion='DRAFT',
    localeId='en_GB'

)

print(response)
# -----------------------------------------------------------------------------------------------------------------------
# Write a function that can add a load of intents at once, skip ones that are already on there but add new ones
# this is what we want to update each time

import pandas as pd

df = pd.read_csv("intents_long.csv")


# Here is a function that could work for it

def create_intent_jen(intentname,
                      desc,
                      utterances,
                      fulfillment):
    response = client.create_intent(
        intentName=intentname,
        description=desc,
        sampleUtterances=utterances,
        dialogCodeHook={
            'enabled': False
        },
        fulfillmentCodeHook={
            'enabled': False,
            'postFulfillmentStatusSpecification': {
                'successResponse': {
                    'messageGroups': [
                        {
                            'message': {
                                'plainTextMessage': {
                                    'value': fulfillment
                                }
                            }
                        }
                    ]
                }
            }
        },

        #botId=created_bot_response['botId'],
        botId='KA6ARFQ5CT',
        botVersion='DRAFT',
        localeId='en_GB'

    )
    return response



# Adding Intents and utterances from the dataset
# Attempt for long format data


for i in df['intentname'].unique():
    # Get the data in the right format for the create_intent function which is fussy
    utterances = df[df['intentname'] == i]['utterances'].tolist()
    utterance_list = []

    for j in utterances:
        thisdict = {"utterance": j}
        utterance_list.append(thisdict)

    intentname = df[df['intentname'] == i]['intentname'].reset_index(drop=True)[0]
    desc = df[df['intentname'] == i]['desc'].reset_index(drop=True)[0]
    fulfillment = df[df['intentname'] == i]['fulfillment'].reset_index(drop=True)[0]

    response = create_intent_jen(intentname=intentname,
                                 desc=desc,
                                 utterances=utterance_list,
                                 fulfillment=fulfillment)

    if response['ResponseMetadata']['HTTPStatusCode'] != 200:
        print("Intent Creation failed!!!\n", response)
        break

# -----------------------------------------------------------------------------------------------------------------------
# Check it has done it

# Describe the Lex Bot
client.describe_bot(
    botId='KA6ARFQ5CT'
)

# -----------------------------------------------------------------------------------------------------------------------
# Create a version? Just using DRAFT for now

# You can get the botID out of the previous response

response = client.create_bot_version(
    botId=created_bot_response['botId'],
    description='trying out version',
    botVersionLocaleSpecification={
        'DRAFT': {
            'sourceBotVersion': 'version 1'
        }
    }
)

print(response['botId'])

# -----------------------------------------------------------------------------------------------------------------------
# Create an alias


# Resources
# https://towardsaws.com/getting-started-with-aws-lex-using-a-datafile-and-aws-python-sdk-64517fd751b7

# -----------------------------------------------------------------------------------------------------------------------
# End

























# Working



utterances = df[df['intentname'] == "Agile"]['utterances'].tolist()
utterance_list = []

for j in utterances:
        thisdict = {"utterance": j}
        utterance_list.append(thisdict)







# Adding Intents and utterances from the dataset
# Attempt for wide format data

for idx, row in df.iterrows():
    response = create_intent(intentname=row['intentname'],
                             desc=row['description'],
                             utterances=row['utterances'],
                             fulfillment=row['fulfillment'])
    if response['ResponseMetadata']['HTTPStatusCode'] != 200:
        print("Creating the intents failed :(!\n", response)
        break















df['intentname'].unique()
utterances = df[df['intentname'] == 'Agile']['utterances'].values.tolist()
print(utterances)

for key in utterances:
    utterances['utterance'] = utterances.pop(key)


dictionary to string
the str.replace()

hello = '0:'

import re

utterances = str(df[df['intentname'] == 'Agile']['utterances'].to_dict())

new = re.sub(
           "[0-9]\:",
           "utterance",
    utterances
       )