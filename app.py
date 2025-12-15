from flask import Flask, render_template, jsonify
import threading
import json
import os
from scrape_totals import run  # your scraper function

app = Flask(__name__)

def start_scraper():
    """Run the scraper in a daemon thread so it updates totals continuously."""
    scraper_thread = threading.Thread(target=run, daemon=True)
    scraper_thread.start()

# Start scraper when module is imported
start_scraper()

@app.route("/")
def index():
    """Render the thermometer page."""
    return render_template("thermometer.html")

@app.route("/totals")
def totals():
    """Return the current totals as JSON."""
    totals_file = "totals.json"
    if not os.path.exists(totals_file):
        return jsonify({"goal": 0, "total": 0, "percent": 0})

    try:
        with open(totals_file) as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"goal": 0, "total": 0, "percent": 0})

# Only run locally if executed directly
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
