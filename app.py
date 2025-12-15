from flask import Flask, render_template, jsonify
from scrape_totals import run
import os
import threading
import time

app = Flask(__name__)
totals_cache = {}

def update_totals():
    """Background thread: update totals every 20 seconds"""
    global totals_cache
    while True:
        totals_cache = run()
        time.sleep(20)

@app.route("/")
def index():
    """Serve thermometer HTML"""
    return render_template("thermometer.html")

@app.route("/totals")
def totals():
    """Return JSON of current campaign totals"""
    return jsonify(totals_cache)

if __name__ == "__main__":
    # Start background thread
    thread = threading.Thread(target=update_totals, daemon=True)
    thread.start()
    
    # Run Flask app on Railway port
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
