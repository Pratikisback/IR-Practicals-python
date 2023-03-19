import snscrape.modules.twitter as sntwitter
import pandas as pd

attributes_container = []

for i, tweet in enumerate(sntwitter.TwitterSearchScraper('from:bhaveshagarwal').get_items()):
    if i > 100:
        break
    attributes_container.append([tweet.date, tweet.likeCount, tweet.rawContent, tweet.sourceLabel])

tweets_df = pd.DataFrame(attributes_container, columns=['Datetime', 'Likes', 'Text', 'Source'])
print(tweets_df)