# Chatbot Innovation Project

This chatbot innovation project is using Amazon Lex as the AI Chatbot engine, information store will use either postgresql through Amazon RDS or DynamoDB and the deployment plan is to use Microsoft Teams (longer term use REACT JS for the user interface). You can embed the chatbot onto a website using html.

dynamodb uses [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) library to connect to AWS

You need to use IAM AWS service to setup user permissions and for Key/password etc

Currently Alex has been built using the web interface for Amazon Lex for a few sample intents, but we will use the modeling building API long term as per diagram below.

**Current model**

![flowchart](https://user-images.githubusercontent.com/68733783/180014611-dcfd0fe8-ffc3-47d5-883c-8e0e56b49410.png)



We have a alex-lex S3 bucket for the project here (Created using boto rather than web interface):

![image](https://user-images.githubusercontent.com/68733783/180030497-e5e13052-bb50-4145-a603-2050172f8f62.png)
