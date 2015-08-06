# remember in windows, for now, to use chcp 65001
# type that into the terminal then hit enter then 
# run your script.

from TweetCollector import TwitterAnalyzer, TweetStream

twitter = TwitterAnalyzer()
streamer = TweetStream()

       

   
  
twitter.key_grabber()# loads the keys needed for OAuth
twitter.twitter_analytics()# prints out data from the twitter analytics csv file
twitter.twitter_miner()# requires the calling of twitter.key_grabber() 
streamer.key_grabber()
streamer.streamer()# A live stream of tweets
   
    
