import pytest


from helper import *
from data_py.rethink.sifter import *


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

