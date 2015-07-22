# remember in windows, for now, to use chcp 65001
# type that into the terminal then hit enter then 
# run your script.
import sqlite3
from TweetCollector import TwitterAnalyzer, TweetStream

twitter = TwitterAnalyzer()
streamer = TweetStream()

       
try:
    conn = sqlite3.connect('TweetData.db')
    c = conn.cursor()
    twitter.key_grabber()# loads the keys needed for OAuth
    twitter.twitter_analytics()
    twitter.twitter_miner()# requires the calling of twitter.key_grabber() 
    streamer.key_grabber()
    streamer.streamer()# A live stream of tweets
   
    
finally:
    conn.close()
    print("Connection Terminated")