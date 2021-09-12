# FoodReview

![home page all screen sizes](https://raw.githubusercontent.com/matteofiorini92/restaurants-reviews/master/static/img/wireframes/food-review-responsive.png)

[Link to deployed website](https://restaurants-reviews-mf.herokuapp.com/)

FoodReview is a website where users can leave reviews on Irish restaurants.
All visitors can read these reviews, but only members can add or edit new reviews.

# Table Of Contents

-   [User Experience](#user-experience)
-   [Features](#features)
-   [Technologies Used](#technologies-used)
-   [Testing](#testing)
-   [Deployment](#deployment)
-   [Credits](#credits)

## User Experience

-   [User Stories](#user-stories)
-   [The Scope Plane](#the-Scope-plane)
-   [The Structure Plane](#the-structure-plane)
-   [Wireframes](#wireframes)
-   [The Surface Plane](#the-surface-plane)


### User Stories

The purpose of the website is for users to read about previous experiences other people had, at restaurants they may want to go to.
Restaurants will have all the relevant contact details, a pricing score (based on the price of an average meal), a star score (based on the average of their reviews) and badges if they are vegan-friendly and have gluten-free options.

- User story 1: As a visitor, I want to check a restaurant's reviews before deciding to book
- User story 2: As a user, I want to leave a review of a restaurant that's already present in the list, that I've recently eaten at
- User story 3: As a user, I want to add a new restaurant to the list, so that myself and other users can leave our reviews
- User story 4: As a user, I want to be able to manage my previous reviews. This includes editing or deleting them.
- User story 5: As an admin user, I want to have control over new restaurants that are added. Since restaurants' details are objective, they need to be reviewed and approved by me
- User story 6: As an admin user, I want to be able to delete or edit restaurants once they've been approved. 
- User story 7: As an admin user, I want to be able to delete unfair or spam reviews. I don't want to be able to edit a review, as the review's author is the only one who should be allowed to edit it.
- User story 8: As a visitor, I want to be able to register on the website to add new restaurants and reviews
- User story 9: As a user, I want to be able to log-in and log-out of the website

### The Scope Plane

Users want to be able to rate their experiences when eating out, to leave the reviews for other people to know how a particular restaurant was, what was their favourite dish, what they didn't enjoy.
At the same time, people want to know what to expect when they go to a new place, they rely on other users' experiences to know whether a place is nice or not, if a low-cost small diner has better food than a fancy restaurant.

### The Structure Plane

The website will have the following structure for visitors (not users):
- Restaurants: lists all restaurants approved by an admin, with their contact details and their reviews
- Log-in/Register: allows the visitor to either log-in or register as a new user

On top of these pages, a user will have access to:
- My Reviews: collections of all reviews left by the user. From here, they will also be able to edit or delete these reviews
- Add Review: from here, a user can add a new review for a restaurant approved by an admin
- Add Restaurant: from here, a user can request to add a new restaurant to the list. This request will need to be approved by an admin user.
- Log-out: used to simply log-out of the current session
- Restaurants: in addition to what a visitor sees here, a user will also have the option to edit/delete their reviews from this page too

An admin user will also have access to:
- Approve Restaurants: collection of all restaurants added by users but not yet approved by an admin
- Restaurants: only admin users will see edit/delete buttons for each restaurants in this page, as well as a delete button for each review.

### Wireframes

- [Add Restaurant](https://raw.githubusercontent.com/matteofiorini92/restaurants-reviews/master/static/img/wireframes/add_restaurant.png)
- [Add Review](https://raw.githubusercontent.com/matteofiorini92/restaurants-reviews/master/static/img/wireframes/add_review.png)
- [Approve Restaurants](https://raw.githubusercontent.com/matteofiorini92/restaurants-reviews/master/static/img/wireframes/approve_restaurants.png)
- [Edit Review](https://raw.githubusercontent.com/matteofiorini92/restaurants-reviews/master/static/img/wireframes/edit_review.png)
- [My Reviews](https://raw.githubusercontent.com/matteofiorini92/restaurants-reviews/master/static/img/wireframes/my_reviews.png)
- [Restaurants](https://raw.githubusercontent.com/matteofiorini92/restaurants-reviews/master/static/img/wireframes/restaurants.png)

### The Surface Plane

The color palette of the website will be white - dark orange - teal

## Features

-   [Existing Features](#existing-features)
-   [Features Left to Implement](#features-left-to-implement)
 
### Existing Features

- User story 1: As a visitor, I want to check a restaurant's reviews before deciding to book
    - Feature 1 - Search restaurants by name and location
    - Feature 2 - Read reviews and access contact details of restaurants
- User story 2: As a user, I want to leave a review of a restaurant that's already present in the list, that I've recently eaten at
    - Feature 3 - Add a new review
- User story 3: As a user, I want to add a new restaurant to the list, so that myself and other users can leave our reviews
    - Feature 4 - Request to add a new restaurant
- User story 4: As a user, I want to be able to manage my previous reviews. This includes editing or deleting them.
    - Feature 5 - Edit an existing review
    - Feature 6 - Delete a review
- User story 5: As an admin user, I want to have control over new restaurants that are added. Since restaurants' details are objective, they need to be reviewed and approved by me
    - Feature 7 - Approve restaurants (admin only)
- User story 6: As an admin user, I want to be able to delete or edit restaurants once they've been approved.
    - Feature 8 - Edit an existing restaurant (admin only)
    - Feature 9 - Delete a restaurant (admin only)
- User story 7: As an admin user, I want to be able to delete unfair or spam reviews. I don't want to be able to edit a review, as the review's author is the only one who should be allowed to edit it.
    - Feature 5 - Delete a review
- User story 8: As a visitor, I want to be able to register on the website to add new restaurants and reviews
- User story 9: As a user, I want to be able to log-in and log-out of the website
    - Feature 10 - Register, log-in, log-out

### Features Left to Implement
- Filter restaurants by "has_vegan_options" or "has_gluten_free_options"

## Technologies Used

### Languages and Frameworks

- HTML for the basic structure of the website
- CSS for some custom styling of the website
- [Materialize](https://materializecss.com/) to use the grid system, pre-formatted buttons, colors and panel cards
- [JQuery](https://code.jquery.com/) to initiate some interactive elements of the materialize framework
- [Jinja](jinja.palletsprojects.com) to reuse common elements of different pages with templates
- [Flask](https://flask.palletsprojects.com/) to write the python part of the project

### Applications

- [MongoDB](https://www.mongodb.com/) as DB to store all data used by the application
- [Gitpod](https://gitpod.io/) to develop the project
- [GitHub](https://github.com/) for version control
- [Heroku](https://www.heroku.com) to deploy the project
- [Balsamiq](https://balsamiq.com/) for the wireframes of this readme.md file
- [Canva](https://www.canva.com/) to create the logo image
- [IconFinder](https://www.iconfinder.com/) for the vegan friendly and gluten free badges

## Testing

The application functionalities were tested in three different scenarios:

1. Visitor
    - Able to view restaurants
        - tested the search bar and it worked as expected when filtering by name, county and both
        - all buttons (search, reset, read reviews) worked as expected
    - Able to login or register
    - Not able to perform any other action
    - When trying to access a non-existing page, was prompted with the 404 template (with working link to home page)
    - When trying to access an existing page that required to be logged-in, was prompted the 401 template (with working link to login page)

2. User
    - Able to view restaurants
        - tested the search bar and it worked as expected when filtering by name, county and both
        - all buttons (search, reset, read reviews, edit for own reviews) worked as expected
    - Able to add reviews (tested submit and cancel buttons)
    - Able to edit and delete own reviews (tested edit, delete and cancel buttons): note on editing reviews, user is only able to edit description and star scoring. If they want to edit the restaurant the review was for, this will need to be deleted and re-added.
    - Adding, editing and deleting a review updates the relative restaurant's star scoring as expected
    - Able to request to add a new restaurant
    - Able to log out
    - When trying to access a non-existing page, was prompted with the 404 template (with working link to home page)
    - When trying to access an existing page that required to admin access, was prompted the 403 template (with working link to home page)
    - Tested confirm and cancel buttons of all modals, working as expected

3. Admin
    - Able to view restaurants
        - tested the search bar and it worked as expected when filtering by name, county and both
        - all buttons (search, reset, read reviews, edit for own reviews) worked as expected
    - Able to edit and delete restaurants (tested all submit and cancel buttons)
    - Able to add reviews (tested submit and cancel buttons)
    - Able to edit and delete own reviews (tested edit, delete and cancel buttons): note on editing reviews, user is only able to edit description and star scoring. If they want to edit the restaurant the review was for, this will need to be deleted and re-added.
    - Adding, editing and deleting a review updates the relative restaurant's star scoring as expected
    - Able to request to add a new restaurant
    - Able to approve restaurants
    - Able to log out
    - When trying to access a non-existing page, was prompted with the 404 template (with working link to home page)
    - Tested confirm and cancel buttons of all modals, working as expected

I used the following validators to check my HTML, CSS and JavaScript code:

[HTML Validator](https://validator.w3.org/)
- [Restaurants](https://validator.w3.org/nu/?doc=http%3A%2F%2Frestaurants-reviews-mf.herokuapp.com%2Fget_restaurants)
- [Login-Register](https://validator.w3.org/nu/?doc=http%3A%2F%2Frestaurants-reviews-mf.herokuapp.com%2Flogin_register)
- [My Reviews](https://validator.w3.org/nu/?doc=http%3A%2F%2Frestaurants-reviews-mf.herokuapp.com%2Fmy_reviews)
- [Add Review](https://validator.w3.org/nu/?doc=http%3A%2F%2Frestaurants-reviews-mf.herokuapp.com%2Fadd_review)
- [Add Restaurant](https://validator.w3.org/nu/?doc=http%3A%2F%2Frestaurants-reviews-mf.herokuapp.com%2Fadd_restaurant)
- [Approve Restaurants](https://validator.w3.org/nu/?doc=http%3A%2F%2Frestaurants-reviews-mf.herokuapp.com%2Fapprove_restaurants)

[CSS Validator](https://jigsaw.w3.org/css-validator/)

<p>
    <a href="https://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="https://jigsaw.w3.org/css-validator/images/vcss-blue"
            alt="Valid CSS!" />
    </a>
</p>

[JS Validator](https://jshint.com/)

[PEP8 Validator](http://pep8online.com/)

### Bugs

- Email address wasn't pulling in edit_restaurant function: fixed by correcting the variable name used
- Incorrect number of golden stars displayed in edit_review page: fixed by adjusting parameters in jinja for loop
- my_reviews function not working correctly: was querying db with user[name] instead of user[username]
- HTML validator raised error for a href tel attribute of restaurant_list page because phone numbers contained whitespaces: removed whitespaces with replace jinja method
- Cancel buttons working as submitfix: found reason for that [here](https://stackoverflow.com/a/18407896/16735714) - was using type=cancel 
- When logged as normal users, Edit and delete buttons weren't displayed in get_restaruants page for reviews written by that user: corrected logic in if statement

## Deployment

[Link to deployed website](https://restaurants-reviews-mf.herokuapp.com/)

This project was developed using GitPod, pushed to GitHub and deployed using Heroku.

To deploy to Heroku from the GitHub repository, the following steps were taken:

1. Go to heroku.com and log in
2. Click on "Create new app"
3. Go to Deploy > Deployment method > Github
4. Go to Settings > Config vars and add variables
8. Git add / commit / push Procfile and requirements.txt files
9. Enable automatic deployments from Heroku
10. Click on Deploy branch

### Hot to run this project locally

To clone this project into Gitpod you will need:

1. A Github account
2. Use the Chrome browser

Then follow these steps:

1. Install the Gitpod Browser Extension for Chrome
2. After installation, restart the browser
3. Log into Gitpod with your gitpod account
4. Navigate to the Project GitHub repository
5. Click the green GitPod button in the top right corner of the repository
6. This will trigger a new gitpod workspace to be created

To work on the project code within a local IDE such as VSCode, Pycharm etc:

1. Follow this link to the [GitHub repository](https://github.com/matteofiorini92/restaurants-reviews)
2. Click on the Code button
3. In the drop-down, copy the URL that you see in the HTTPs tab
4. In your local IDE, open the terminal
5. Change the current working directory to the location where you want the cloned directory to be made
6. Type git clone and paste the URL you copied in Step 3
7. Press Enter. Your local clone will be created.

## Credits
The content of the deployment section of this readme.md was mostly taken from (this webinar](https://www.youtube.com/watch?v=7BteidgLAyM).

### Images
- The [background image](https://unsplash.com/photos/N_Y88TWmGwA) was taken from [Unsplash](https://unsplash.com/).
- The [gluten free](https://www.iconfinder.com/icons/4650676/bio_celiac_food_gluten_free_label_icon) and [vegan friendly](https://www.iconfinder.com/icons/4650689/cruelty_free_eco_no_meat_vegan_vegetarian_icon) badges were purchased on [IconFinder](https://www.iconfinder.com/)