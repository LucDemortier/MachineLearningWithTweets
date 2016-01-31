import json
import tweepy
from textblob import TextBlob
from pymongo import MongoClient

# import twitter keys and tokens
import cnfg
config = cnfg.load(".twitter_config")

# create instance of MongoClient
client = MongoClient()
db     = client.dsbc
yoga   = db.yoga
tweet_number = 0

class TweetStreamListener(tweepy.StreamListener):

    # on success
    def on_data(self, data):

        # increment tweet number
        global tweet_number
        tweet_number += 1

        # decode json
        dict_data = json.loads(data)

        # pass tweet into TextBlob
        tweet = TextBlob(dict_data["text"])

        # determine if sentiment is positive, negative, or neutral
        if tweet.sentiment.polarity < 0:
            sentiment = "negative"
        elif tweet.sentiment.polarity == 0:
            sentiment = "neutral"
        else:
            sentiment = "positive"

        # output sentiment polarity and sentiment
        print tweet_number, tweet.sentiment.polarity, sentiment

        # add text and sentiment info to Mongo DB
        summary = {}
        summary["author"] = dict_data["user"]["screen_name"]
        summary["time"] = dict_data["created_at"]
        summary["location"] = dict_data["place"]
        summary["favorite_count"] = dict_data["favorite_count"]
        summary["retweet_count"] = dict_data["retweet_count"]
        summary["message"] = dict_data["text"]
        summary["polarity"] = tweet.sentiment.polarity
        summary["subjectivity"] = tweet.sentiment.subjectivity
        summary["sentiment"] = sentiment
        yoga.insert(summary)

        return True

    # on failure
    def on_error(self, status):
        print status

if __name__ == '__main__':

    # create instance of the tweepy tweet stream listener
    listener = TweetStreamListener()

    # set twitter keys/tokens
    auth = tweepy.OAuthHandler(config['consumer_key'], 
                               config['consumer_secret'])
    auth.set_access_token(config['access_token'], 
                          config['access_token_secret'])

    # create instance of the tweepy stream
    stream = tweepy.Stream(auth, listener)

    # search twitter for "yoga" keyword
    stream.filter(track=['yoga'],languages = ['en'])