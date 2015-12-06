'''Use this module to collect tweets from the live stream.'''
import tweepy
import json
import time
import rethinkdb as r
from rethinkdb.errors import RqlRuntimeError
from http.client import IncompleteRead


# This works best outside class StdOutListener as
# it's own function.
def database_connect(name1):
    '''Creates the database and the table if it doesn't already exist'''
    db_name = 'test'# Enter name of your database
    table_name = name1# name of your table
    conn = r.connect('localhost', 28015)
    try:
        try:
            r.db_create(db_name).run(conn)
            r.db(db_name).table_create(table_name).run(conn)
            print("Database setup completed!")
        except RqlRuntimeError:
            r.db(db_name).table_create(table_name).run(conn)
            print("Database already exists!")
    except:
        print("Database and table exist!")
    finally:
        conn.close()

class StdOutListener(tweepy.StreamListener):
    '''Used to override the StreamListener so you can do what you want
    with the data streaming in.'''
    def __init__(self):
        self.conn = r.connect('localhost', 28015)
    def on_data(self, data):
        '''Prints the data on screen and stores the data in a RethinkDB
        database.'''
        print(data)
        try:
            tweet_data = json.loads(data)
            r.db('test').table('chat_test_1').insert(tweet_data).run(self.conn)

        except Exception:
            pass

    def on_error(self, status):
        '''prints out any errors that come from the listener.'''
        print (status)

class TweetStream(object):
    '''Used to access the streaming portion of the API
     that actually prints out live tweets.'''
    def __init__(self, limit, tag):
        self.consumer_key = ""
        self.consumer_secret = ""
        self.access_token = ""
        self.access_token_secret = ""
        self.rate_limit = limit
        self.tag = tag

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
        # This code should allow the user to stream for a specified amount of time.
        try:
            # May need to be tested! self.tag should be a list.
            stream.filter(track=self.tag, async=True)
            timeout = time.time() + self.rate_limit
            while True:
                if time.time() >= timeout:
                    stream.disconnect()
                    break
        except IncompleteRead:
            stream.filter(track=self.tag, async=True)
            timeout = time.time() + self.rate_limit
            while True:
                if time.time() >= timeout:
                    stream.disconnect()
                    break
