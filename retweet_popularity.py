import json
import tweepy
from prettytable import PrettyTable
from operator import itemgetter
from auth import get_api

api = get_api()

count = 10
min_retweets = 10 #minimum number of retweets and tweet should get to make it to our list.

query = 'Ireland'

#Get all tweets for the search query

results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

popular_tweets = [status for status in results if status._json['retweet_count'] > min_retweets]

#create a dictionary of tweet text and associated retweets
tweets_tup = tuple([(tweet._json['text'].encode('utf-8'), tweet._json['retweet_count']) for tweet in popular_tweets])

#remove any duplicated
popular_tweets_set = set(tweets_tup)

#sort the tuple entries in desending order
sorted_tweets_tuple = sorted(popular_tweets_set, key=itemgetter(1), reverse=True)[:5]

#Prettify the MoFo!
table = PrettyTable(field_names=['Text', 'Retweet Count'])
for key, val in sorted_tweets_tuple:
    table.add_row(key, val)
    table.max_width['Text'] = 50
    table.align['Text'], table.align['Retweet Count'] = '1', 'r' #align the columns
print table