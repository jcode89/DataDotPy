""" This module contains the client that talks to Twitter """
import tweepy
import sqlite3

def cursor(api, **kwargs):
    """ Wraps the tweepy Cursor call to make this generic """
    return tweepy.Cursor(api.search, **kwargs).items(1000)

def stream(auth, listener):
    return tweepy.Stream(auth, listen)

class TwitterClient(object):
    """ This class wraps the Tweepy API """

    def __init__(self):
        """ Initialize the instance """
        self.authenticated = False
        self.api = None

    def authenticate(self, config, json=False):
        """ Authenticates the user with Twitter """
        self.auth = tweepy.OAuthHandler(config.consumer_key, \
                                        config.consumer_secret)
        self.auth.set_access_token(config.access_token, \
                                   config.access_token_secret)
        if json:
            self.api = tweepy.API(self.auth, \
                                  parser=tweepy.parsers.JSONParser())
        else:
            self.api = tweepy.API(self.auth)

        self.authenticated = True

    def search(self, tweet_callback, **kwargs):
        """ Performs a search using the arguments specified in kwargs

        Parameters
            * tweet_callback - This is a reference to a function that will
                               be called for each tweet returned
            * kwargs         - The twitter API query parameters
        """
        tweets = cursor(self.api, **kwargs)

        for tweet in tweets:
            tweet_callback(tweet)

    def stream(self, listener, filter_list):
        """ Uses the Twitter stream API
            * listener    - Instance of tweepy's StreamListener
            * filter_list - List of terms to filter
        """
        result = stream(self.auth, listener)
        result.filter(track=filter_list)
        print(result)

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

