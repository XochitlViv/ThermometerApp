import time
import json
import requests
from bs4 import BeautifulSoup

URLS = [
    "https://fundraise.givesmart.com/public/campaigns/164386/graph?no_polling=false",
    "https://fundraise.givesmart.com/public/campaigns/168058/graph?no_polling=false",
    "https://fundraise.givesmart.com/public/campaigns/168174/graph?no_polling=false"
]

GOAL = 100_000_000_000  # 100B

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def parse_money(text):
    return int(text.replace("$", "").replace(",", "").strip())

def scrape_once():
    total = 0

    for url in URLS:
        try:
            r = requests.get(url, headers=HEADERS, timeout=15)
            soup = BeautifulSoup(r.text, "html.parser")

            raised = soup.select_one(
                ".fundraising-total-raised .fundraisingAmount"
            )

            if raised:
                total += parse_money(raised.text)

        except Exception as e:
            print(f"Error scraping {url}: {e}")

    percent = round((total / GOAL) * 100, 4)

    data = {
        "goal": GOAL,
        "total": total,
        "percent": percent
    }

    with open("totals.json", "w") as f:
        json.dump(data, f)

    print("Updated totals:", data)

def run():
    while True:
        scrape_once()
        time.sleep(20)

if __name__ == "__main__":
    run()
