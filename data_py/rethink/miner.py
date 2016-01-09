# remember in windows, for now, to use chcp 65001
# type that into the terminal then hit enter then
# run your script.

from data_py.twitter_client import *
from data_py.configuration import EnvironmentConfiguration

def stream_tweets():
    # Configure
    env_config = EnvironmentConfiguration()
    config = env_config.build_configuration()
    
    # Connect and create your database and table
    connect1 = database_connect('chat_test_1')
    Connect2 = database_connect('time_test_1')

    """ Streams a live stream of tweets """
    listener = RethinkListener()
    twitter = TwitterClient()
    twitter.authenticate(config)

    filter_list = ['BigData', 'MongoDB', 'MySql']
    twitter.stream_adv(listener, filter_list)
