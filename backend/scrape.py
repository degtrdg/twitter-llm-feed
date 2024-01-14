import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

class Scraper:
    async def init_browser(self, nitter_url: str, chromium_path: str = None):
        self.playwright = await async_playwright().start()
        args = {
            "executable_path": chromium_path,
            "headless": True,
            "args": [
                "--user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:120.0) Gecko/20100101 Firefox/120.0",
                "--disable-blink-features=AutomationControlled",
                "--window-size=1920,1080"
            ]
        }
        
        if not chromium_path:
            args.pop("executable_path")

        self.browser = await self.playwright.chromium.launch(**args)
        self.page = await self.browser.new_page()
        await self.page.set_viewport_size({"width": 1920, "height": 1080})
    
        await self.page.evaluate("""
        navigator.webdriver = undefined;
        navigator.languages = ['en-US', 'en'];
        navigator.plugins = [1, 2, 3, 4, 5];
        """)

        self.nitter_url = nitter_url

    async def get_user_timeline(self, tag):
        await self.page.goto(self.nitter_url + tag)
        content = await self.page.content()
        soup = BeautifulSoup(content, 'html.parser')

        posts = []
        for item in soup.select('.timeline-item'):
            post = {
                'link': item.select_one('.tweet-link')['href'],
                'date': item.select_one('.tweet-date a').get_text(),
                'content': item.select_one('.tweet-content').get_text(strip=True),
                'attachments': [self.nitter_url + img['src'] for img in item.select('.attachments img')]
            }
            posts.append(post)

        return posts

    async def close(self):
        await self.browser.close()
        await self.playwright.stop()

async def main(tag: str):
    scraper = Scraper()
    await scraper.init_browser(
        "https://nitter.rawbit.ninja/", 
        "/Users/tk541/Library/Caches/ms-playwright/chromium-1084/chrome-mac/Chromium.app/Contents/MacOS/Chromium"
    )
    posts = await scraper.get_user_timeline(tag)
    print(posts)
    await scraper.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main("elonmusk"))
