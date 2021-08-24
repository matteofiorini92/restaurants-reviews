import os
import math
from flask import Flask
if os.path.exists("env.py"):
    import env
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask import Flask, flash, render_template, \
    redirect, request, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_restaurants")
def get_restaurants():
    """
    Renders the main page with the list of restaurants
    If the user is logged in, the username is passed
    as a parameter as buttons such as edit_review are only available
    if the current user is the author of the review
    """
    if session:
        user = mongo.db.users.find_one({"username": session["user"]})
    else:
        user = [{"role": ""}, {"username": ""}]
    restaurants = mongo.db.restaurants.find({"status": "approved"})
    counties = mongo.db.counties.find().sort("name", 1)
    return render_template(
        "get_restaurants.html",
        restaurants=restaurants,
        user=user,
        counties=counties
    )


@app.route("/add_restaurant", methods=["GET", "POST"])
def add_restaurant():
    """
    Renders the page to add a new restaurant
    Only available to registered and logged in users
    Allows post method that adds the new restaurant to the DB
    The list of counties is passed as a parameter to build
    the dropdown menu using jinja2
    """
    if not session:
        # 401 = unauthorized - triggered if the user is not logged in
        return render_template("401.html")
    else:
        if request.method == "POST":
            if request.form.get("has_vegan_options"):
                has_vegan_options = True
            else:
                has_vegan_options = False
            if request.form.get("has_gluten_free_options"):
                has_gluten_free_options = True
            else:
                has_gluten_free_options = False
            restaurant = {  # build the new restaurant with info from form
                "name": request.form.get("name"),
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
                "created_by": session["user"],
                "status": "pending",
                "avg_star_score": "",
                "reviews": []
            }
            mongo.db.restaurants.insert_one(restaurant)
            # add restaurant to the DB
        counties = mongo.db.counties.find().sort("name", 1)
        return render_template("add_restaurant.html", counties=counties)


@app.route("/login_register", methods=["GET", "POST"])
def login_register():
    """
    One function to either login or register
    This is determined based on "type" hidden field of the form
    If attempting to register, checks if user already exists
    The authentication part is taken from
    https://github.com/matteofiorini92/TaskManagerAuth/
    blob/main/08-SearchingWithinTheDatabase/01-text_index_searching/app.py
    """
    if request.method == "POST":
        type = request.form.get("action")  # either "register" or "login"
        if type == "register":
            # check if username already exists
            existing_user = mongo.db.users.find_one(
                {"username": request.form.get("username").lower()})
            if existing_user:
                # if user already exists - error
                flash("Username already exists")
                return redirect(url_for("login_register"))
            else:
                # if user doesn't exist, create new one
                register = {
                    "username": request.form.get("username").lower(),
                    "password": generate_password_hash(
                        request.form.get("password")
                    ),
                    "address_county": request.form.get("address_county").lower(),
                    "role": "user"
                }
                # user added to the DB
                mongo.db.users.insert_one(register)
            # put the new user into 'session' cookie
            session["user"] = request.form.get("username").lower()
            flash("Registration Successful!")
            return redirect(url_for("get_restaurants",
                                    username=session["user"]))
        else:  # type is log_in
            existing_user = mongo.db.users.find_one({"username":
                                                    request.form.
                                                    get("username").lower()})
            # check if username exists in db
            if existing_user:
                if check_password_hash(
                    existing_user["password"],
                    request.form.get("password")
                ):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    return redirect(url_for("get_restaurants",
                                            username=session["user"]))
                else:
                    # invalid password match
                    flash("Incorrect Username and/or Password")
                    return redirect(url_for("login_register"))
            else:
                # username doesn't exist
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login_register"))
    counties = mongo.db.counties.find().sort("name", 1)
    return render_template("login_register.html", counties=counties)


# The following is taken from
# https://stackoverflow.com/questions/14032066/can-flask-have-optional-url-parameters
@app.route("/add_review", defaults={'restaurant_id': None},
           methods=["GET", "POST"])
