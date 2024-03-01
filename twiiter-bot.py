import tweepy

api_key = "0gxAKorpuOmBuwOCcpREztbE6"
api_secret = "OLvKmsHrZVkKn6pkuXujnrQTkqoAsjJQdR4ceXGiQaZHw1x036"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAOFFsgEAAAAAZfaKxGlKNtrzVbv9d37CWY9xrVw%3DVzdBoZxoC2JqGgbPnMpIGgRu060dvDaWMM1Yf5GIGobRafj74K"
access_token = "1253204477521219584-RgY6r4dNZdQOVMOv9xxpsOjdU88skL"
access_token_secret_key = "mJ7SGpM3DXkvkKuBvyiwHkpvMXEkTaPbpfZVX5G38iOgc"

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret_key)
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret_key)
api = tweepy.API(auth)

# client.create_tweet(text = "Hello, this is a bot created by Lakshay2 🤖🤖")
# client.like(tweet_id="1747671410225668366", user_auth=True)
client.retweet(tweet_id="1763468872072458680")