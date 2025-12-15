from flask import Flask, render_template, jsonify
import threading
import json
import os
from scrape_totals import run as scrape_run

app = Flask(__name__)

# Start scraper in a background thread
threading.Thread(target=scrape_run, daemon=True).start()

@app.route("/")
def index():
    return render_template("thermometer.html")

@app.route("/totals")
def totals():
    if not os.path.exists("totals.json"):
        return jsonify({"goal": 0, "total": 0, "percent": 0})
    with open("totals.json") as f:
        return jsonify(json.load(f))

if __name__ == "__main__":
    # For Railway: port is assigned via environment
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
