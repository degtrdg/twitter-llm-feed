from flask import Flask, jsonify, request
import asyncio
from scrape import Scraper

app = Flask(__name__)

nitter_url = "https://nitter.rawbit.ninja/"
chromium_path = "/Users/tk541/Library/Caches/ms-playwright/chromium-1084/chrome-mac/Chromium.app/Contents/MacOS/Chromium"

@app.route('/user-tweets', methods=['GET'])
def user_tweets():
    tag = request.args.get('tag')
    if not tag:
        return jsonify({'error': 'Tag parameter is required'}), 400

    try:
        # Create a new event loop for this request
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        scraper = Scraper()
        loop.run_until_complete(scraper.init_browser(nitter_url, chromium_path))
        posts = loop.run_until_complete(scraper.get_user_timeline(tag))
        loop.run_until_complete(scraper.close())

        # Close the loop after completion
        loop.close()
        
        return jsonify(posts)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
