import pytest


from data_py.configuration import ConfigService, Configuration


class TestConfig(ConfigService):
    def build_configuration(self):
        conf = Configuration()
        conf.consumer_key = "aa"
        conf.consumer_secret = "bb"
        conf.access_token = "cc"
        conf.access_token_secret = "dd"
        return conf

