import tweepy

from tweepy import OAuthHandler
import codecs
from string import punctuation

class tweet():
    ckey = 'fPWFGLE8TUJuvNI85Un14BD9W'      #cKey, cSecret, aToken, aSecret for the twitter access
    csecret = 'iXjrA1CyjzcEGWaioMyvze2hR73Ipddy71iKJC1ktphjgZCu0H'

    atoken = '3318507648-RRuZ652ct0R9IzzCmvBrY8DqhtQC4HY6s6crjYm'
    asecret = 'NtoRS98WljTFiZd1glAFCjJc3IPT6AyBApwRkPoQqlviV'

    # OAuth Authentication
    auth = OAuthHandler(ckey, csecret)      #authentication
    auth.set_access_token(atoken, asecret)

    #Twitter API wrapper
    api = tweepy.API(auth)

    #Load the list of positive and negative words
    #These will be used in the analysis of the tweets
    pos_sent = open("positive_words.txt").read()    #read positive words
    positive_words = pos_sent.split('\n')

    neg_sent = open('negative_words.txt').read()    #read negative words
    negative_words = neg_sent.split('\n')

    def tweetSearch(self, celebrityName):   #searching celebrity name on the web
        outFile = codecs.open("testTweets.txt", 'w', "utf-8")
        results = self.api.search(q=celebrityName, lang="en", locale="en", count=100)   #limiting the search results to 100

        for result in results:
            outFile.write(result.txt + '\n') #writing the result in an result.txt
        outFile.close()
    def posNegCount(self, tweet):

        pos = 0
        neg = 0

        for p in list(punctuation):
            tweet = tweet.replace(p, '')

        tweet = tweet.lower() #.encode('utf8') , converting into a lowercase string.
        words = tweet.split('')
        word_count = len(words)

        for word in words:      #counting the negative words and the positive words.
            if word in self.positive_words:
                pos = pos + 1
            elif word in self.negative_words:
                neg = neg + 1
        return pos, neg

    def tweetSentimentAnalysis(self):
        tweets = codecs.open("testTweets.txt", 'r', "utf-8").read()
        tweets_list = tweets.split('\n')

        positive_counter = 0
        negative_counter = 0

        for tweet in tweets_list:
            if(len(tweet)):
                p,n = self.posNegCount(tweet)
                positive_counter += p
                negative_counter += n

        if positive_counter > negative_counter:
            return "positive"

        elif positive_counter < negative_counter:
            return "negative"

        else:
            return "Neutral"