@app.route("/add_review/<restaurant_id>", methods=["GET", "POST"])
def add_review(restaurant_id):
    """
    Function to add a new review to a restaurant.
    restaurant_id id optional as the user can get to the
    add_review page from two paths:
    1. Use the navbar: no restaurant_id is passed in this case
    2. go from get_restaurants: if a restaurant has 0 reviews,
    there is the option to leave the first one.
    In this case, the restaurant_id is passed so that the restaurant dropdown
    menu is already set to the restaurant the user was looking at
    """
    if not session:
        # 401 = unauthorized - triggered if the user is not logged in
        return render_template("401.html")
    else:  # get list of restaurants from DB to pass as a parameter
        restaurants = mongo.db.restaurants.find(
            {"status": "approved"}
        ).sort(
            "name", 1
        )
        if restaurant_id:  # if restaurant_id exists, find the relevant name
            restaurant = mongo.db.restaurants.find_one(
                {"_id": ObjectId(restaurant_id)},
                {"name": 1, "_id": 0}
            )["name"]
        else:
            restaurant = ""
        if request.method == "POST":
            name = request.form.get("name")
            review = {  # create review to add to the DB
                "_id": ObjectId(),
                "author": session["user"],
                "description": request.form.get("description"),
                "star_score": int(request.form.get("star_score"))
            }
            mongo.db.restaurants.update_one({  # add review to DB
                "name": name}, {
                    "$push": {
                        "reviews": review
                    }
                }
            )
            mongo.db.restaurants.update_one({  # calculate new avg star score
                "name": name}, {
                    "$set": {
                        "avg_star_score": calculate_average_star_score(name)
                    }
                }
            )
        return render_template(
            "add_review.html",
            restaurants=restaurants,
            chosen_restaurant=restaurant
        )


@app.route("/logout")
def logout():
    """
    Logs out the user
    """
    session.pop("user")
    return redirect(url_for('login_register'))


@app.route("/approve_restaurants", methods=["GET", "POST"])
def approve_restaurants():
    """
    This function is only available to admin users
    It allows to change the status of a restaurant from
    "pending" to "approved". Only admin approved restaurants
    can have reviews and are displayed in the get_restaurants page
    """
    if not session:
        # 401 = unauthorized - triggered if the user is not logged in
        return render_template("401.html")
    else:
        user = mongo.db.users.find_one({"username": session["user"]})
        if user["role"] != "admin":
            # 403 = forbidden - triggered if the user is not an admin
            return render_template("403.html")
        else:
            restaurants = mongo.db.restaurants.find({"status": "pending"})
            if request.method == "POST":
                name = request.form.get("name")
                mongo.db.restaurants.update_one({
                    "name": name}, {
                        "$set": {
                            "status": "approved"
                        }
                    }
                )
            return render_template(
                "approve_restaurants.html",
                restaurants=restaurants
            )


@app.route("/my_reviews")
def my_reviews():
    if not session:
        # 401 = unauthorized - triggered if the user is not logged in
        return render_template("401.html")
    else:
        user = session["user"]
        restaurants = mongo.db.restaurants.find({"reviews.author": user})
        reviews = []
        for restaurant in restaurants:
            for review in restaurant["reviews"]:
                if review["author"] == user:
                    reviews.append(
                        {"name": restaurant["name"],
                         "review": review})
        return render_template("my_reviews.html", reviews=reviews)


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    restaurants = mongo.db.restaurants.find(
        {"reviews._id": ObjectId(review_id)})
    for restaurant in restaurants:
        reviews = restaurant["reviews"]
        for review in reviews:
            if review["_id"] == ObjectId(review_id):
                break
    if request.method == "POST":
        query = {
            "name": restaurant["name"],
            "reviews._id": ObjectId(review_id)}
        update_description = {
            "$set": {
                "reviews.$.description": request.form.get("description")}}
        update_star_score = {
            "$set": {
                "reviews.$.star_score": int(request.form.get("star_score"))}}
        mongo.db.restaurants.update_one(query, update_description)
        mongo.db.restaurants.update_one(query, update_star_score)
        mongo.db.restaurants.update_one({
            "name": restaurant["name"]}, {
                "$set": {
                    "avg_star_score": calculate_average_star_score(
                        restaurant["name"]
                    )
                }
            }
        )
        return render_template("my_reviews.html")
    return render_template("edit_review.html",
                           review=review, restaurant=restaurant)


