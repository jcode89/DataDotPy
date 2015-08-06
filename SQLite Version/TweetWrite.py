'''Run this script to gather the data already collected and prep for analysis.
save the user: tweet information to a text file, and finally,
analyze the data gathered and save it to the database.'''

import sqlite3
import datetime

class DataFilter(object):
    '''Use this to pull info from the database, write it to a file,
    analyze it and then close the database and file of course.'''
    def __init__(self):
        # Open the database connection and gather the data needed for later
        self.conn = sqlite3.connect('TweetData.db')
        self.c = self.conn.cursor()

    def database_pull(self):
        '''Pulls data out of the database and counts the number of total tweets captured.'''
        self.c.execute('''CREATE TABLE IF NOT EXISTS data(Total Tweets,
                                            Actual User,
                                            Tweet User Ratio,
                                            Date Time)''')
        self.fetch = self.c.execute("select user, text from codenewbie")
        self.total = 0
        self.chat_list = []
        self.actual_user = []
        for user, text in self.fetch:# unpack the tuple
            # append the chat_list and encode the text properly
            self.chat_list.append((user, text.encode('ascii', 'xmlcharrefreplace')))
            if user not in self.actual_user:
                self.actual_user.append(user)
            print(user, text)
            self.total += 1

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
        self.c.execute("INSERT INTO data VALUES(?,?,?,?)", (self.total,
                                                            self.user_num,
                                                            self.user_ratio,
                                                            self.time_now))
        self.conn.commit()

    def close_the_database(self):
        '''Close the open file and close the connection to the database.'''
        # close the file and database connection
        self.open_file.close()
        self.conn.close()
