import requests
from bs4 import BeautifulSoup
import asyncio
import aiohttp

# Synchronous request for a single page
def crawl_page(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to access {url}")
        return None

# Asynchronous request for multiple pages
async def fetch(url, session):
    headers = {'User-Agent': 'Mozilla/5.0'}
    async with session.get(url, headers=headers) as response:
        return await response.text()

async def fetch_all(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(url, session) for url in urls]
        return await asyncio.gather(*tasks)
