# **TESTING**

## **Table of Contents**
* [**User Story Testing**]()
* [**Code Validation**]()
    + [**HTML**]()
    + [**CSS**]()
    + [**JavaScript**]()
    + [**Python**]()
* [**Browser Testing**]()
* [**Device Testing**]()
* [**Lighthouse**]()
* [**Manual Testing**]()
    + [**Navigation**]()
    + [**Home Page**]()
    + [**About Page**]()
    + [**Gallery**]()
    + [**Book a Tour**]()
    + [**Contact Us Page**]()
    + [**Sign Up Page**]()
    + [**Login Page**]()
    + [**Logout Page**]()
* [**Responsiveness**]()
* [**Bugs & Fixes**]()

## **User Story Testing**

For the following, I will leave out the type of user, ***As a developer/admin/user, I can…***, and only list the latter part of the story as a heading.

### **EPIC 1 - Heroku and deployment:**

**...create new Github repository so that I can store project's files online** |passed |
|:---:|:---|
Create new repository |&check;|
|||

**...set up new workspace so that I can start working on project** |passed |
|:---:|:---|
Create workspace on Gitpod using CI Gitpod full template |&check;|
Install Django |&check;|
Add required libraries and PostgreSQL database |&check;|
|||

**...create a new Heroku app and deploy project early to confirm functionality** |passed |
|:---:|:---|
Create new Heroku app |&check;|
Connect database |&check;|
|||

### **EPIC 2 - Developer:**

**...create wireframes so that I can clearly see website layout** |passed |
|:---:|:---|
Create wireframe for desktop and mobile with Balsamiq |&check;|
Export and save wireframes in project's doc/wireframes folder |&check;|
|||

**...choose color scheme and style of the website so that it is pleasant to use** |passed |
|:---:|:---|
Color theme should be decided |&check;|
Style of the project should be decided |&check;|
|||

**...choose fonts so that they match website style** |passed |
|:---:|:---|
Choose two fonts - headings and body |&check;|
Ensure fonts compliment each other |&check;|
|||

**...create fully responsive website so that it is accessible on all devices** |passed |
|:---:|:---|
Design project with mobile first approach |&check;|
Use Bootstrap and media queries to create responsive website |&check;|
|||

### **EPIC 3 - Content:**

**...clearly understand the purpose of the website so that I know if I'm interested** |passed |
|:---:|:---|
I can see the purpose of website |&check;|
|||

**...read relevant content so that I can stay informed** |passed |
|:---:|:---|
User can read content relevant to wine/ wine making |&check;|
Content is easy to read and split in paragraphs |&check;|
Content is relevant to each page on website |&check;|
|||

### **EPIC 4 - Contact:**

**...contact someone at wine cellar so that I can receive any additional information needed or book a tour** |passed |
|:---:|:---|
Responsive and easy to use contact form with necessary fields |&check;|
A confirmation of message sent |&check;|
The Wine O'Clock site should prominently display contact information, including phone number, a contact form and/or email address |&check;|
|||

**...find openings hours so that I know when can I visit** |passed |
|:---:|:---|
A dedicated section, on the Contact page or in the footer, that prominently displays the wine cellar's opening hours |&check;|
The displayed opening hours should be regularly updated to reflect any changes |&check;|
|||

**...find address so that I know wine cellar's location** |passed |
|:---:|:---|
Clearly visible address in footer |&check;|
|||

### **EPIC 5 - User registration & login:**

**...register on site so that I can leave review, add photo and sign up to newsletter** |passed |
|:---:|:---|
Easy sign up form |&check;|
User data stored and processed securely |&check;|
Validation for user input |&check;|
|||

**...login using email and password so that I don't have to remember username** |passed |
|:---:|:---|
Easy to fill login form |&check;|
Validation for user input |&check;|
|||

**...log out so that my data is safe** |passed |
|:---:|:---|
Clearly visible Log out button |&check;|
Redirect user to Home page after logging out |&check;|
|||

### **EPIC 6 - Admin:**

**...login so that I can access the admin panel to update site content** |passed |
|:---:|:---|
A secure login interface |&check;|
Access to only authenticated admin |&check;|
|||

**...add/edit content so that I'm in control of site** |passed |
|:---:|:---|
Access to a dashboard that facilitates the addition and editing of content |&check;|
Functionality for admins to manage media assets, including uploading, deleting, or modifying images |&check;|
User-friendly form to add new content |&check;|
|||

