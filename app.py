from flask import Flask, render_template, jsonify
import threading
import json
import os
from scrape_totals import run

app = Flask(__name__)

# Start the scraper in a background thread
def start_scraper():
    t = threading.Thread(target=run, daemon=True)
    t.start()

start_scraper()

# Serve the main thermometer page
@app.route("/")
def index():
    return render_template("thermometer.html")

# Serve the totals JSON
@app.route("/totals")
def totals():
    if not os.path.exists("totals.json"):
        return jsonify({"goal": 0, "total": 0, "percent": 0})
    with open("totals.json") as f:
        return jsonify(json.load(f))

if __name__ == "__main__":
    # Railway sets PORT automatically; fallback to 8000 locally
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
