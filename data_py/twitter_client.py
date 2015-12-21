""" This module contains the client that talks to Twitter """
import tweepy

def cursor(api, **kwargs):
    """ Wraps the tweepy Cursor call to make this generic """
    return tweepy.Cursor(api.search, **kwargs).items(1000)

class TwitterClient(object):
    """ This class wraps the Tweepy API """

    def __init__(self):
        """ Initialize the instance """
        self.authenticated = False
        self.api = None

    def authenticate(self, config):
        """ Authenticates the user with Twitter """
        auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
        auth.set_access_token(config.access_token, config.access_token_secret)
        self.api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
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