@app.route("/edit_restaurant/<restaurant_id>", methods=["GET", "POST"])
def edit_restaurant(restaurant_id):
    if not session:
        # 401 = unauthorized - triggered if the user is not logged in
        return render_template("401.html")
    else:
        user = mongo.db.users.find_one({"username": session["user"]})
        if user["role"] != "admin":
            # 403 = forbidden - triggered if the user is not an admin
            return render_template("403.html")
        else:
            restaurant = mongo.db.restaurants.find_one(
                {"_id": ObjectId(restaurant_id)}
            )
            counties = mongo.db.counties.find().sort("name", 1)
            if request.method == "POST":
                if request.form.get("has_vegan_options"):
                    has_vegan_options = True
                else:
                    has_vegan_options = False
                if request.form.get("has_gluten_free_options"):
                    has_gluten_free_options = True
                else:
                    has_gluten_free_options = False
                query = {"_id": ObjectId(restaurant_id)}
                update_restaurant = {"$set": {
                    "name": request.form.get("name"),
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
                    "updated_by": session["user"]
                }}
                mongo.db.restaurants.update_one(query, update_restaurant)
                return redirect(url_for("get_restaurants"))
            return render_template(
                "edit_restaurant.html",
                restaurant=restaurant,
                counties=counties
            )


@app.route("/delete_restaurant/<restaurant_id>")
def delete_restaurant(restaurant_id):
    mongo.db.restaurants.delete_one({"_id": ObjectId(restaurant_id)})
    return redirect(url_for("get_restaurants"))


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    restaurant = mongo.db.restaurants.find_one(
        {"reviews._id": ObjectId(review_id)}
    )
    """ https://stackoverflow.com/questions/15641492/mongodb-remove-object-from-array """
    mongo.db.restaurants.update({
        "_id": ObjectId(restaurant["_id"])}, {
            "$pull": {
                "reviews": {
                    "_id": ObjectId(review_id)
                }
            }
        }
    )
    mongo.db.restaurants.update_one({
        "name": restaurant["name"]}, {
            "$set": {
                "avg_star_score": calculate_average_star_score(
                    restaurant["name"]
                )
            }
        }
    )
    return redirect(url_for("my_reviews"))


@app.route("/search", methods=["GET", "POST"])
def search():
    if session:
        user = mongo.db.users.find_one({"username": session["user"]})
    else:
        user = [{"role": ""}, {"username": ""}]
    counties = mongo.db.counties.find().sort("name", 1)
    name = request.form.get("name")
    county = request.form.get("address_county")
    if name:
        if not county:
            all = list(mongo.db.restaurants.find({"$text": {"$search": name}}))
        else:
            all = []
            by_name = list(
                mongo.db.restaurants.find({
                    "$text": {
                        "$search": name
                    }
                })
            )
            for restaurant in by_name:
                if restaurant["address_county"] == county:
                    all.append(restaurant)
    elif county:
        all = list(mongo.db.restaurants.find({"$text": {"$search": county}}))
    else:
        all = mongo.db.restaurants.find().sort("name", 1)
    restaurants = only_approved(all)
    return render_template(
        "get_restaurants.html",
        restaurants=restaurants,
        user=user,
        counties=counties
    )


def only_approved(all):
    restaurants = []
    for item in all:
        if item["status"] == "approved":
            restaurants.append(item)
    return restaurants


""" https://www.geeksforgeeks.org/python-404-error-handling-in-flask/ """


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


def calculate_average_star_score(name):
    restaurant = mongo.db.restaurants.find_one({"name": name})
    reviews = restaurant["reviews"]
    if len(reviews):
        star_scores = []
        for review in reviews:
            star_scores.append(int(review["star_score"]))
        print(star_scores)
        print(sum(star_scores)/len(star_scores))
        average = math.floor(sum(star_scores)/len(star_scores))
    else:
        average = 0
    return average


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
