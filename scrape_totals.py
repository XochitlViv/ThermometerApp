import requests
from bs4 import BeautifulSoup
import json
import time

# Campaign URLs
URLS = [
    "https://fundraise.givesmart.com/public/campaigns/164386/graph?no_polling=false",
    "https://fundraise.givesmart.com/public/campaigns/168058/graph?no_polling=false",
    "https://fundraise.givesmart.com/public/campaigns/168174/graph?no_polling=false"
]

# Goal for the combined thermometer
GOAL = 100_000_000_000

# Output JSON file
OUTPUT_FILE = "totals.json"

# Update interval in seconds
UPDATE_INTERVAL = 20

def scrape_total(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        total_div = soup.find("div", class_="fundraising-total-raised")
        if total_div:
            amount_text = total_div.find("div", class_="fundraisingAmount").get_text(strip=True)
            # Remove $ and commas
            amount = float(amount_text.replace("$","").replace(",",""))
            return amount
    except Exception as e:
        print(f"Error scraping {url}: {e}")
    return 0

def run():
    while True:
        total = sum(scrape_total(url) for url in URLS)
        percent = (total / GOAL) * 100 if GOAL else 0
        data = {
            "goal": GOAL,
            "total": total,
            "percent": round(percent, 2)
        }
        try:
            with open(OUTPUT_FILE, "w") as f:
                json.dump(data, f)
        except Exception as e:
            print(f"Error writing {OUTPUT_FILE}: {e}")
        time.sleep(UPDATE_INTERVAL)

if __name__ == "__main__":
    run()
