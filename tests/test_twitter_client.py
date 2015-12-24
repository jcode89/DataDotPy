from data_py.twitter_client import *
from data_py.configuration import Configuration
import data_py

import pytest


def test_twitter_client_does_authentication():
    client = TwitterClient()
    config = Configuration()

    assert not client.authenticated
    client.authenticate(config)
    assert client.authenticated

def test_cursor_search_uses_closure(monkeypatch):
    # monkeypatching twitter_client to avoid twitter call and
    # return [1,2,3,4] instead of a list of tweets
    def fake_cursor(api, **kwargs):
        return [1,2,3,4]

    monkeypatch.setattr(data_py.twitter_client, "cursor", fake_cursor)

    # this is the closure that will be called for each tweet
    target = []
    def closure(tweet):
        target.append(tweet)

    client = TwitterClient()
    client.search(closure, q='testing goats')

    assert [1,2,3,4] == target

def test_tweepy_mode_on_by_default():
    """ Tweepy has issues with outputing JSON and so I would like to
    transition to the twitter module instead.  This will be a gradual
    process starting with the search method of the twitter client
    to test if tweepy is being used a tweepy_mode flag will be set.
    Ultimately I think it would be best to transtion compeltely to
    the twitter module, rendering this feature and test obsolete"""
    client = TwitterClient()
    assert client.tweepy_mode

def test_using_json_mode_switches_from_tweepy_to_twitter():
    client = TwitterClient()
    config = Configuration()

    client.authenticate(config, True)
    assert not client.tweepy_mode

def test_twitter_client_does_authentication_with_twitter_module():
    client = TwitterClient()
    config = Configuration()

    assert not client.authenticated
    client.authenticate_with_twitter(config)
    assert client.authenticated

