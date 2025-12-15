100B Meals Thermometer – README

Overview

This package displays a live, vertical “mercury” thermometer representing the combined totals of three GiveSmart campaigns.

- Realistic thermometer with glowing bulb and thin neck.
- Totals and percentage are displayed underneath the thermometer.
- Updates automatically every 20 seconds using a web scraper.
- Built with Python, Flask, and BeautifulSoup.

Folder Structure

ThermometerApp/
├─ app.py                  # Flask web server
├─ scrape_totals.py        # Scraper that fetches totals from GiveSmart pages
├─ templates/
│   └─ thermometer.html    # HTML page for the thermometer
├─ static/
│   └─ styles.css          # CSS for styling thermometer
├─ requirements.txt        # Python dependencies
└─ README.txt              # This file

Dependencies

You need Python 3.x installed.

Install dependencies:

    pip install -r requirements.txt

Dependencies include:

- Flask – web server
- requests – fetch GiveSmart pages
- beautifulsoup4 – scrape totals from HTML

How It Works

Scraper (scrape_totals.py)

- Fetches the HTML of three GiveSmart campaign URLs.
- Scrapes the “Raised” amounts from the page.
- Combines the totals and calculates the percentage of the goal.
- Saves the totals to totals.json.
- Runs in a loop, updating every 20 seconds.

Flask Server (app.py)

- Serves the HTML page at http://localhost:8000/.
- Provides a JSON endpoint /totals for current totals.

Front-end (thermometer.html + styles.css)

- Fetches /totals every 20 seconds.
- Updates the mercury level, total raised, and percentage.
- Mercury rises in a realistic bulb + neck thermometer.

How to Run Locally

1. Open a terminal in the project folder.

Start the scraper (keeps updating totals every 20 seconds):

    python scrape_totals.py

2. Open another terminal and start the Flask server:

    python app.py

3. Open a browser:

    http://localhost:8000/

Customizing

- Campaign URLs: Edit URLS list in scrape_totals.py.
- Goal: Change the GOAL variable in scrape_totals.py and thermometer.html.
- Update frequency: Change the time.sleep(20) in scrape_totals.py and setInterval(updateThermometer, 20000) in thermometer.html (value is in milliseconds).

Deploying to the Internet

- Flask can be deployed to platforms like Heroku, PythonAnywhere, or AWS EC2.
- Steps:
  1. Copy the whole folder to the server.
  2. Install dependencies (`pip install -r requirements.txt`).
  3. Run scrape_totals.py in the background (e.g., with nohup or screen).
  4. Run app.py to serve the page.
  5. Make sure ports are open and/or use a reverse proxy like nginx for public access.

Note: This setup will keep the thermometer live and updating every 20 seconds.

