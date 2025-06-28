import os
import logging
import re
import bleach
from dotenv import load_dotenv
from newspaper import Article
from playwright.sync_api import sync_playwright
from serpapi import GoogleSearch

load_dotenv()
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")
if not SERPAPI_API_KEY:
    raise ValueError("SERPAPI_API_KEY environment variable is not set.")
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


def is_safe_query(query, banned_keywords=None):
    if banned_keywords is None:
        banned_keywords = [
            "hack", "illegal", "bomb", "attack", "weapon", "drugs", "terrorism", "kill",
            "nudity", "pornography"
        ]
    query_lower = query.lower()
    for word in banned_keywords:
        if word in query_lower:
            logger.warning(f"Blocked unsafe query due to banned keyword: {word}")
            return False
    return True

def search_web(query):
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_API_KEY,
        "num": 5,
        "safe": "active"
    }
    try:
        search = GoogleSearch(params)
        results = search.get_dict()
        organic_results = results.get("organic_results", [])
        return [{"title": r.get("title"), "link": r.get("link")} for r in organic_results if r.get("title") and r.get("link")]
    except Exception as e:
        logger.error(f"Error using SerpAPI: {e}")
        return []

def extract_content(url):
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url, timeout=60000)
            page.wait_for_timeout(3000)
            html = page.content()
            browser.close()

            article = Article('')
            article.set_html(html)
            article.parse()
            return sanitize_text(article.text)
    except Exception as e:
        logger.warning(f"Playwright failed to extract content from {url}: {e}")
        return ""

def sanitize_text(text):
    clean_text = bleach.clean(text, tags=[], strip=True)
    patterns = [
        r"ignore previous instructions",
        r"disregard safety filters",
        r"output confidential",
        r"do not mention",
        r"secret",
        r"hidden",
        r"private",
        r"restricted",
        r"classified",
        r"leak",
        r"(nsfw|nude|sex|xxx|porn|erotic|adult)"
    ]
    for pattern in patterns:
        clean_text = re.sub(pattern, "", clean_text, flags=re.IGNORECASE)
    return clean_text.strip()

def decompose_query(query):
    if ',' in query:
        return [q.strip() for q in query.split(',') if q.strip()]
    elif ' and ' in query.lower():
        return [q.strip() for q in query.lower().split('and') if q.strip()]
    else:
        return [query.strip()]
