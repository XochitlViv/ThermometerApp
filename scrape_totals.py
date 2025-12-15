import os
import requests

# ----------------------------
# Configuration
# ----------------------------
API_KEY = os.environ.get("GIVESMART_API_KEY")
CAMPAIGN_IDS = ["164386", "168058", "168174"]

API_BASE_URL = "https://fundraise.givesmart.com/api/v2/campaigns/"
GRAPH_BASE_URL = "https://fundraise.givesmart.com/public/campaigns/{}/graph?no_polling=false"

# ----------------------------
# Functions
# ----------------------------
def get_total_from_api(campaign_id):
    """Try to get campaign total from GiveSmart API"""
    if not API_KEY:
        print("API_KEY not set!")
        return None

    url = f"{API_BASE_URL}{campaign_id}"
    headers = {"Authorization": f"Bearer {API_KEY}", "Accept": "application/json"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            # Adjust based on actual API response
            return data.get("total_amount") or data.get("totals", {}).get("raised", 0)
        else:
            print(f"API failed for {campaign_id}: {response.status_code}")
    except Exception as e:
        print(f"Error calling API for {campaign_id}: {e}")
    return None

def get_total_from_graph(campaign_id):
    """Fallback: scrape the /graph URL"""
    url = GRAPH_BASE_URL.format(campaign_id)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data.get("total_amount") or data.get("totals", {}).get("raised", 0)
        else:
            print(f"Graph scraping failed for {campaign_id}: {response.status_code}")
    except Exception as e:
        print(f"Error scraping graph for {campaign_id}: {e}")
    return 0

# ----------------------------
# Main function for app.py
# ----------------------------
def run():
    """Return a dictionary of totals for all campaigns"""
    totals = {}
    for cid in CAMPAIGN_IDS:
        total = get_total_from_api(cid)
        if total is None:
            print(f"Falling back to scraping for campaign {cid}")
            total = get_total_from_graph(cid)
        totals[cid] = total
    return totals

# ----------------------------
# Test run
# ----------------------------
if __name__ == "__main__":
    print(run())
