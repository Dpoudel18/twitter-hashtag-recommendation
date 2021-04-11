import tweepy
import pandas as pd
import re
import psycopg2
from tweet_api import *

def build_data(tweet_input):
    api = get_api()
    query = "{} -filter:retweets -filter:mentions".format("hello world")

    tweets = tweepy.Cursor(api.search,tweet_mode='extended',q=query,count=1000,lang="en",since="2017-04-03").items(100)

    df_columns = [[tweet.id, tweet.full_text, tweet.user.screen_name, tweet.created_at] for tweet in tweets]

    df = pd.DataFrame(data=df_columns,
                        columns=["tweet_id","tweet","screen_name","created_at"])
    df['hashtags'] = df['tweet'].apply(lambda x: re.findall(r"#(\w+)", x))
    df['hashtags'] = df['hashtags'].apply(lambda x: " ".join(x))
    df['hashtags'] = df['hashtags'].str.lower()
    df = df[df['hashtags'].map(lambda d: len(d)) > 0]
    df['tweet'] = df['tweet'].map(lambda x: p.clean(x))
    df['tweet'] = df['tweet'].str.lower()
    df = df.replace(',','', regex=True)
    df = df[["tweet_id","tweet","hashtags","screen_name","created_at"]]
    df = df.reset_index(drop=True)
    df.to_csv("tweets.csv", encoding='utf-8', index = False)


    connection = psycopg2.connect(host="bowie.cs.earlham.edu",database="dpoudel18_db",user="dpoudel18",password="***")
    cursor = connection.cursor()
    #sqlStatement = "Select * from campaign_table;"
    #cursor.execute(sqlStatement)
    with open('tweets.csv', 'r') as f:
      next(f) # Skip the header row.
      cursor.copy_from(f, 'tweets', sep=',')
      #cursor.execute(sql_statement)
      connection.commit()
      connection.close()
