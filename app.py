import os
from flask import Flask
if os.path.exists("env.py"):
    import env
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask import Flask, flash, render_template, redirect, request, session, url_for

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

@app.route("/")
@app.route("/get_restaurants")
def get_restaurants():
    restaurants = mongo.db.restaurants.find()
    return render_template("restaurants.html", restaurants=restaurants)


@app.route("/add_restaurant", methods=["GET", "POST"])
def add_restaurant():
    if request.method == "POST":
        has_vegan_options = True if request.form.get("has_vegan_options") else False
        has_gluten_free_options = True if request.form.get("has_gluten_free_options") else False
        restaurant = {
            "restaurant_name": request.form.get("restaurant_name"),
            "address_street": request.form.get("address_street"),
            "address_city": request.form.get("address_city"),
            "address_county": request.form.get("address_county"),
            "tel": request.form.get("tel"),
            "email_address": request.form.get("email_address"),
            "website": request.form.get("website"),
            "fb_page": request.form.get("fb_page"),
            "ig_page": request.form.get("ig_page"),
            "has_vegan_options": has_vegan_options,
            "has_gluten_free_options": has_gluten_free_options,
            "pricing_score": request.form.get("pricing_score"),
            "created_by": "mfiorini",
            "status": "pending"
        }
        mongo.db.restaurants.insert_one(restaurant)
    counties = mongo.db.counties.find().sort("name", 1)
    return render_template("add_restaurant.html", counties=counties)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)