import pytest


from data_py.configuration import Configuration


@pytest.fixture
def config():
    return Configuration()

def test_config_has_consumer_key(config):
    assert "" == config.consumer_key

def test_config_has_consumer_secret(config):
    assert "" == config.consumer_secret

def test_config_has_access_token(config):
    assert "" == config.access_token

def test_config_has_access_token_secret(config):
    assert "" == config.access_token_secret

