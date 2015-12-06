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
        self.retweets = []
        self.favorites = []
        self.doc_check =[]
        for document in self.fetch:
            self.data.append(document)
            self.chat_list.append((document['user']['screen_name'],
                                    document['text'], document['user']['location']))
            if document['user']['screen_name'] not in self.actual_user:
                self.actual_user.append(document['user']['screen_name'])
            if document['user']['location'] not in self.user_locations:
                self.user_locations.append(document['user']['location'])
            if 'retweeted_status' in document:
                self.retweets.append((document['retweeted_status']['user']['screen_name'],
                                     document['retweeted_status']['text'],
                                     document['retweeted_status']['retweet_count']))

                self.favorites.append((document['retweeted_status']['user']['screen_name'],
                                    document['retweeted_status']['text'],
                                    document['retweeted_status']['favorite_count']))
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
        # The locations are saved in a list, because more may be done with them later
        print("Locations: ", len(self.user_locations))
        # The amount of original tweets
        print("Original Tweets: %d" % (self.total - len(self.retweets)))
        # The amount of Retweets.
        print("Retweets: %d" % len(self.retweets))
        # The amount of favorites.
        print("Favorites count: %d" % len(self.favorites))
        # This section of code finds the highest retweet count so the user can see
        # How many times a tweet was retweeted.
        empty_var = 0
        for text_num in self.retweets:
            # Checks the current number of rewteets against the number that
            # was just checked before.
            if text_num[2] > empty_var:
                # We accomplish this by saving the greater of the two numbers in
                # the empty variable and checking the numbers over until we find
                # the larger one.
                empty_var = text_num[2]
                highest_rt = text_num
        print("Most retweeted tweet: ", highest_rt)

        empty_fav = 0
        for fav_num in self.favorites:
            if fav_num[2] > empty_fav:
                empty_fav = fav_num[2]
                highest_fav = fav_num
        print("Most favorited Tweet: ", highest_fav)
        # Prints exact time programs was run, including the date.
        print(self.time_now)

        # stores the data in a new table in the database.
        # You should make sure you create the table and db using the database_connect
        # function.
        try:
            r.db('tweet_test').table_create('tweet_results').run(self.conn)
            r.db('tweet_test').table('tweet_results').insert({'users': self.user_num,
                                                        'users_ratio': self.user_ratio,
                                                        'Locations': self.user_locations,
                                                        'Retweets': self.retweets,
                                                        'Time': self.time_now}).run(self.conn)
        except:
            r.db('tweet_test').table('tweet_results').insert({'users': self.user_num,
                                                        'users_ratio': self.user_ratio,
                                                        'Locations': self.user_locations,
                                                        'Retweets': self.retweets,
                                                        'Time': self.time_now}).run(self.conn)

    def close_the_database(self):
        '''Close the open file and close the connection to the database.'''
        # close the file and database connection
        self.open_file.close()
        self.conn.close()
