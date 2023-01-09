import tweepy
import time

TIME_BETWEEN_TWEETS_IN_SECONDS = 60
 
api_key = "UGl1AyPKOZ2CTQQ42SpIASY0F"
api_secret = "iDYMdQCxD8PRCzmWdWsqrZUPsOhQlf9TtoJXEdbgblFEOgKPRm"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAFVmlAEAAAAAyQToiom5hMTT0fXTqMKokWoGV0c%3DXghaUkP75d0K9wh2b0Ujd0IRcMWX24NbAgW86vagIfQaHThIZB"
acess_key = "1612175800744148993-DrNZghwC8rhIP90rldtBwIKpRSNDSl"
acess_secret = "8t0zvcYfUOB10ICxaWXGvSA0eAvL8qLkKb5gN6DDrKU76"
# autentica

client = tweepy.Client(bearer_token, api_key, api_secret, acess_key, acess_secret)

auth = tweepy.OAuthHandler(api_key, api_secret, acess_key, acess_secret)

# api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_notify=True)


class myStream(tweepy.StreamingClient):
    timeToNextTweet = time.time()
    
    def on_tweet(self, tweet):
        print(tweet.text)
        currentTime = time.time()
        if (currentTime >= self.timeToNextTweet):
            print("retwitando")
            try:
                self.timeToNextTweet = currentTime + TIME_BETWEEN_TWEETS_IN_SECONDS
                client.retweet(tweet.id)
            except Exception as error:
                print(error)
        else:
            print("ignorando")
stream = myStream(bearer_token=bearer_token)
rule = tweepy.StreamRule("(tarot OR signos OR tarológa OR astrologia OR baralho cigano OR tarô OR espiritualidade OR lei da atração)(-is:retweet -is:reply lang:pt)")
stream.delete_rules([rule.id for rule in stream.get_rules().data])
stream.add_rules(rule)
stream.filter()
