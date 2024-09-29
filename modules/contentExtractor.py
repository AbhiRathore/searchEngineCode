from goose3 import Goose
from newspaper import Article

# Extract content using Goose
def extract_content_goose(url):
    g = Goose()
    article = g.extract(url=url)
    return article.cleaned_text

# Extract content using Newspaper3k
def extract_content_newspaper(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text
