# remember in windows, for now, to use chcp 65001
# type that into the terminal then hit enter then
# run your script.

from data_py.rethink.collector import TweetStream, database_connect
from data_py.rethink.sifter import TwitterAnalyzer
from data_py.configuration import EnvironmentConfiguration

def analyze_tweets():
    # Create an instance of the class you want to use
    twitter = TwitterAnalyzer()

    # Configure
    config = EnvironmentConfiguration()

    # Load the keys needed for OAuth
    twitter.key_grabber(config)

    # Connect and create your database and table
    connect1 = database_connect('chat_test_1')
    Connect2 = database_connect('time_test_1')

    print('''What would you like to do open a stream,
        work with the RESTful, or with the csv file?''')
    response = input("> ").lower()

    if response == "restful":
        twitter.twitter_miner()# requires the calling of twitter.key_grabber()
    elif response == "csv":
        twitter.twitter_analytics()# prints out data from the twitter analytics csv file
    elif response == "stream":
        print("Please enter the keyword you wish to track.")
        resp = input("> ")
        tag = resp.split()
        print("Please enter the amount of time in seconds you would like spend to collecting.")
        print("3600 seconds = 1 hour")
        amnt_of_time = int(input("> "))
        streamer = TweetStream(amnt_of_time, tag)
        streamer.key_grabber(config)
        streamer.streamer()# A live stream of tweets
    else:
        print("Oops, check your spelling!")