**...delete inappropriate reviews/photos so that site is safe/relevant for users** |passed |
|:---:|:---|
The ability to identify and delete reviews deemed inappropriate or violating community guidelines |&check;|
Able to identify and remove photos from the gallery |&check;|
|||

### **EPIC 7 - Reviews:**

**...leave a review so that can contribute to the community and help other wine enthusiasts make informed decisions** |passed |
|:---:|:---|
The review submission form should include fields for the user to enter a title and written content |&check;|
Review should be instantly visible on page |&check;|
|||

**...add photos to reviews so that I can share my unique perspective and enhance the collective experience** |passed |
|:---:|:---|
An option to "Add Photo" within the review section |&check;|
Clicking on "Add Photo" should offer a user-friendly way to do so |&check;|
|||

**...edit my review so that I can update and refine my contributions, ensuring accuracy and relevance** |passed |
|:---:|:---|
Easily accessible an "Edit" button associated with each of the logged-in user's submitted reviews |&check;|
After confirming the edits, updated review should immediately be visible |&check;|
|||

**...read reviews so that to gain insights into their experiences at the wine cellar** |passed |
|:---:|:---|
Each review should display the user's name or a username and the date of the review |&check;|
The review section should be responsive, ensuring a seamless experience across various devices and screen sizes |&check;|
|||

**...delete my review so that I can have control over the content associated with myself** |passed |
|:---:|:---|
Easily accessible "Delete" button |&check;|
Clicking on the "Delete" option should trigger a confirmation prompt, ensuring that user genuinely intends to remove review |&check;|
Confirming the deletion should immediately remove my review from the site and show confirmation modal |&check;|
|||

### **EPIC 8 - Gallery:**

**...add/delete images to gallery so that user can have a better feel of wine cellar** |passed |
|:---:|:---|
An easy-to-use option to manage gallery |&check;|
Clearly visible confirmation after adding/deleting image |&check;|
Gallery page should reflect changes without a delay |&check;|
|||

### **EPIC 9 - Booking:**

**...book a tour so that I can visit "Wine O'Clock" wine cellar** |passed |
|:---:|:---|
Easy to follow booking form |&cross; (future development)|
Clear booking confirmation |&cross; (future development)|
User input validation |&cross; (future development)|
|||

**...edit my booking so that I can make changes without contacting admin/staff** |passed |
|:---:|:---|
Easy-to-use edit booking form |&cross; (future development)|
Clearly shown confirmation after editing |&cross; (future development)|
Confirmation email sent with new booking data |&cross; (future development)|
|||

**...cancel my booking so that I don't have to contact staff** |passed |
|:---:|:---|
Easy-to-use form to cancel booking |&cross; (future development)|
Alert to confirm cancellation |&cross; (future development)|
Email confirmation |&cross; (future development)|
|||

**...see my booking so that I have a record of it** |passed |
|:---:|:---|
Clearly visible booking information |&cross; (future development)|
|||

### **EPIC 10 - Posts:**

**...create draft posts so that I can finish writing the content later** |passed |
|:---:|:---|
A logged in admin can save a draft blog post |&check;|
Then they can finish the content at a later time |&check;|
|||

**...create, read, update and delete posts so that I can manage blog content** |passed |
|:---:|:---|
Logged in admin can create a blog post |&check;|
Logged in admin can read a blog post |&check;|
Logged in admin can edit a blog post |&check;|
Logged in admin can delete a blog post |&check;|
|||

**...click on a post so that I can read the full text** |passed |
|:---:|:---|
Detailed view of the post is seen when a blog post title is clicked on |&check;|
|||

**...view a paginated list of posts so that I can easily browse through posts** |passed |
|:---:|:---|
If more than one post in the database, these multiple posts are listed |&check;|
When a user opens the blog page a list of posts is seen |&check;|
Visible post titles with pagination to choose what to read |&check;|
|||

### **EPIC 11 - Comments:**

**...leave comments on a post so that I can express my thoughts** |passed |
|:---:|:---|
Easy-to-use form to add a comment |&check;|
Given more than one comment on a post, user can reply once comment is approved |&check;|
|||

**...approve / disapprove comments so that I can filter out objectionable comments** |passed |
|:---:|:---|
A logged in admin can approve a comment |&check;|
A logged in admin can disapprove a comment |&check;|
|||

**...edit & delete my own comment so that I can be involved in the conversation** |passed |
|:---:|:---|
A logged in user can edit their own comment |&check;|
A logged in user can delete their own comment |&check;|
|||

