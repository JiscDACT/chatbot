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
client = boto3.client('lexv2-models', region_name='eu-west-2',
                      aws_access_key_id=AWS_KEY_ID,
                      aws_secret_access_key=AWS_SECRET)

response = client.create_bot(
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


# -----------------------------------------------------------------------------------------------------------------------
