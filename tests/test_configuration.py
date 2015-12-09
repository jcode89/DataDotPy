import pytest
import data_py.configuration

from data_py.configuration import *

"""
Test the Configuration class
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
Test the ConfigService class
"""
def test_build_configuration_throws_not_implemented_error():
    subject = ConfigService()

    try:
        subject.build_configuration()
    except NotImplementedError as e:
        assert e.args[0] == "This class defines an interface and should not be used directly"
    else:
        assert False, "Expected a NotImplementedError"

"""
Test the EnvironmentConfiguration class
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

def test_api_key_name_can_be_overridden():
    env = EnvironmentConfiguration(consumer_key_name="TEST")
    conf = env.build_configuration()
    assert "TEST_RESULT" == conf.consumer_key

def test_api_secret_name_can_be_overridden():
    env = EnvironmentConfiguration(consumer_secret_name="TEST")
    conf = env.build_configuration()
    assert "TEST_RESULT" == conf.consumer_secret

def test_is_instance_of_config_service():
    env = EnvironmentConfiguration()
    assert isinstance(env, ConfigService)
def test_token_name_can_be_overridden():
    env = EnvironmentConfiguration(access_token_name="TEST")
    conf = env.build_configuration()
    assert "TEST_RESULT" == conf.access_token

def test_token_secret_name_can_be_overridden():
    env = EnvironmentConfiguration(access_token_secret_name="TEST")
    conf = env.build_configuration()
    assert "TEST_RESULT" == conf.access_token_secret


