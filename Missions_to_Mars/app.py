# Imports
import sys
from flask import Flask, render_template, jsonify, redirect
import pymongo
import scrape_mars

# Instance
app = Flask(__name__)

# Connect to mongodb
mongodb = PyMongo(app, uri="mongodb://localhost:27017/app")

# App & Scrape Routes
@app.route("/")
def index():
    scrape = mongodb.db.scrapes.find_one()
    return render_template("index.html", scrape=scrape)

@app.route("/scrape")
def scraper():   ## Required
    scrapes = mongodb.db.scrapes
    scrape_data = scrape()
    scrapes.update({}, scrape_data, upsert=True)
    return redirect("/", code=302)

# Assuring execution
if __name__ == "__main__":
    app.run(debug=True)