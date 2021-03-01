import tweepy

consumer_key = ''
consumer_key_secret = ''
access_token = ''
access_token_secret = ''

def get_api():
    auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api
