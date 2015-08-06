'''Use this module to collect tweets, and any data that goes along with it.
Whether it is from a file or from the RESTful or from the live stream,
this is the module you want.'''
import csv
import tweepy
import json
import rethinkdb as r

class TwitterAnalyzer(object):
    '''The class used to analyze data files obtained from Twitter,
     as well as, grabbing tweets that had already been tweeted,
     in other words not live streamed.'''
    def __init__(self):
        self.file_name = "tweet_JvCode.csv"
        self.consumer_key = ""
        self.consumer_secret = ""
        self.access_token = ""
        self.access_token_secret = ""

    def key_grabber(self):
        '''Used to store the keys needed for OAuth.'''
        self.consumer_key = ""
        self.consumer_secret = ""
        self.access_token = ""
        self.access_token_secret = ""

    def twitter_analytics(self):
        '''Opens, reads and prints the data from twitter analytics.
        To change what is printed you must change the strings in
        line 34 to the names of the columns you would like to print.'''
        text_data = {}
        with open(self.file_name) as f:
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

    def twitter_miner(self):
        '''Used to grab tweets already tweeted, it is part of the RESTful API.
        To choose what tweets you get change the string in q.
        To choose how many tweets you get change the value in items.'''
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)
        tweets = []
        # Searches the public tweets.
        public_tweets = tweepy.Cursor(api.search, q='BigData').items(1000)
        for tweet in public_tweets:
            tweets.append(tweet)

        return tweets

# This works best outside class StdOutListener.
db_name = 'test'# Enter name of your database
table_name = 'chat_test_1'# Enter name of your table
conn = r.connect('localhost', 28015)
try:
    r.db(db_name).table_create(table_name).run(conn)
except:
    r.db(db_name).table(table_name).run(conn)

class StdOutListener(tweepy.StreamListener):
    '''Used to override the StreamListener so you can do what you want
    with the data streaming in.'''
    def on_data(self, data):
        '''Prints the data on screen and stores certain parts in a RethinkDB
        database.'''
        print(data)
        try:
            tweet_data = json.loads(data)
            r.table(table_name).insert(tweet_data).run(conn)
        except Exception:
            pass

    def on_error(self, status):
        '''prints out any errors that come from the listener.'''
        print (status)

class TweetStream(object):
    '''Used to access the streaming portion of the API
     that actually prints out live tweets.'''
    def __init__(self):
        self.consumer_key = ""
        self.consumer_secret = ""
        self.access_token = ""
        self.access_token_secret = ""

    def key_grabber(self):
        '''Grabs the keys needed for OAuth.'''
        self.consumer_key = ""
        self.consumer_secret = ""
        self.access_token = ""
        self.access_token_secret = ""

    def streamer(self):
        '''Instantiates the listener class we created above and
        also access the stream. stream.filter(track=[]) is where,
        you tell tweepy what keywords to look for.'''
        listen = StdOutListener()
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        stream = tweepy.Stream(auth, listen)
        stream.filter(track=['BigData', 'MongoDB', 'MySQL'])
        print(stream)
