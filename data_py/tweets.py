""" This module contains all the data objects for holding tweet data"""

class User(object):
    def __init__(self):
        self.id = None
        self.name = None
        self.screen_name = None

    def populate(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.screen_name = data["screen_name"]
