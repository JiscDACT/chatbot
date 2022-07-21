### Convert the JSON file to CSV format
# This is useful when manually exporting intents from Amazon Lex

import json
import os
import csv

user = os.getlogin()

csv_file_path = os.path.join("C:\\Users\\" + user + '\\OneDrive - Jisc\\GitHub\\chatbot\\TRAVEL\\Intent.csv')
json_file_path = os.path.join("C:\\Users\\" + user + '\\OneDrive - Jisc\\GitHub\\chatbot\\TRAVEL\\Intent.json')

 # clean dictionary
def dict_clean(items):
    result = {}
    for key, value in items:
        if value is None:
            value = 'None'
        result[key] = value
    return result  

# Load JSON file
with open(json_file_path) as json_data:
    data = json.load(json_data, object_pairs_hook=dict_clean) 


# Export dictionary to CSV
with open(csv_file_path, "w", newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(data.keys())
    writer.writerow(data.values())
    
