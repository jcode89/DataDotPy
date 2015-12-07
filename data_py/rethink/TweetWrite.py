'''Run this script to gather the data already collected and prep for analysis.
save the user: tweet information to a text file, and finally,
analyze the data gathered and save it to the database.'''

import rethinkdb as r
import datetime

class DataFilter(object):
    '''Use this to pull info from the database, write it to a file,
    analyze it and then close the database and file of course.'''
    def __init__(self):
        # Open the database connection and gather the data needed for later
        self.conn = r.connect('localhost', 28015)

    def database_pull(self):
        '''Pulls data out of the database and counts the number of total tweets captured.'''
        self.fetch = r.db("test").table("chat_test_1").run(self.conn)
        self.total = 0
        self.data=[]
        self.chat_list = []
        self.actual_user = []
        self.user_locations = []
        for document in fetch:
            self.data.append(document)
            self.chat_list.append((document['user']['screen_name'],
                                    document['text'], document['user']['location']))
            if document['user']['screen_name'] not in self.actual_user:
                self.actual_user.append(document['user']['screen_name'])
            if document['user']['location'] not in self.user_locations:
                self.user_locations.append(document['user']['location'])
            self.total+=1

    def write_to_file(self):
        '''Writes the user and user's tweet to a file for archival purposes.'''
        # Write the user and the tweet to a txt file.
        self.open_file = open("ChatArchive.txt", 'w')
        for text in self.chat_list:
            # write each line in the list to the file using a double space for each.
            self.open_file.write((str(text)+ "\n"+"\n"))

    def analyze_data(self):
        '''Analyze all of the data pulled from the database and store it in a new table
        in the database.'''
        # analyze the information gathered from above and save it to the database.
        self.user_num = len(self.actual_user)
        self.user_ratio = float(self.total/len(self.actual_user))
        self.time_now = datetime.datetime.now().strftime("%B, %d, %Y, %X")
        print("Number of Tweets: %d" % self.total)
        # Number of users that sent out tweets.
        # Multiple tweets per user still count as one user.
        print("Number of actual users: %d" % self.user_num)
        # Tweets per user, or Tweets:user
        print("Tweets per user: %.2f" % self.user_ratio)
        # Prints exact time programs was run, including the date.
        print(self.time_now)
        # The locations are saved in a list, because more may be done with them later
        print("Locations: ", len(self.user_locations))

    def close_the_database(self):
        '''Close the open file and close the connection to the database.'''
        # close the file and database connection
        self.open_file.close()
        self.conn.close()
