# FoodReview

![home page all screen sizes](https://raw.githubusercontent.com/matteofiorini92/FoodReview/master/static/img/wireframes/food-review-responsive.png)

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

The purpose of the website is for users to read about previous experiences other people had, at reastaurants they may want to go to.
Restaurants will have all the relevant contact details, a pricing score (based on the price of an average meal), a star score (based on the average of their reviews) and badges if they are vegan-friendly and have gluten-free options.

- User story 1: As a visitor, I want to check a restaurant's reviews before deciding to book
- User story 2: As a user, I want to leave a review of a restaurant that's already present in the list, that I've recently eaten at
- User story 3: As a user, I want to add a new restaurant to the list, so that myself and other users can leave our reviews
- User story 4: As a user, I want to be able to manage my previous reviews. This includes editing or deleting them.
- User story 5: As an admin user, I want to have control over new restaurants that are added. Since restaurants' details are objective, they need to be reviewed and approved by me
- User story 6: As an admin user, I want to be able to delete or edit restaurants once they've been approved. 
- User story 7: As an admin user, I want to be bale to delete unfair or spam reviews. I don't want to be able to edit a review, as the review's author is the only one who should be allowed to edit it.
- User story 8: As a visitor, I want to be able to register on the website to add new restaurants and reviews
- User story 9: As a user, I want to be able to log-in and log-out of the website

### The Scope Plane

Users want to be able to rate their experiences when eating out, to leave the reviews for other people to know how a particular restaurant was, what was their favourite dish, what they didn't enjoy.
At the same time, people want to know what to expect when they go to a new place, they rely on other users experiences to know whether a place is nice or not, if a low-cost small diner has better food than a fancy restaurant.

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

- [Add Restaurant](https://raw.githubusercontent.com/matteofiorini92/restaurants-reviews/master/static/img/wireframes/add_restaurants.png)
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

- Feature 1 - Search restaurants by name and location
- Feature 2 - Read reviews and access contact details of restaurants
- Feature 3 - Request to add a new restaurant
- Feature 4 - Edit an existing restaurant (admin only)
- Feature 5 - Add a new review
- Feature 6 - Edit an existing review
- Feature 7 - Delete a restaurant (admin only)
- Feature 8 - Delete a review
- Feature 9 - Approve restaurants (admin only)
- Feature 10 - Register, log-in, log-out

### Features Left to Implement
- Filter restaurants by "has_vegan_options" or "has_gluten_free_options"

## Technologies Used

- [Balsamiq](https://balsamiq.com/) for the wireframes of this readme.md file
- [Materialize](https://materializecss.com/) to use the grid system, pre-formatted buttons, colors and panel cards
- [Canva](https://www.canva.com/) to create the logo image
- [JQuery](https://code.jquery.com/) to initiate some interactive elements of the materialize framework
- [Jinja](jinja.palletsprojects.com) to re-use common elements of different pages with templates
- [Flask](https://flask.palletsprojects.com/) to write the python part of the project
- [Gitpod](https://gitpod.io/) to develop the project
- [GitHub](https://github.com/) for version control
- [Heroku](https://www.heroku.com) to deploy the project
- [IconFinder](https://www.iconfinder.com/) for the vegan friendly and gluten free badges

## Testing

Usability and responsiveness were tested on the following browsers:
- Google Chrome Version 90.0.4430.212 (Official Build) (x86_64)
- Mozilla Firefox Version 72.0.2 (32-bit)
- Safari Version 13.0.5 (15608.5.11)

All sections and divs adapted to the screen size as expected, all links worked fine and the navigation was flawless.
Some styling gets lots using Firefox (e.g. the "how to play" bar) but the rest of the website worked without any issues.

 
- User story 1: I want to prove to myself how well I know a specific subject (movies, books, etc.).
The player is able to challenge themselves on a number of topics, choosing the difficulty and length of the challenge.
The final scoreboard is made with random scores, it doesn't give a realistic idea of what the player's score is - a more accurate scoreboard with real previous scores will be implemented in the future.

- User story 2: I want to challenge my friends on who knows a particular topic the best
The scoring system allows multiple players to play one after the other, and see who knows a particular topic best by comparing the final points. This needs to be done by the players as the system doesn't record the scoring of previous games.

The Google Chrome Lighthouse reports for Desktop and Mobile:
- ![Desktop](https://raw.githubusercontent.com/matteofiorini92/QuotesQuiz/master/assets/img/lighthouse/lighthouse-desktop.png)
- ![Mobile](https://raw.githubusercontent.com/matteofiorini92/QuotesQuiz/master/assets/img/lighthouse/lighthouse-mobile.png)


I used the following validators to check my HTML, CSS and JavaScript code:

[HTML Validator](https://validator.w3.org/)
- [Home Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fmatteofiorini92.github.io%2FQuotesQuiz%2F)

[CSS Validator](https://jigsaw.w3.org/css-validator/)

- [style.css file](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fmatteofiorini92.github.io%2FQuotesQuiz%2Fassets%2Fcss%2Fstyle.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
<p>
    <a href="https://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="https://jigsaw.w3.org/css-validator/images/vcss-blue"
            alt="Valid CSS!" />
    </a>
</p>

[JS Validator](https://jshint.com/)

### Bugs

- Issues with background image not responsive:
    - tried using cover and contain based on the size of the viewport but that didn't work)
    - fixed by setting the background-size property to 100% auto
- Characters button text turning black once clicked:
    - fixed by adding color: #FFF to the right-answer / wrong-answer classes
- Fake results calculations giving unrealistic scores:
    - fake results for made up players was calculating a random number between the lowest and highest achievable scores for that game
    - this gives unrealistic results, for example a game of 1 round can only have a result of either 5 or -2, it can't give a result of 0
    - changed logic so that for each fake character the system adds either 5 or -2 randomly, for the number of rounds of the game
- 2 extra characters for "hard" version weren't hidden at the end of the gaem
    - fixed this by adding the "hidden" class to the "hard" characters buttons
- Names of the wrong characters were just checked against the right answer. This could give duplicates as there could be two wrong characters with the same name
    - changed logic used to retrieve the wrong characters fake names, so that each new name was compared with the right name and existing wrong answers
- Deployed website wasn't workin because GitHub pages only works with relative paths, not with absolute paths
    - switch paths to relative
- Click of Start Game button firing multiple times
    - fixed by adding e.stopImmediatePropagation() to the event listener as suggested in [this](https://stackoverflow.com/a/24564826) StackOverflow thread.
- When trying to clean up the code and merge duplicated code into functions, the processing of two topics (friends and got) stopped working as the structure of the response was different:
    - fixed by adapting the structure of allAuthors to an array of objects for these two topics as well, so that the same function could be used to process allAuthors for all topics.
- The friends API is slow to respond the first time: a loading icon should be added while waiting for the response.
            

## Deployment

[Link to deployed website](https://restaurants-reviews-mf.herokuapp.com/)

This project was developed using GitPod, pushed to GitHub and deployed using GitHub Pages.

To deploy to GitHub Pages from its GitHub repository, the following steps were taken:

1. Log into GitHub
2. From the list of repositories on the screen, select **matteofiorini92/QuotesQuiz**
3. From the menu items near the top of the page, select **Settings**
4. Scroll down to the **GitHub Pages** section
5. Under **Source** click the drop-down menu labelled **None** and select **master**
6. In the **folder** drop-down, the **/root** folder is automatically selected
7. Click on **Save**
8. The project is now deployed and the URL of the website is available in the GitHub Pages section

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

1. Follow this link to the [GitHub repository](https://github.com/matteofiorini92/QuotesQuiz)
2. Click on the Code button
3. In the drop-down, copy the URL that you see in the HTTPs tab
4. In your local IDE, open the terminal
5. Change the current working directory to the location where you want the cloned directory to be made
6. Type git clone and paste the URL you copied in Step 3
7. Press Enter. Your local clone will be created.

## Credits


### Acknowledgements

The content of the deployment section of this readme.md was mostly taken from [this webinar](https://www.youtube.com/watch?v=7BteidgLAyM).

images
https://unsplash.com/photos/N_Y88TWmGwA