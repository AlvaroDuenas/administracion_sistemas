import tweepy
import webbrowser
import time

consumer_key = "QDortjbTRjSPOR6P46Iq5BVr4"
consumer_secret = "3q1uxfeTNWxdYhNvxNJyR17EEZyEQpqfJRA6W2qwN6rpWTiynD"
callback_uri = 'oob'  # https://cfe.sh/twitter/callback
auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_uri)
redirect_url = auth.get_authorization_url()
print(redirect_url)
webbrowser.open(redirect_url)
user_pint_input = input("What's the input value")
print(user_pint_input)
auth.get_access_token(user_pint_input)
api = tweepy.api(auth)