**...view comments on an individual post so that I can read the conversation** |passed |
|:---:|:---|
Given one or more user comments the admin can view them |&check;|
Then a site user can click on the comment thread to read the conversation |&check;|
|||

## **Code Validation**

### **HTML**

All HTML pages were validated using [W3C HTML Validator](https://validator.w3.org/).

|   PAGE                                     |  VALIDATOR SCREENSHOT                                     |   RESULT    |
|--------------------------------------------|-----------------------------------------------------------|-------------|
| Home Page                                  |<details><summary>Home Page</summary><img src=""></details>| <mark>PASS</mark> |
| About Page                                 |<details><summary>About Page</summary><img src=""></details>| <mark>PASS</mark> |
| Gallery Page                               |<details><summary>Gallery</summary><img src=""></details>| <mark>PASS</mark> |
| Book a Tour                                |<details><summary>Book a Tour</summary><img src=""></details>| <mark>PASS</mark> |
| Contact Page                               |<details><summary>Contact Page</summary><img src=""></details>| <mark>PASS</mark> |
| Sign up Page                               |<details><summary>Sign up Page</summary><img src=""></details>| <mark>PASS</mark> |
| Login Page                                 |<details><summary>Login Page</summary><img src=""></details>| <mark>PASS</mark> |
| Logout Page                                |<details><summary>Logout Page</summary><img src=""></details>| <mark>PASS</mark> |

### **CSS**

CSS was validated using [Jigsaw W3](https://jigsaw.w3.org/css-validator/)

### **JavaScript**

|   FILE                                     |  VALIDATOR SCREENSHOT                                     |   RESULT    |
|--------------------------------------------|-----------------------------------------------------------|-------------|
| reviews.js                                 |<details><summary>reviews.js</summary><img src=""></details>| <mark>PASS</mark> ("one unidentified variable 'bootstrap'" ignored as it's caused by cross referencing scripts)|
| comments.js                                |<details><summary>comments.js</summary><img src=""></details>| <mark>PASS</mark> ("one unidentified variable 'bootstrap'" ignored as it's caused by cross referencing scripts)|

### **Python**

All Python pages were validated using [CI Python Linter](https://pep8ci.herokuapp.com/)

| FILE        | VALIDATOR SCREENSHOT                                                                                                    | RESULT            |
| ----------- | ---------------------------------------------------------------------------------------------------------------------- | ----------------- |
| models.py   | <details><summary>Models</summary><img src=""></details>     | <mark></mark> |
| views.py    | <details><summary>Views</summary><img src=""></details>       | <mark></mark> |
| forms.py    | <details><summary>Forms</summary><img src=""></details>       | <mark></mark> |
| urls.py     | <details><summary>Urls</summary><img src=""></details>      | <mark></mark> |
| admin.py    | <details><summary>Admin</summary><img src=""></details>       | <mark></mark> |
| settings.py | <details><summary>Settings</summary><img src=""></details> | <mark></mark> |

## **Browser Testing**

The website was tested on Google Chrome, Firefox and Microsoft Edge browsers.

## **Device Testing**

The website was tested on various devices using Chrome DevTools and real-life device, such as iPhone 12, Dell laptop and iPad Air.

## **Lighthouse**

| Page            |  Screenshot  |
| --------------- | ------------ |
| ***Desktop***   |              |
| Home            | <details><summary>Home</summary><img src="static/images/lighthouse/desktop/home-desktop-lhouse.png"></details> |
| About           | <details><summary>About</summary><img src="static/images/lighthouse/desktop/about-desktop-lhouse.png"></details> |
| Gallery         | <details><summary>Gallery</summary><img src="static/images/lighthouse/desktop/gallery-desktop-lhouse.png"></details> |
| Reviews         | <details><summary>Reviews</summary><img src="static/images/lighthouse/desktop/reviews-desktop-lhouse.png"></details> |
| Contact         | <details><summary>Contact</summary><img src="static/images/lighthouse/desktop/contact-desktop-lhouse.png"></details> |
| Sign Up         | <details><summary>Sign Up</summary><img src="static/images/lighthouse/desktop/signup-desktop-lhouse.png"></details> |
| Login           | <details><summary>Login</summary><img src="static/images/lighthouse/desktop/login-desktop-lhouse.png"></details> |
| Logout          | <details><summary>Logout</summary><img src="static/images/lighthouse/desktop/logout-desktop-lhouse.png"></details> |
| Blog            | <details><summary>Blog</summary><img src="static/images/lighthouse/desktop/blog-desktop-lhouse.png"></details> |
| Blog Post       | <details><summary> Post</summary><img src="static/images/lighthouse/desktop/blog-post-desktop-lhouse.png"></details> |
|  |  |

<br>

| Page            |  Screenshot  |
| --------------- | ------------ |
| ***Mobile***   |              |
| Home            | <details><summary>Home</summary><img src="static/images/lighthouse/mobile/home-mobile-lhouse.png"></details> |
| About           | <details><summary>About</summary><img src="static/images/lighthouse/mobile/about-mobile-lhouse.png"></details> |
| Gallery         | <details><summary>Gallery</summary><img src="static/images/lighthouse/mobile/gallery-mobile-lhouse.png"></details> |
| Reviews         | <details><summary>Reviews</summary><img src="static/images/lighthouse/mobile/reviews-mobile-lhouse.png"></details> |
| Contact         | <details><summary>Contact</summary><img src="static/images/lighthouse/mobile/contact-mobile-lhouse.png"></details> |
| Sign Up         | <details><summary>Sign Up</summary><img src="static/images/lighthouse/mobile/signup-mobile-lhouse.png"></details> |
| Login           | <details><summary>Login</summary><img src="static/images/lighthouse/mobile/login-mobile-lhouse.png"></details> |
| Logout          | <details><summary>Logout</summary><img src="static/images/lighthouse/mobile/logout-mobile-lhouse.png"></details> |
| Blog            | <details><summary>Blog</summary><img src="static/images/lighthouse/mobile/blog-mobile-lhouse.png"></details> |
| Blog Post       | <details><summary> Post</summary><img src="static/images/lighthouse/mobile/blog-post-mobile-lhouse.png"></details> |
|  |  |

## **Manual Testing**

### **Navigation**

| Element                | Action      | Expected Result                                         | Pass/Fail         |
| ---------------------- | ----------- | ------------------------------------------------------- | ----------------- |
| Logo                   | Click       | Redirect to Home page                                   | <mark></mark> |
| Home Link              | Click       | Redirect to Home page                                   |  |
| Register Link          | Click       | Redirect to sign up page                                |  |
| Log in Link            | Click       | Redirect to sign in page                                |  |
| Log out Link           | Click       | Redirect to log out page                                |  |
| Hamburger Menu         | Click       | Render a dropdown menu of all links                     |  |
| Footer Socials         | Click       | Redirect in a new tab to all respective media platforms |  |
| Footer Email           | Click       | Open up an email provider with developer email attached |  |
| Register Link          | Display     | Render for non authenticated users                      |  |
| Log in Link            | Display     | Render for non authenticated users                      |  |
| Log out Link           | Display     | Render only if user is authenticated                    |  |

### Home Page

| Element            | Action      | Expected Result                          | Pass/Fail         |
| ------------------ | ----------- | ---------------------------------------- | ----------------- |
| Book a Tour button | Click       | Redirect to Book a Tour page             | <mark></mark> |

### About Page

| Element            | Action      | Expected Result                          | Pass/Fail         |
| ------------------ | ----------- | ---------------------------------------- | ----------------- |
| Book a Tour button | Click       | Redirect to Book a Tour page             | <mark></mark> |

### Gallery Page

| Element            | Action      | Expected Result                          | Pass/Fail         |
| ------------------ | ----------- | ---------------------------------------- | ----------------- |
| Book a Tour button | Click       | Redirect to Book a Tour page             | <mark></mark> |

### Book a Tour

| Element            | Action      | Expected Result                          | Pass/Fail         |
| ------------------ | ----------- | ---------------------------------------- | ----------------- |
| Book a Tour button | Click       | Redirect to Book a Tour page             | <mark></mark> |

### Contact Page

| Element            | Action      | Expected Result                          | Pass/Fail         |
| ------------------ | ----------- | ---------------------------------------- | ----------------- |
| Book a Tour button | Click       | Redirect to Book a Tour page             | <mark></mark> |

### Review

| Element       | Action      | Expected Result                             | Pass/Fail         |
| ------------- | ----------- | ------------------------------------------- | ----------------- |
| Comment       | Display     | Render the review content, author and date  | <mark></mark> |
| Author Link   | Click       | Redirect to authors profile page            |  |
| Author Icon   | Click       | Redirect to authors profile page            |  |
| Delete Button | Display     | Render if authenticated author              |  |
| Delete Button | Click       | Delete Confirmation Modal appears           |  |
| Delete Button | Hover/Focus | Darken Background                           |  |

### Delete Confirmation Modal

| Element               | Action      | Expected Result                       | Pass/Fail         |
| --------------------- | ----------- | ------------------------------------- | ----------------- |
| Close Button          | Click       | Modal and opacic background disappear | <mark></mark> |
| Confirm Delete Button | Click       | Context item is delete from database  |  |
| Close Button          | Hover/Focus | Darken Background                     |  |
| Confirm Delete Button | Hover/Focus | Darken Background                     |  |

### Sign Up Page

| Element       | Action         | Expected Result                             | Pass/Fail         |
| ------------- | -------------- | ------------------------------------------- | ----------------- |
| Page          | Authentication | Authenticated users redirected to Home page | <mark></mark> |
| Form(Valid)   | Submit         | Redirected to Home page                     |  |
| Form(Valid)   | Submit         | Sign up in Notification received            |  |
| Form(Invalid) | Submit         | Error Context rendered to UI                |  |
| Form(Invalid) | Submit         | Error Notification received                 |  |
| Login Link    | Click          | Redirect to Login Page                      |  |
| Form Button   | Hover/Focus    | Darken Background                           |  |
| Login Link    | Hover/Focus    | Darken Text                                 |  |

### Login Page

| Element       | Action         | Expected Result                             | Pass/Fail         |
| ------------- | -------------- | ------------------------------------------- | ----------------- |
| Page          | Authentication | Authenticated users redirected to Home page | <mark></mark> |
| Form(Valid)   | Submit         | Redirected to Home page                     |  |
| Form(Valid)   | Submit         | Sign up in Notification received            |  |
| Form(Invalid) | Submit         | Error Context rendered to UI                |  |
| Form(Invalid) | Submit         | Error Notification received                 |  |
| Register Link | Click          | Redirect to Sign Up Page                    |  |
| Form Button   | Hover/Focus    | Darken Background                           |  |
| Register Link | Hover/Focus    | Darken Text                                 |  |

### Log Out Page

| Element       | Action         | Expected Result                                | Pass/Fail         |
| ------------- | -------------- | ---------------------------------------------- | ----------------- |
| Page          | Authentication | Un-authenticated users redirected to Home page | <mark></mark> |
| Logout Button | Click          | User session is Logged out                     |  |
| Logout Button | Click          | Redirected to Home page                        |  |
| Form Button   | Hover/Focus    | Darken Background                              |  |

## **Responsiveness**

Responsiveness was achieved using TailwindCSS and custom CSS and tested with Chrome DevTools making sure all pages adjust to screens starting from 280px wide.

## **Bugs & Fixes**

| Bug                                          | Cause                        | Solution                                                                              |
| -------------------------------------------- | ---------------------------- | ------------------------------------------------------------------------------------- |
| TemplateDoesNotExist at /base.html           | Incorrect base.html location | Delete unneccessary folder where base.html is located and move it to correct location |
| Images not displaying                        | Forgot to run collectstatic  | Running <code>python manage.py collectstatic</code> in terminal resolved the issue    |
| TemplateDoesNotExist at /gallery.html        | Incorrect gallery.html path in views.py | Adding 'wine_cellar' resolved the error <code>return render(request, 'wine_cellar/gallery.html', {'gallery_images': gallery_images})</code> |
| CSRF verification error when trying to login as admin | Missing CSRF_TRUSTED_ORIGINS in settings.py | Adding <code>CSRF_TRUSTED_ORIGINS=['https://8000-violaberg-wineoclock-3rc52bvzr9m.ws-eu108.gitpod.io']</code> resolved the issue |
| django.db.migrations.exceptions.InconsistentMigrationHistory | Didn't handle migrations correctly | Contacted tutor support and John very kindly helped me to reset database |
| Impossible to add a non-nullable field 'author' to review without specifying a default | No default value provided to new field in model | Added default='' to field resolved the issue |
| Review text not showing | Changed Review module field from text to body, forgot to change template | Changing <code>{{ review.text }}</code> to <code>{{ review.body }}</code> resolved the issue |
| Logo not showing on account pages | Wrong path <code><img src="../static/images/logo.jpg" alt="Logo" class="logo d-inline-block align-text-top"></code> | Fixing path resolved it <code><img src="{% static 'images/logo.jpg' %}" alt="Logo" class="logo d-inline-block align-text-top"></code> |

[Back to Readme](README.md)