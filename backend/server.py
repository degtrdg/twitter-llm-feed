from flask import Flask, jsonify, request
import asyncio
from scrape import Scraper
import pandas as pd
import dotenv
import requests
from helper import evaluate_tweet
from prompts import prompt
from flask_cors import CORS
from flask_caching import Cache
from utils import memoize_to_file

app = Flask(__name__)
CORS(app)

nitter_url = "https://nitter.rawbit.ninja/"
# chromium_path = "/Users/tk541/Library/Caches/ms-playwright/chromium-1084/chrome-mac/Chromium.app/Contents/MacOS/Chromium"
chromium_path = "/Users/danielgeorge/Library/Caches/ms-playwright/chromium-1091/chrome-mac/Chromium.app/Contents/MacOS/Chromium"
dotenv_path = "./.env"
file_path = './following_list/following_list.xlsx'
output_file_path = './results.csv'
server = 'http://127.0.0.1:5000'


nitter_url = "https://nitter.rawbit.ninja/"
chromium_path = "/Users/danielgeorge/Library/Caches/ms-playwright/chromium-1091/chrome-mac/Chromium.app/Contents/MacOS/Chromium"
dotenv_path = "/Users/danielgeorge/Documents/work/ml/small-stuff/twitter-llm-feed/backend/.env"
file_path = '/Users/danielgeorge/Documents/work/ml/small-stuff/twitter-llm-feed/backend/following_list/following_list.xlsx'
output_file_path = '/Users/danielgeorge/Documents/work/ml/small-stuff/twitter-llm-feed/backend/results.csv'
server = 'http://127.0.0.1:5000'

dotenv.load_dotenv(dotenv_path)

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

# @cache.cached(timeout=300) 
def user_tweets(tag):
    if not tag:
        return jsonify({'error': 'Tag parameter is required'}), 400

    try:
        @memoize_to_file('memoize_timeline.pkl')
        def get_user_timeline(tag):
            # Create a new event loop for this request
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

            scraper = Scraper()
            loop.run_until_complete(scraper.init_browser(nitter_url, chromium_path))
            posts = loop.run_until_complete(scraper.get_user_timeline(tag))
            loop.run_until_complete(scraper.close())

            # Close the loop after completion
            loop.close()

            return posts
        posts = get_user_timeline(tag)
        return posts
    except Exception as e:
        print(tag)
        print(e) 
        return []

@app.route('/unanalyzed-tweets', methods=['GET'])
def unanalyzed_tweets():
    print('im being hit')
    try:
        df = pd.read_excel(file_path)
        twitter_handle_column = df['Twitter Handle']
        results = [] 
        for twitter_handle in twitter_handle_column:
            tag = twitter_handle.strip()  # Ensure the twitter handle is clean
            tweets = user_tweets(tag)
            for tweet in tweets:
                link = tweet['link']
                result = {
                    'Link': link,
                }
                results.append(result)
        return jsonify(results) 

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500

@app.route('/evaluate-tweets', methods=['GET'])
def evaluate_tweets():
    try:
        df = pd.read_excel(file_path)
        twitter_handle_column = df['Twitter Handle']
        positive_prompt_column = df['Positive Prompt']
        negative_prompt_column = df['Negative Prompt']

        results = [] 

        for index, twitter_handle in enumerate(twitter_handle_column):
            tag = twitter_handle.strip()  # Ensure the twitter handle is clean
            tweets = user_tweets(tag)
            for tweet in tweets:
                link = tweet['link']
                formatted_prompt = prompt.format(
                    positive_prompt=positive_prompt_column[index].lstrip('\'\"'), # Cells start with ' or " for bulleted lists on my excel sheet
                    negative_prompt=negative_prompt_column[index].lstrip('\'\"'),
                    tweet=f'User: {tag} ' + tweet['content']
                )
                evaluation = evaluate_tweet(formatted_prompt)
                result = {
                    'Prompt': formatted_prompt,
                    'Link': link,
                    'Reasoning': evaluation['reasoning'],
                    'Answer': evaluation['answer']
                }
                results.append(result)
        
        # Convert the results list to a DataFrame
        df_results = pd.DataFrame(results)

        # Save the DataFrame to a CSV file
        # output_file_path = './backend/results.csv' This was the bug
        output_file_path = '/Users/danielgeorge/Documents/work/ml/small-stuff/twitter-llm-feed/backend/results.csv'
        df_results.to_csv(output_file_path, index=False)

        return jsonify(results) 

    except Exception as e:
        print(e)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()