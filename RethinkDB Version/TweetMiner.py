# remember in windows, for now, to use chcp 65001
# type that into the terminal then hit enter then
# run your script.

from TweetCollector import TweetStream, database_connect
from TweetSifter import TwitterAnalyzer

# Create an instance of the class you want to use
twitter = TwitterAnalyzer()


# Load the keys needed for OAuth
twitter.key_grabber()
streamer.key_grabber()

# Connect and create your database and table
connect = database_connect()

print('''What would you like to do open a stream,
    work with the RESTful, or with the csv file?''')
response = input("> ").lower()

if response == "restful":
    twitter.twitter_miner()# requires the calling of twitter.key_grabber()
elif response == "csv":
    twitter.twitter_analytics()# prints out data from the twitter analytics csv file
elif response == "stream":
    print("Please enter the keyword you wish to track.")
    tag = input("> ")
    print("Please enter the number of tweets you would like to collect.")
    num_tweets = int(input("> "))
    streamer = TweetStream(num_tweets, tag)
    streamer.streamer()# A live stream of tweets
else:
    print("Oops, check your spelling!")

