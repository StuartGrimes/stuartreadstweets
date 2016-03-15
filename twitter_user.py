import tweepy
from auth import get_api

api = get_api()

user = api.get_user('LewisHamilton')

print (user.screen_name)
print (user.followers_count)

for friend in user.friends():
    print
    print(friend.screen_name)
    print(friend.followers_count)

for status in tweepy.Cursor(api.home_timeline).items(10):
    #process a tweet
    print(status.text)
