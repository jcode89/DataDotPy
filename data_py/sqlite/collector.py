'''Use this module to collect tweets, and any data that goes along with it.
Whether it is from a file or from the RESTful or from the live stream,
this is the module you want.'''
import csv
import tweepy
import sqlite3

class TwitterAnalyzer(object):
    '''The class used to analyze data files obtained from Twitter,
     as well as, grabbing tweets that had already been tweeted,
     in other words not live streamed.'''
    def __init__(self):
        self.file_name = "tweet_JvCode.csv"
        self.consumer_key = ""
        self.consumer_secret = ""
        self.access_token = ""
        self.access_token_secret = ""

    def key_grabber(self, configuration_service):
        '''Used to set the configuration'''
        self.configuration_service = configuration_service
        conf = self.configuration_service.build_configuration()
        self.consumer_key = conf.consumer_key
        self.consumer_secret = conf.consumer_secret
        self.access_token = conf.access_token
        self.access_token_secret = conf.access_token_secret

    def twitter_analytics(self):
        '''Opens, reads and prints the data from twitter analytics.
        To change what is printed you must change the strings in
        line 34 to the names of the columns you would like to print.'''
        text_data = {}
        with open(self.file_name, "a+") as f:
            data = csv.DictReader(f)
            for row in data:
                text_data[row['Tweet text']] = row['engagements']
            # grabs the maximum number of engagements
            max_num = max(text_data.values())
            for key, value in text_data.items():# loops through the dictionary
                # checks the dictionary value(engagements) against our known max
                if value == max_num:
                    # prints the key(Tweet_text) out
                    #so we know which was most engaging.
                    print (key)

    def twitter_miner(self):
        '''Used to grab tweets already tweeted, it is part of the RESTful API.
        To choose what tweets you get change the string in q.
        To choose how many tweets you get change the value in items.'''
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        api = tweepy.API(auth)
        tweets = []
        # Searches the public tweets.
        public_tweets = tweepy.Cursor(api.search, q='BigData').items(1000)
        for tweet in public_tweets:
            tweets.append(tweet)
        #print(len(tweets))
        return tweets

class StdOutListener(tweepy.StreamListener):
    '''Used to override the StreamListener so you can do what you want
    with the data streaming in.'''
    conn = sqlite3.connect('TweetData.db')
    def on_status(self, status):
        '''Prints the data on screen and stores certain parts in a SQLite
        database.'''
        print(status)
        try:
            c = self.conn.cursor()# needed to perform execute.
            c.execute('''CREATE TABLE IF NOT EXISTS tweets
                    (created, text, user, source)''')
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
        '''prints out any errors that come from the listener.'''
        print (status)

class TweetStream(object):
    '''Used to access the streaming portion of the API
     that actually prints out live tweets.'''
    def __init__(self):
        self.consumer_key = ""
        self.consumer_secret = ""
        self.access_token = ""
        self.access_token_secret = ""

    def key_grabber(self, configuration_service):
        '''Used to set the configuration'''
        self.configuration_service = configuration_service
        conf = self.configuration_service.build_configuration()
        self.consumer_key = conf.consumer_key
        self.consumer_secret = conf.consumer_secret
        self.access_token = conf.access_token
        self.access_token_secret = conf.access_token_secret

    def streamer(self):
        '''Instantiates the listener class we created above and
        also access the stream. stream.filter(track=[]) is where,
        you tell tweepy what keywords to look for.'''
        listen = StdOutListener()
        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        stream = tweepy.Stream(auth, listen)
        stream.filter(track=['BigData', 'MongoDB', 'MySQL'])
        print(stream)
