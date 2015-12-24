import pytest
import json


from data_py import configuration
from data_py import twitter_client



def test_alice_makes_twitter_search_output_json():
    # Alice wants to collect tweets as JSON rather then the
    # standard tweepy result object.  This will make it easier
    # for her to write tests without making actual twitter
    # queries in the future
    tweets = []

    def collect_tweets(tweet):
        tweets.append(tweet)

    env_config = configuration.EnvironmentConfiguration()
    twitter = twitter_client.TwitterClient()
    config = env_config.build_configuration()

    # Alice sets the authentication to use the JSON parser
    twitter.authenticate(config, True)

    # Alice searches
    search="#codenewbie"
    twitter.search(collect_tweets, q=search, count=1)

    assert 1 == len(tweets)
    assert "metadata" in tweets[0].keys()
    assert "source" in tweets[0].keys()

