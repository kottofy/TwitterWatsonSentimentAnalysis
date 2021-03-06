﻿from TwitterWatsonSentimentAnalysis.settings import *
import oauth2 as oauth
import json
from app.models import Scored_Tweet

def search_twitter(query):
    CONSUMER_KEY = twitter_credentials['consumer_key']
    CONSUMER_SECRET = twitter_credentials['consumer_secret']
    ACCESS_KEY = twitter_credentials['access_token']
    ACCESS_SECRET = twitter_credentials['access_token_secret']

    consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    access_token = oauth.Token(key=ACCESS_KEY, secret=ACCESS_SECRET)
    client = oauth.Client(consumer, access_token)

    timeline_endpoint = "https://api.twitter.com/1.1/search/tweets.json?q=" + query
    response, data = client.request(timeline_endpoint)

    tweets_json = json.loads(data.decode(encoding='UTF-8'))
    
    tweets = []
    #tweets['statuses'][0]['text']
    try:
        for tweet in tweets_json['statuses']:       
            NewScoredTweet = Scored_Tweet()
            NewScoredTweet.tweet = tweet['text']
            NewScoredTweet.username = tweet['user']['screen_name']
            tweets.append(NewScoredTweet)
    except Exception as e:
        print("Error adding new Scored_Tweet")
        print(e)

    return tweets
