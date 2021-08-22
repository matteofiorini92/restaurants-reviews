import os
from flask import Flask
if os.path.exists("env.py"):
    import env
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask import Flask, flash, render_template, redirect, request, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_restaurants")
def get_restaurants():
    restaurants = mongo.db.restaurants.find({"status": "approved"})
    return render_template("get_restaurants.html", restaurants=restaurants)


@app.route("/add_restaurant", methods=["GET", "POST"])
def add_restaurant():
    if not session:
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
            restaurant = {
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
                "created_by": "mfiorini",
                "status": "pending",
                "avg_star_score": "",
                "reviews": []
            }
            mongo.db.restaurants.insert_one(restaurant)
        counties = mongo.db.counties.find().sort("name", 1)
        return render_template("add_restaurant.html", counties=counties)


@app.route("/login_register", methods=["GET", "POST"])
def login_register():
    if request.method == "POST":
        type = request.form.get("action")
        if type == "register":
            # check if username already
            existing_user = mongo.db.users.find_one(
                {"username": request.form.get("username").lower()})

            if existing_user:
                flash("Username already exists")
                return redirect(url_for("login_register"))

            register = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(request.
                                                   form.get("password")),
                "address_county": request.form.get("address_county").lower()
            }
            mongo.db.users.insert_one(register)

            # put the new user into 'session' cookie
            session["user"] = request.form.get("username").lower()
            flash("Registration Successful!")
            return redirect(url_for("get_restaurants",
                                    username=session["user"]))

        elif type == "log_in":
            # check if username exists in db
            existing_user = mongo.db.users.find_one({"username":
                                                    request.form.
                                                    get("username").lower()})

            if existing_user:
                # ensure hashed password matches user input
                if check_password_hash(existing_user["password"],
                                       request.form.get("password")):
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


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if not session:
        return render_template("401.html")
    else:
        restaurants = mongo.db.restaurants.find({"status": "approved"}).sort(
                                                "name", 1)
        if request.method == "POST":
            name = request.form.get("name")
            review = {
                "author": session["user"],
                "description": request.form.get("description"),
                "star_score": request.form.get("star_score")
            }
            mongo.db.restaurants.update_one({"name": name},
                                            {"$push": {"reviews": review}})
        return render_template("add_review.html", restaurants=restaurants)


@app.route("/logout")
def logout():
    session.pop("user")
    return redirect(url_for('login_register'))


@app.route("/approve_restaurants", methods=["GET", "POST"])
def approve_restaurants():
    if not session:
        return render_template("401.html")
    elif session["user"] != "mfiorini":
        return render_template("403.html")
    else:
        restaurants = mongo.db.restaurants.find({"status": "pending"})
        if request.method == "POST":
            name = request.form.get("name")
            print(name)
            mongo.db.restaurants.update_one({"name": name},
                                            {"$set": {"status": "approved"}})
        return render_template("approve_restaurants.html",
                               restaurants=restaurants)


@app.route("/my_reviews")
def my_reviews():
    if not session:
        return render_template("401.html")
    else:
        user = session["user"]
        restaurants = mongo.db.restaurants.find({"reviews.author": user})
        reviews = []
        for restaurant in restaurants:
            for review in restaurant["reviews"]:
                if review["author"] == user:
                    reviews.append({"name": restaurant["name"], "review": review})
        print(reviews)
        return render_template("my_reviews.html", reviews=reviews)


""" https://www.geeksforgeeks.org/python-404-error-handling-in-flask/ """


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
