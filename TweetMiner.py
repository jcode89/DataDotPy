# remember in windows, for now, to use chcp65001
# type that into the terminal then hit enter then 
# run your script.
import sqlite3
import csv

try:
    conn = sqlite3.connect('TweetData.db')
    c = conn.cursor()
    file_name = "tweet_JvCode.csv"
    text_data ={}
    
    with open(file_name) as f:
        data = csv.DictReader(f)
        for row in data:
            text_data[row['Tweet text']]=row['engagements']
        max_num = max(text_data.values())# grabs the maximum number of engagements
        for key, value in text_data.items():# loops through the dictionary
            if value == max_num:# checks the dictionary value(engagements) against our known max
                print (key)# prints the key(Tweet_text) out so we know which was most engaging. 
       
finally:
    conn.close()
    print("Connection Terminated")