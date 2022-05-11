import pandas as pd
import snscrape.modules.twitter as sntwitter
import twitterSentimentPredictor as sp

def tweetsFromUser(user):
    tweets = []
    limit = 20

    query = "(from:" + user + ")"

    for tweet in sntwitter.TwitterSearchScraper(query).get_items():
        #pprint(tweet.content)
        #break
        if len(tweets) == limit:
            break;
        else:
            tweets.append([tweet.date, tweet.user.username, tweet.content ])



    df = pd.DataFrame(tweets, columns=['Date', 'Username', 'Tweet'])
    df['Sentiment'] = df['Tweet'].apply(sp.predict_class)
    #print(df["Content"])
    return df