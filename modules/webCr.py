import requests
from bs4 import BeautifulSoup
import asyncio
import aiohttp
from goose3 import Goose

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

# Function to asynchronously fetch the content of a single URL
async def fetch_page_content(session, url):
    try:
        async with session.get(url) as response:
            if response.status == 200:
                html = await response.text()
                return html
            else:
                print(f"Failed to fetch {url} with status: {response.status}")
                return None
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

# Function to asynchronously crawl multiple URLs
async def fetch_all_pages(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_page_content(session, url) for url in urls]
        html_pages = await asyncio.gather(*tasks)
        return html_pages

# Function to extract content using Goose from multiple URLs
def extract_content_goose(html_content):
    goose = Goose()
    article = goose.extract(raw_html=html_content)
    return article.cleaned_text if article else None

# Wrapper to crawl URLs asynchronously and extract content
async def crawl_and_extract_content(urls):
    html_pages = await fetch_all_pages(urls)
    
    # Extract content for each HTML page using Goose
    extracted_contents = [extract_content_goose(html) for html in html_pages if html]
    return extracted_contents