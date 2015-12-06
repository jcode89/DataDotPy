"""
This module contains all of the configuration tools and informaton
"""

class Configuration:
    """A central structure for holding config items"""
    def __init__(self):
        self.consumer_key = ""
        self.consumer_secret = ""
        self.access_token = ""
        self.access_token_secret = ""
