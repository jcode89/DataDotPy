import pytest

from helper import *
from data_py.configuration import ConfigService, Configuration
from data_py.sqlite.collector import *


def test_analyzer_key_grabber_takes_configuration():
    conf = TestConfig()
    analyzer = TwitterAnalyzer()

    analyzer.key_grabber(conf)
    assert analyzer.configuration_service == conf

def test_analyzer_sets_configuration():
    conf = TestConfig()
    analyzer = TwitterAnalyzer()

    analyzer.key_grabber(conf)
    assert analyzer.consumer_key == "aa"
    assert analyzer.consumer_secret == "bb"
    assert analyzer.access_token == "cc"
    assert analyzer.access_token_secret == "dd"

def test_streamer_key_grabber_takes_configuration():
    conf = TestConfig()
    analyzer = TweetStream()

    analyzer.key_grabber(conf)
    assert analyzer.configuration_service == conf

def test_streamer_sets_configuration():
    conf = TestConfig()
    analyzer = TweetStream()

    analyzer.key_grabber(conf)
    assert analyzer.consumer_key == "aa"
    assert analyzer.consumer_secret == "bb"
    assert analyzer.access_token == "cc"
    assert analyzer.access_token_secret == "dd"
