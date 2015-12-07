'''Use this module to collect Tweets via RESTful API or simply
read the data contained within the .csv file obtained from Twitter
analytics.'''
import csv
import tweepy
import json

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
        with open(self.file_name) as f:
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

        return tweets
