import csv

def twitter_analytics(filename):
    '''Opens, reads and prints the data from twitter analytics.
    To change what is printed you must change the strings in
    line 34 to the names of the columns you would like to print.'''
    text_data = {}
    with open(filename) as f:
        data = csv.DictReader(f)
        for row in data:
            text_data[row['Tweet text']] = row['engagements']
        # grabs the maximum number of engagements
        max_num = max(text_data.values())
        for key, value in text_data.items():# loops through the dictionary
            # checks the dictionary value(engagements) against our known max
            if value == max_num:
                # prints the key(Tweet_text) out
                #so we know which was most engaging.
                print (key)

