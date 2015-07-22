import csv
import tweepy
import sqlite3

class TwitterAnalyzer(object):
    def __init__(self):
        self.file_name = "tweet_JvCode.csv"
        
       
    
    def key_grabber(self):
        
        self.consumer_key = ""
        self.consumer_secret = ""
        self.access_token = ""
        self.access_token_secret = ""
    
    def twitter_analytics(self):
        
        text_data ={}
    
        with open(self.file_name) as f:
            data = csv.DictReader(f)
            for row in data:
                text_data[row['Tweet text']]=row['engagements']
            max_num = max(text_data.values())# grabs the maximum number of engagements
            for key, value in text_data.items():# loops through the dictionary
                if value == max_num:# checks the dictionary value(engagements) against our known max
                    print (key)# prints the key(Tweet_text) out so we know which was most engaging. 
       
    def twitter_miner(self):
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        
        api = tweepy.API(auth)
        tweets = []
        public_tweets = tweepy.Cursor(api.search, q='BigData').items(1000)
        for tweet in public_tweets:
            tweets.append(tweet)
        #print(len(tweets))
        return tweets
        
class StdOutListener(tweepy.StreamListener):
    conn = sqlite3.connect('TweetData.db')
    def on_status(self, status):
        
        
        try:
            c = self.conn.cursor()
            #c.execute('''CREATE TABLE tweets
                    #(created, text, user, source)''')
            c.execute("INSERT INTO tweets VALUES(?,?,?,?)", (status.created_at,
                                                        status.text,
                                                        status.user.screen_name,
                                                        status.source))
            self.conn.commit()
        #finally:
            
            #self.conn.close()
            #print("Connection Terminated")
        except Exception:
            pass
        
    def on_error(self, status):
        print (status)
        
class TweetStream(object):
    
    def key_grabber(self):
       
        self.consumer_key = ""
        self.consumer_secret = ""
        self.access_token = ""
        self.access_token_secret = ""
        
    def streamer(self):
        listen = StdOutListener()
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        stream = tweepy.Stream(auth, listen)
        stream.filter(track=['BigData', 'MongoDB', 'MySQL'])
        print(stream)
    