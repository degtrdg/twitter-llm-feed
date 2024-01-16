import pandas as pd
from openai import OpenAI

client = OpenAI(api_key='your_api_key')

# Load the CSV file
df = pd.read_csv('path_to_your_tweets.csv')

# Set your OpenAI API key

# Function to evaluate a tweet
def evaluate_tweet(tweet, prompt):
    try:
        response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": prompt},
                  {"role": "user", "content": tweet}])
        return 'Yes' if 'yes' in response.choices[0].message.content.lower() else 'No'
    except Exception as e:
        print(f"Error: {e}")
        return 'No'

# Processing each tweet
for index, row in df.iterrows():
    user_prompt = user_preference_prompts['user1']  # Change as per the user
    result = evaluate_tweet(row['text'], user_prompt)
    df.at[index, 'worth_time'] = result

# Save the updated DataFrame
df.to_csv('path_to_updated_tweets.csv', index=False)
