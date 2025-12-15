import requests
from bs4 import BeautifulSoup
import json
import time

URLS = [
    "https://fundraise.givesmart.com/public/campaigns/164386/graph?no_polling=false",
    "https://fundraise.givesmart.com/public/campaigns/168058/graph?no_polling=false",
    "https://fundraise.givesmart.com/public/campaigns/168174/graph?no_polling=false"
]

GOAL = 100_000_000_000  # adjust if needed

def fetch_total(url):
    """Scrape the 'Raised' total from a GiveSmart campaign page."""
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")
        amount_div = soup.select_one(".fundraising-total-raised .fundraisingAmount")
        if amount_div:
            text = amount_div.text.replace("$", "").replace(",", "").strip()
            return float(text)
    except Exception as e:
        print(f"Error fetching {url}: {e}")
    return 0

def run():
    """Continuously scrape totals and write to totals.json."""
    while True:
        total = sum(fetch_total(url) for url in URLS)
        percent = (total / GOAL) * 100 if GOAL else 0
        data = {"goal": GOAL, "total": total, "percent": round(percent, 2)}
        with open("totals.json", "w") as f:
            json.dump(data, f)
        time.sleep(20)  # updates every 20 seconds

if __name__ == "__main__":
    run()
