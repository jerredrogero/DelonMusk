import robin_stocks as r
import pyotp
import pprint
import tweepy
import secrets

#Robinhood Login
try:
    login = r.login(secrets.RH_User, secrets.RH_Pass, mfa_code=totp)
except:
    login = r.login(secrets.RH_User, secrets.RH_Pass)

auth = tweepy.OAuthHandler(secrets.API_Key, secrets.API_Secret_Key)
auth.set_access_token(secrets.Access_Token, secrets.Token_Secret)
api = tweepy.API(auth)

#Filters out mentions and RTs
def from_creator(status):
    if hasattr(status, 'retweeted_status'):
        return False
    elif status.in_reply_to_status_id != None:
        return False
    elif status.in_reply_to_screen_name != None:
        return False
    elif status.in_reply_to_user_id != None:
        return False
    else:
        return True

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        if from_creator(status):
            tweet = status.text
            if "doge" in tweet:
                print(r.order_buy_crypto_by_price('DOGE' , 20))
            return True
        return True


    def on_error(self, status_code):
        if status_code == 420:
            print("Error 420")
            #returning False in on_error disconnects the stream
            return False
    
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)   
myStream.filter(follow=['44196397'])             









