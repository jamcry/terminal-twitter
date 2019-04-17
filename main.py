import tweepy
import json

try:
    # Load app keys from json file
    with open("keys.json", "r") as f:
        keys = json.load(f)
except FileNotFoundError:
    print("[!] THE json FILE NOT FOUND!")
    exit(0)

auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
auth.set_access_token(keys['access_token'], keys['access_token_secret'])
api = tweepy.API(auth)

try:
    user = api.me()
except tweepy.TweepError as e:
    print(f"EXCEPTION: {e}")
    exit(0)

print (f" API User Name: {user.name}")
homeFeed = api.home_timeline()
for tweet in homeFeed:
    print("-" * 50)
    print(f" @{tweet.user.name} :")
    print(f"  {tweet.text}")
