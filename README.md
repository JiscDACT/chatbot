# Chatbot Innovation Project

This chatbot innovation project is using Amazon Lex as the AI Chatbot engine, information store will use either postgresql through Amazon RDS or DynamoDB and the deployment plan is to use Microsoft Teams (longer term use REACT JS for the user interface). You can embed the chatbot onto a website using html.

dynamodb uses [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) library to connect to AWS

You need to use IAM AWS service to setup user permissions and for Key/password etc

Currently Alex has been built using the web interface for Amazon Lex for a few sample intents, but we will use the modeling building API long term as per diagram below.

## IT/Cloud Architecture

![image](https://user-images.githubusercontent.com/68733783/182109998-4ea37959-4e7a-45af-bd40-57cf8371fc23.png)






## Further Information
![flowchart](https://user-images.githubusercontent.com/68733783/180014611-dcfd0fe8-ffc3-47d5-883c-8e0e56b49410.png)



We have a alex-lex S3 bucket for the project here (Created using boto rather than web interface):

![image](https://user-images.githubusercontent.com/68733783/180030497-e5e13052-bb50-4145-a603-2050172f8f62.png)



**Connecting to a PostgreSQL Database**

Used these instructions to create the below guide - https://aws.amazon.com/getting-started/hands-on/create-connect-postgresql-db/ 

1.	The RDS instance has already been created (details can be found here https://us-east-1.console.aws.amazon.com/rds/home?region=us-east-1#database:id=database-1;is-cluster=false;tab=connectivity)

2.	We can use any SQL client to connect to the database however in this instance we are using SQL Workbench. SQL workbench can be downloaded here - https://www.sql-workbench.eu/downloads.html. Once downloaded, extract everything from the compressed folder.

![image](https://user-images.githubusercontent.com/76955721/180193055-0c2436a8-c09c-4aff-903b-f48b4de27318.png)

3. Download the latest JDBC driver from the PostgreSQL website - https://jdbc.postgresql.org/.  Save the file in a place where you can easily find it later. This file is needed in the next step.

![image](https://user-images.githubusercontent.com/76955721/180193136-7f70b289-e77d-4f22-b612-139ce6200f4b.png)

4.	Connect to the PostgreSQL database

    a.	From the SQL Workbench extracted file, open the application file.

    b.	A dialogue box will appear which you will need to populate as below:

        i.	Driver: PostgreSQL (org.postgresql.Driver)

        ii.	URL: jdbc:postgresql://database-1.c96qplvjhpi5.us-east-1.rds.amazonaws.com:5432/Information_Store

        iii.	Username: postgres Password: ChatbotAlex123

    Once this has been updated, click ‘OK’. 

    c.	You are now connected to the database. You can return to the Amazon RDS Console, select the instance from the Databases list and you should see that there is an additional connection to the database listed under the Current activity heading.

At this point your database is ready to use. You can start creating tables, insert data, and run queries from SQL Workbench client.

![image](https://user-images.githubusercontent.com/76955721/180193195-722ca030-f7fd-4559-bd72-9e090cf18c2f.png)
