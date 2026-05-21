import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:

    tweet_id = []

    for i in range(len(tweets["tweet_id"])):

        if(len(tweets["content"][i]) > 15):
            tweet_id.append(tweets["tweet_id"][i])

    data = {
        "tweet_id" : tweet_id
    }

    return pd.DataFrame(data)
