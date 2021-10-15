# Use Flask to render a template, redirecting to another url, and creating a URL
from flask import Flask, render_template, redirect, url_for

# Use PyMongo to interact with our Mongo database
from flask_pymongo import PyMongo

# To use the scraping code, we will convert from Jupyter notebook to Python
import scraping

# Set up Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
# Tells Python that our app will connect to Mongo using a URI, a uniform resource identifier similar to a URL
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
# "mongodb://localhost:27017/mars_app" is the URI we'll be using to connect our app to Mongo. This URI is saying that the app can reach Mongo through our localhost server, using port 27017, using a database named "mars_app".
mongo = PyMongo(app)

# Set up Flask route for the main HTML page everyone will view when visiting the web app
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

# Set up Flask route to actually scrape new data using the code we've written
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)

# Tell Flask to run.
if __name__ == "__main__":
   app.run()
   
