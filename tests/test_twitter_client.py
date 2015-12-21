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


