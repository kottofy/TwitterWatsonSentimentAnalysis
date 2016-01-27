from TwitterWatsonSentimentAnalysis.settings import *
import urllib.request
import urllib.parse
import json
import logging

def get_sentiment_analysis(tweets):

    LOG_FILENAME = "log.txt"
    logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)

    #scores = []
    
    api_key = watson_credentials['api_key']
    timeline_endpoint = "http://gateway-a.watsonplatform.net/calls/text/TextGetTextSentiment"

    for tweet in tweets:
        data_dictionary = {
            'apikey' : api_key,
            'outputMode' : 'json',
            'text' : tweet.tweet,
            }

        #print("getting sentiment analysis on: " + text.encode(encoding='UTF-8',errors='strict'))

        try:
            # send POST request to url with encoded data

            #https://docs.python.org/3.4/howto/urllib2.html
            data = urllib.parse.urlencode(data_dictionary)
            data = data.encode('ascii')
            req = urllib.request.Request(timeline_endpoint, data)
            with urllib.request.urlopen(req) as response:
                response_info = response.read()

            #response = urllib.request.Request(timeline_endpoint, data = urllib.parse.urlencode(data_dictionary).encode("utf-8"))
            ##response = urllib.request.urlopen(timeline_endpoint, data = urllib.parse.urlencode(data_dictionary).encode("utf-8"))
            #logging.info(logging.time.clock())
            #logging.info("sent POST request and got response")

            # read the response - gets bytes 
            #response_info = response.read()
            #logging.info("read the response")

            #convert response to json
            readable_info_json = json.loads(response_info.decode(encoding='UTF-8'))
            logging.info( "converted response to json")

            #identify sentiment score!
            score = readable_info_json['docSentiment']['score']
            polarity = readable_info_json['docSentiment']['type']

            #big hurrah!
            #print('got score:' + readable_info_json['docSentiment']['score'])
           
            tweet.score = score
            tweet.polarity = polarity
            #scores.append(score)
            #logging.info(score)

        except Exception as m:
            print('Error in getting Sentiment Analysis score')
            logging.error(m)
            tweet.score = "unable to score"
            pass

    return tweets