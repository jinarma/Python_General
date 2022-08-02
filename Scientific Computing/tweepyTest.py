import tweepy
import hidden

auth = tweepy.OAuth1UserHandler(
	hidden.oauth()['consumer_key'],
	hidden.oauth()['consumer_secret'],
	hidden.oauth()['token_key'],
	hidden.oauth()['token_secret']
	)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
	print(tweet.text)
