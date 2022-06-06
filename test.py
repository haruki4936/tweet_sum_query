import tweepy

consumer_key = "c0WcnQMC5Flw01iLXBvLcYP5N"
consumer_secret = "TsAer7d4EosPuLBRdZMxH4ky1lMRwlgJX2vXFCuf3zs5yZw5FJ"
access_token = "1245637260151685122-DNIbUc7gj1gPcv7uoEloPBqhG6Ot6g"
access_token_secret = "MByOoHYTFUCmtoDfi1QN63tOvHdUzwY709R1BNs21cCWe"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
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
