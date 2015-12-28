""" This module contains all the data objects for holding tweet data"""
from datetime import datetime
import pytz

class User(object):
    """ Represents a Twitter user """
    def __init__(self):
        self.id = None
        self.name = None
        self.screen_name = None
        self.location = None

    def populate(self, data):
        """ Populates data in instance from the JSON from twitter"""
        self.id = data["id"]
        self.name = data["name"]
        self.screen_name = data["screen_name"]
        self.location = data["location"]

class Tweet(object):
    @staticmethod
    def parse_date(stamp):
        fmt = '%a %b %d %H:%M:%S +0000 %Y'
        return datetime.strptime(stamp, fmt).replace(tzinfo=pytz.UTC)

    def __init__(self):
        self.id = None
        self.user_id = None
        self.text = None
        self.retweet_count = None
        self.favorite_count = None
        self.created_at = None

    def populate(self, data):
        """ Populates data in instance from the JSON from twitter"""
        self.id = data["id"]
        self.user_id = data["user"]["id"]
        self.text = data["text"]
        self.retweet_count = data["retweet_count"]
        self.favorite_count = data["favorite_count"]
        self.created_at = Tweet.parse_date(data["created_at"])

