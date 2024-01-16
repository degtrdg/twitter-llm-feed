# Let's write a script to parse the markdown file and extract the tweets into a CSV format
# The CSV will have two columns: username and text

import pandas as pd
import re

# Function to parse the markdown file
def parse_tweets_md(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Split the content by '---'
    tweets = content.split('---\n')

    # Extract username and text for each tweet
    tweet_data = []
    for tweet in tweets:
        # Use regex to find the username and the text
        username_match = re.search(r'@[\w]+', tweet)
        username = username_match.group(0) if username_match else ''
        text = tweet.replace(username, '').strip()

        if username and text:
            tweet_data.append({'username': username, 'text': text})

    return tweet_data

# File path
file_path = '/Users/danielgeorge/Documents/work/ml/small-stuff/twitter-llm-feed/tweets.md'

# Parse the file
tweet_data = parse_tweets_md(file_path)

# Convert to DataFrame and save to CSV
df = pd.DataFrame(tweet_data)
csv_file_path = '/Users/danielgeorge/Documents/work/ml/small-stuff/twitter-llm-feed/tweets.csv'
df.to_csv(csv_file_path, index=False)

csv_file_path