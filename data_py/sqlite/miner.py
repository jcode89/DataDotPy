"""
This module uses a sqlite backend to analyze and stream tweets

# remember in windows, for now, to use chcp 65001
# type that into the terminal then hit enter then
# run your script.
"""

from data_py.sqlite.TweetCollector import TwitterAnalyzer, TweetStream
from data_py.configuration import EnvironmentConfiguration

def analyze_tweets():
    """ Performs tweet analytics """
    env_config = EnvironmentConfiguration()
    config = env_config.build_configuration()
    twitter = TwitterAnalyzer()
    twitter.key_grabber(config)# loads the keys needed for OAuth
    twitter.twitter_analytics()# prints out data from the twitter analytics csv
    twitter.twitter_miner()# requires the calling of twitter.key_grabber()

def stream_tweets():
    """ Streams a live stream of tweets """
    env_config = EnvironmentConfiguration()
    config = env_config.build_configuration()
    streamer = TweetStream()
    streamer.key_grabber(config)
    streamer.streamer()# A live stream of tweets

