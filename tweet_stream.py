from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from auth import get_api

api = get_api()

keyword_list = ['python', 'java', 'c#','ruby']  #track List

class MyStreamListener(StreamListener):
    def on_data(self, data):
        try:
            with open('tweet_mining.json', 'a') as tweet_file:
                tweet_file.write(data)
                return True
        except BaseException as e:
            print ("Failed on_data: %s" % str(e))
            return True

    def on_error(self, status):
        print(status)
        return True

twitter_stream = Stream(auth, MyStreamListener())
twitter_stream.filter(track=keyword_list)