"""
This module uses a sqlite backend to analyze and stream tweets

# remember in windows, for now, to use chcp 65001
# type that into the terminal then hit enter then
# run your script.
"""

from data_py.sqlite.collector import TwitterAnalyzer
from data_py.configuration import EnvironmentConfiguration
from data_py.twitter_client import TwitterClient, SqliteListener

def analyze_tweets():
    """ Performs tweet analytics """
    twitter = TwitterAnalyzer()
    twitter.twitter_analytics()# prints out data from the twitter analytics csv

def print_text(tweet):
    print(tweet.text)

def show_tweets(search):
    env_config = EnvironmentConfiguration()
    listener = SqliteListener()
    twitter = TwitterClient()
    config = env_config.build_configuration()
    twitter.authenticate(config)
    twitter.search(print_text, q=search)

def stream_tweets():
    """ Streams a live stream of tweets """
    env_config = EnvironmentConfiguration()
    listener = SqliteListener()
    twitter = TwitterClient()
    config = env_config.build_configuration()
    twitter.authenticate(config)

    filter_list = ['BigData', 'MongoDB', 'MySql']
    twitter.stream(listener, filter_list)



