import tweepy
import api_key

auth = tweepy.OAuthHandler(api_key.consumer_key, api_key.consumer_secret)
auth.set_access_token(api_key.access_token, api_key.access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit = True)

#-------------------------------------------------------------------------
accounts = input().rstrip().split(",")
tweet_sum = 0
for account in accounts:
    user = api.get_user(screen_name = account, include_entities = True)
    tweet_num = user.statuses_count
    print(user.screen_name + ": ", end = "")
    print(user.name + ": ", end = "")
    print(tweet_num)
    tweet_sum += tweet_num

print(tweet_sum)
