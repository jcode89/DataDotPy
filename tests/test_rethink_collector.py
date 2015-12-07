import pytest


from tests.helper import *
from data_py.rethink.collector import *


def test_streamer_key_grabber_takes_configuration():
    conf = TestConfig()
    analyzer = TweetStream(1, None)

    analyzer.key_grabber(conf)
    assert analyzer.configuration_service == conf

def test_streamer_sets_configuration():
    conf = TestConfig()
    analyzer = TweetStream(1, None)

    analyzer.key_grabber(conf)
    assert analyzer.consumer_key == "aa"
    assert analyzer.consumer_secret == "bb"
    assert analyzer.access_token == "cc"
    assert analyzer.access_token_secret == "dd"
