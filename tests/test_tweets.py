import pytest
import json
import os
from datetime import datetime
import pytz


from data_py import tweets as t


def test_user_has_id():
    user = t.User()
    assert None == user.id

def test_user_has_name():
    user = t.User()
    assert None == user.name

def test_user_has_screen_name():
    user = t.User()
    assert None == user.screen_name

def test_user_has_locatiion():
    user = t.User()
    assert None == user.location

@pytest.fixture
def user_info():
    cwd = os.getcwd()
    filename = os.path.join(cwd, "tests", "fixtures", "user.json")

    with open(filename) as data:
        user_data = json.load(data)

    return user_data["user"]

def test_user_can_populate_from_json(user_info):
    user = t.User()
    user.populate(user_info)

    assert 1234567890 == user.id
    assert "Test User" == user.name
    assert "The moon" == user.location
    assert "Test_User" == user.screen_name

# Test Tweet Class

def test_tweet_has_id():
    tweet = t.Tweet()
    assert None == tweet.id

def test_tweet_has_user_id():
    tweet = t.Tweet()
    assert None == tweet.user_id

def test_tweet_has_text():
    tweet = t.Tweet()
    assert None == tweet.text

def test_tweet_has_retweet_count():
    tweet = t.Tweet()
    assert None == tweet.retweet_count

def test_tweet_has_favorite_count():
    tweet = t.Tweet()
    assert None == tweet.favorite_count

def test_tweet_has_created_at():
    tweet = t.Tweet()
    assert None == tweet.created_at

@pytest.fixture
def tweet_info():
    cwd = os.getcwd()
    filename = os.path.join(cwd, "tests", "fixtures", "tweet.json")

    with open(filename) as data:
        user_data = json.load(data)

    return user_data[0]

def test_tweet_can_populate_from_json(tweet_info):
    tweet = t.Tweet()
    tweet.populate(tweet_info)

    assert 2345678901 == tweet.id
    assert 1234567890 == tweet.user_id
    assert "Tweet text" == tweet.text
    assert 2 == tweet.retweet_count
    assert 1 == tweet.favorite_count
    expected = datetime(2015, 12, 24, 17, 51, 9).replace(tzinfo=pytz.UTC)
    assert expected == tweet.created_at

def test_tweet_can_parse_twitter_timestamp():
    stamp = 'Thu Feb 12 10:20:30 +0000 2015'
    expected = datetime(2015, 2, 12, 10, 20, 30).replace(tzinfo=pytz.UTC)

    assert t.Tweet.parse_date(stamp) == expected
