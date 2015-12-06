import pytest
import data_py.configuration

from data_py.configuration import *

"""
Test the Configutation class
"""
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

"""
Test the EnvironmentConfigutation class
"""
@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    def envreturn(key):
        return "{}_RESULT".format(key)

    monkeypatch.setattr(data_py.configuration, "environ", envreturn)

@pytest.fixture()
def env():
    return EnvironmentConfiguration()

def test_default_api_key_name(env):
    assert "TWITTER_API_KEY" == env.consumer_key_name

def test_default_api_secret_name(env):
    assert "TWITTER_API_SECRET" == env.consumer_secret_name

def test_default_token_name(env):
    assert "TWITTER_ACCESS_TOKEN" == env.access_token_name

def test_default_token_secret_name(env):
    assert "TWITTER_ACCESS_TOKEN_SECRET" == env.access_token_secret_name

def test_api_key_name_returns_env_variable(env):
    conf = env.build_configuration()
    assert "TWITTER_API_KEY_RESULT" == conf.consumer_key

def test_api_secret_name_returns_env_variable(env):
    conf = env.build_configuration()
    assert "TWITTER_API_SECRET_RESULT" == conf.consumer_secret

def test_token_name_returns_env_variable(env):
    conf = env.build_configuration()
    assert "TWITTER_ACCESS_TOKEN_RESULT" == conf.access_token

def test_token_secret_name_returns_env_variable(env):
    conf = env.build_configuration()
    assert "TWITTER_ACCESS_TOKEN_SECRET_RESULT" == conf.access_token_secret

