"""
This module contains all of the configuration tools and informaton
"""
import os

def environ(key):
    return os.environ[key]

class Configuration:
    """A central structure for holding config items"""
    def __init__(self):
        self.consumer_key = ""
        self.consumer_secret = ""
        self.access_token = ""
        self.access_token_secret = ""

class EnvironmentConfiguration:
    """
    A class that will populate your configuration from environment variables
    """
    def __init__(self, consumer_key_name = "TWITTER_API_KEY", \
                      consumer_secret_name="TWITTER_API_SECRET", \
                      access_token_name = "TWITTER_ACCESS_TOKEN", \
                      access_token_secret_name = "TWITTER_ACCESS_TOKEN_SECRET"):
        self.consumer_key_name = consumer_key_name
        self.consumer_secret_name = consumer_secret_name
        self.access_token_name = access_token_name
        self.access_token_secret_name = access_token_secret_name

    def build_configuration(self):
        conf = Configuration()
        conf.consumer_key = environ(self.consumer_key_name)
        conf.consumer_secret = environ(self.consumer_secret_name)
        conf.access_token = environ(self.access_token_name)
        conf.access_token_secret = environ(self.access_token_secret_name)
        return conf

