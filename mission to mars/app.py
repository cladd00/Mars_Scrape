import sys
from flask import Flask, render_template, jsonify, redirect
import pymongo
import mars_scrape

sys.setrecursionlimit(2000)
app = Flask(__name__)

client = pymongo.MongoClient()
db = client.mars_db
collection = db.mars_facts

@app.route("/scrape")
def scrape():
    mars = mars_scrape.scrape()
    print("\n\n\n")
    return "Some scrapped data"

@app.route("/")
def home():
    mars = list(db.mars_facts.find())
    print(mars)
    return render_template("index.html",mars = mars)

if __name__ == "_main_":
    app.run(debug=True)


