# 1. import Flask
from flask import Flask, render_template, jsonify, redirect
from flask_pymongo import PyMongo
import scrape_mars as mars_scraper

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

mongo = PyMongo(app)


@app.route("/")
def index():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)


@app.route("/scrape")
def scrape():
    print("start to scrape web...")
    mars = mongo.db.mars
    mars_data = mars_scraper.scrape()

    mars.update(
        {},
        mars_data,
        upsert=True
    )

    return redirect("http://localhost:5000/", code=302)


if __name__ == "__main__":
    app.run(debug=True)