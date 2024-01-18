import os
from openai import OpenAI
import dotenv
import retry
import pandas as pd
import requests
from prompts import sys_prompt, prompt
from utils import memoize_to_file
dotenv.load_dotenv("./.env")

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@memoize_to_file()
@retry.retry(tries=3, delay=1)
def evaluate_tweet(prompt):
    try:
        response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[{
            "role": "system",
            "content": sys_prompt 
        },
        {
            "role": "user",
            "content": prompt
        }],
        temperature=0,
        max_tokens=1500)
        text = response.choices[0].message.content
        split_text = text.split("###")
        reasoning = split_text[0].strip() if len(split_text) == 2 else ""
        answer = split_text[-1].strip()
        answer = 'yes' if 'yes' in answer.strip().lower() else 'no'
        return {
            'reasoning': reasoning,
            'answer': answer
        }
    except Exception as e:
        print(prompt)
        print(f"An error occurred while generating the prompt: {e}")
        raise

if __name__ == "__main__":
    file_path = './following_list/following_list.xlsx'
    df = pd.read_excel(file_path)
    twitter_handle_column = df['Twitter Handle']
    positive_prompt_column = df['Positive Prompt']
    negative_prompt_column = df['Negative Prompt']

    nitter_url = "https://nitter.rawbit.ninja"
    results = []  # List to store the results

    for index, twitter_handle in enumerate(twitter_handle_column):
        tag = twitter_handle.strip()  # Ensure the twitter handle is clean
        response = requests.get(f"http://127.0.0.1:5000/user-tweets?tag={tag}")
        if response.status_code == 200:
            tweets = response.json()
            for tweet in tweets:
                link = nitter_url + tweet['link']
                formatted_prompt = prompt.format(
                    positive_prompt=positive_prompt_column[index].lstrip('\'\"'), # Excel cells start with ' or " for bulleted lists
                    negative_prompt=negative_prompt_column[index].lstrip('\'\"'),
                    tweet=f'User: {tag} ' + tweet['content']
                )
                evaluation = evaluate_tweet(formatted_prompt)
                result = {
                    'User': tag,
                    'Tweet': tweet['content'],
                    'Reasoning': evaluation['reasoning'],
                    'Answer': evaluation['answer']
                }
                results.append(result)
                print(f"Added result: {result}")
        else:
            print(f"Failed to get tweets for {tag}, status code: {response.status_code}")

    # Convert the results list to a DataFrame
    df_results = pd.DataFrame(results)

    # Save the DataFrame to a CSV file
    output_file_path = './backend/results.csv'
    df_results.to_csv(output_file_path, index=False)