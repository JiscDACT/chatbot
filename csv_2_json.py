### Convert the CSV file to JSON format

import csv
import json
import os
 
def csv_to_json(csv_file_path, json_file_path):
    #create a dictionary
    data_dict = {}
 
    #Step 2
    #open a csv file handler
    with open(csv_file_path, encoding = 'utf-8') as csv_file_handler:
        csv_reader = csv.DictReader(csv_file_handler)
 
        #convert each row into a dictionary
        #and add the converted data to the data_variable
 
        for rows in csv_reader:
 
            #column named 'name' is the primary key
            key = rows['name']
            data_dict[key] = rows
 
    #open a json file handler and use json.dumps
    #method to dump the data
    #Step 3
    with open(json_file_path, 'w', encoding = 'utf-8') as json_file_handler:
        #Step 4
        json_file_handler.write(json.dumps(data_dict, indent = 4))
 

 
#Step 1
# Get path of current file 
#C:\\Users\\vicky.duxbury\\OneDrive - Jisc\\GitHub\\chatbot\\intents_utterances.csv
user = os.getlogin()

csv_file_path = os.path.join("C:\\Users\\" + user + '\\OneDrive - Jisc\\GitHub\\chatbot\\intents_utterances.csv')
json_file_path = os.path.join("C:\\Users\\" + user + '\\OneDrive - Jisc\\GitHub\\chatbot\\intents_utterances.json')
 
csv_to_json(csv_file_path, json_file_path)