import os
import requests

# ----------------------------
# Configuration
# ----------------------------
API_KEY = os.environ.get("GIVESMART_API_KEY")
CAMPAIGN_IDS = ["164386", "168058", "168174"]
API_BASE_URL = "https://fundraise.givesmart.com/api/v2/campaigns/"
GRAPH_BASE_URL = "https://fundraise.givesmart.com/public/campaigns/{}/graph?no_polling=false"

# ----------------
