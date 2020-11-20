import tweepy

consumer_key = "QDortjbTRjSPOR6P46Iq5BVr4"
consumer_secret = "3q1uxfeTNWxdYhNvxNJyR17EEZyEQpqfJRA6W2qwN6rpWTiynD"
auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)


def search(term, num):
    for searched_item in tweepy.Cursor(api.search, q=term).items(num):
        pass


search("PS5", 10)
