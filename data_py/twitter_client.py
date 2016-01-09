""" This module contains the client that talks to Twitter """
import tweepy
import twitter
import sqlite3
from tqdm import tqdm

def cursor(api, **kwargs):
    """ Wraps the tweepy Cursor call to make this generic """
    return tweepy.Cursor(api.search, **kwargs).items(1000)

def stream(auth, listener):
    return tweepy.Stream(auth, listener)

class TwitterClient(object):
    """ This class wraps the Tweepy API """

    def __init__(self):
        """ Initialize the instance """
        self.authenticated = False
        self.api = None
        self.rate_limit = 500
        self.tweepy_mode = True

    def authenticate_with_tweepy(self, config):
        """ Authenticates the user with Tweepy """
        self.auth = tweepy.OAuthHandler(config.consumer_key, \
                                        config.consumer_secret)
        self.auth.set_access_token(config.access_token, \
                                   config.access_token_secret)
        self.api = tweepy.API(self.auth)

        self.tweepy_mode = True
        self.authenticated = True

    def authenticate_with_twitter(self, config):
        """ Authenticates the user with Twitter """
        self.auth = twitter.OAuth(config.access_token, \
                                  config.access_token_secret, \
                                  config.consumer_key, \
                                  config.consumer_secret)

        self.tweepy_mode = False
        self.api = twitter.Twitter(auth=self.auth)
        self.authenticated = True

    def authenticate(self, config, json=False):
        """ Authenticates the user with Twitter """
        if json:
            self.authenticate_with_twitter(config)
        else:
            self.authenticate_with_tweepy(config)

    def search(self, tweet_callback, **kwargs):
        """ Performs a search using the arguments specified in kwargs

        Parameters
            * tweet_callback - This is a reference to a function that will
                               be called for each tweet returned
            * kwargs         - The twitter API query parameters
        """
        if self.tweepy_mode:
            tweets = cursor(self.api, **kwargs)
        else:
            results = self.api.search.tweets(**kwargs)
            tweets = results['statuses']

        for tweet in tweets:
            tweet_callback(tweet)

    def stream(self, listener, filter_list):
        """ Uses the Twitter stream API
            * listener    - Instance of tweepy's StreamListener
            * filter_list - List of terms to filter
        """
        result = stream(self.auth, listener)
        # Adds the funcitonality to stream for a specified amount of time.
        try:
            # May need to be tested! self.tag should be a list.
            result.filter(track=filter_list, async=True)
            timeout = time.time() + self.rate_limit
            # Allows a progress bar to be displayed
            with tqdm(total=self.rate_limit) as probar:
                while True:
                    for seconds in range(self.rate_limit):
                        probar.update(1)
                        time.sleep(1)
                    if time.time() >= timeout:
                        result.disconnect()
                        break
        except HTTPException as e:
            # This includes IncompleteRead.
            result.filter(track=filter_list, async=True)
            timeout = time.time() + self.rate_limit
            with tqdm(total=self.rate_limit) as probar:
                while True:
                    for seconds in range(self.rate_limit):
                        probar.update(1)
                        time.sleep(1)
                    if time.time() >= timeout:
                        result.disconnect()
                        break

    def stream_adv(self, listener, filter_list):
        ## version of the streamer from rethink. TODO merge with stream()
        '''Instantiates the listener class we created above and
        also access the stream. stream.filter(track=[]) is where,
        you tell tweepy what keywords to look for.'''
        result = stream(self.auth, listener)
        # This code should allow the user to stream for a specified amount of time.
        try:
            # May need to be tested! self.tag should be a list.
            result.filter(track=filter_list, async=True)
            timeout = time.time() + self.rate_limit
            # Allows a progress bar to be displayed
            with tqdm(total=self.rate_limit) as probar:
                while True:
                    for seconds in range(self.rate_limit):
                        probar.update(1)
                        time.sleep(1)
                    if time.time() >= timeout:
                        result.disconnect()
                        break
        except HTTPException as e:
            # This includes IncompleteRead.
            result.filter(track=filter_list, async=True)
            timeout = time.time() + self.rate_limit
            with tqdm(total=self.rate_limit) as probar:
                while True:
                    for seconds in range(self.rate_limit):
                        probar.update(1)
                        time.sleep(1)
                    if time.time() >= timeout:
                        result.disconnect()
                        break

class SqliteListener(tweepy.StreamListener):
    '''Used to override the StreamListener so you can do what you want
    with the data streaming in.'''
    conn = sqlite3.connect('TweetData.db')
    def on_status(self, status):
        '''Prints the data on screen and stores certain parts in a SQLite
        database.'''
        print(status)
        try:
            c = self.conn.cursor()# needed to perform execute.
            c.execute('''CREATE TABLE IF NOT EXISTS tweets
                    (created, text, user, source)''')
            c.execute("INSERT INTO tweets VALUES(?,?,?,?)", (status.created_at,
                                                        status.text,
                                                        status.user.screen_name,
                                                        status.source))
            self.conn.commit()
        #finally:
            #self.conn.close()
            #print("Connection Terminated")
        except Exception:
            pass

    def on_error(self, status):
        '''prints out any errors that come from the listener.'''
        print (status)

### rethink collector

'''Use this module to collect tweets from the live stream.'''
import tweepy
import json
import time
import rethinkdb as r
from rethinkdb.errors import RqlRuntimeError
from urllib3.connection import HTTPException

class RethinkListener(tweepy.StreamListener):
    '''Used to override the StreamListener so you can do what you want
    with the data streaming in.'''
    def __init__(self):
        self.conn = r.connect('localhost', 28015)
    def on_data(self, data):
        '''Prints the data on screen and stores the data in a RethinkDB
        database.'''
        try:
            tweet_data = json.loads(data)
            r.db('test').table('chat_test_1').insert(tweet_data).run(self.conn)

        except Exception:
            pass

    def on_error(self, status):
        '''prints out any errors that come from the listener.'''
        print (status)


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
