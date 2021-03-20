from flask import Flask, render_template, redirect
import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
conn = "mongodb://localhost:27017/"
client = pymongo.MongoClient(conn)


app.config 
mongo = PyMongo(app, uri="mongodb://localhost:27017/")

mars = mongo.db.mars
mars_data = scrape_mars.scrape_all()
mars.update({}, mars_data, upsert=True)
# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    from_mongo=client.mars_db.mars.find_one()
    

    # Return template and data
    #return render_template("index.html", vacation=destination_data)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    #Call the scrape_mars.py and store dictionary of results to mongo
    client.mars_db.insert(upsert=True)
    return redirect ('/')

    # Run the scrape function
   # costa_data = scrape_costa.scrape_info()

    # Update the Mongo database using update and upsert=True
   # mongo.db.collection.update({}, costa_data, upsert=True)

    # Redirect back to home page
  #  return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)