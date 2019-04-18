import tweepy
import json
import sys
showType = "all"
def getSysArg():
    #returns the commandline argument, or pass if not given
    try:
        return sys.argv[1]
    except IndexError:
        pass

option = getSysArg()
if option == "--settings":
    print("## TT SETTINGS")
    print("# 1. Show all tweets")
    print("# 2. Show tweets one by one")
    while True:
        choice = input(" Select one ('q' to exit): ")
        if choice == "1":
            showType = "all"
            break
        elif choice == "2":
            showType = "one"
            break
        elif choice == "q":
            print (" You didn't change the settings.")
            break
        else:
            print(" Invalid choice. Enter 'q' to exit.")

try:
    with open("keys.json", "r") as f:
        # Load developer keys from json file
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
    if showType == "one":
        choice = input(" Press any key for next tweet: ")
        if choice == "q": exit(0)