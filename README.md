# **Wine O'Clock**

## **Overview**

Wine O'Clock is a fictional wine cellar nested in the heart of the world-renowned Bordeaux wine region in France. Born from my deep passion for wine and the enchanting allure of France, this project invites enthusiasts to embark on an unforgettable journey into the captivating realms of winemaking.<br>
The site shares a brief narrative about Wine O'Clock, offering a glimpse into its rich history and commitment to the craft. Immerse yourself in our curated gallery, adorned with exquisite photos captured by owners, reviews left by cherished visitors, creating a tapestry of memories that resonate with the essence of our vineyard, or read our blog if you crave some more info about all things wine. Whether you're a seasoned connoisseur or a curious explorer, Wine O'Clock has something for everyone. For booking or any additional information, our Contact form is at your disposal. Wine O'Clock beckons, a celebration of passion, tradition, and the timeless beauty of French winemaking.

![Home Page](static/images/wine-o-clock.png)

Deployed project can be found here: [Wine O'Clock](https://wine-o-clock-223a2b0e8720.herokuapp.com/)

## **Table of Contents**
* [**Overview**](#overview)
* [**User experience**](#user-experience-ux)
    + [**Strategy plane**](#strategy-plane)
        - [**Site goals**](#site-goals)
        - [**Opportunities**](#opportunities)
    + [**Scope plane**](#scope-plane)
    + [**Structure plane**](#structure-plane)
        - [**Developer Tasks & User Stories**](#developer-tasks--user-stories)
        - [**Flowchart**](#flowchart)
    + [**Skeleton plane**](#skeleton-plane)
        - [**Wireframes**](#wireframes)
    + [**Surface plane**](#surface-plane)
        - [**Color Scheme**](#color-scheme)
        - [**Typography**](#typography)
* [**Agile Development**](#agile-development)
* [**Features & Future Development**](#features--future-development)
* [**Technologies used**](#technologies-used)
* [**Testing**](#testing)
* [**Deployment**](#deployment)
* [**Acknowledgement & Credits**](#acknowledgement--credits)
* [**Media**](#media)

# **User experience (UX)**

During the planning phase I revisited UX videos provided on the course and used 5 planes to create my design. I tried to keep original idea of project as much as I could but as I got unwell for majority of project time, some big changes can be seen. I have left original planning part for Strategy and Scope plane to show what I begun with. Opportunities in Strategy plane and MoSCoW in Scope plane shows exactly how different project was when I planned it.

## **Strategy plane**

### **Site goals**

* Offer a fully responsive user-friendly site to browse through.
* Implement fully functional features.
* Offer admin/user login with full CRUD funcionality.
* Create a welcoming space for wine enthusiasts to contribute their photos and reviews.
* Promote a passion for wine and travel.

### **Opportunities**

Opportunity | Importance | Viability/Feasibility
---|---|---
Age verification | 5 | 5
Newsletter list | 3 | 5
User register/login | 5 | 5
User profile | 3 | 1
User ability to add photos to gallery | 2 | 3
User ability to delete previously added photos | 2 | 3
User reviews | 5 | 5
Full CRUD funcionality for user | 5 | 5
Full CRUD funcionality for admin | 5 | 5
Admin login via front end | 5 | 5
Password recovery | 5 | 5
Reservation management system for admin | 5 | 3
User ability to book a tour online | 5 | 5
User ability to edit/cancel booking online | 3 | 3
Booking confirmation on site | 5 | 5
Booking confirmation by email | 5 | 5
Booking reminder by email | 3 | 3
Visible booking for logged-in user | 3 | 2
Option to pay for booking online | 3 | 1
About page | 5 | 5
Contact form | 5 | 5
Social media links | 3 | 5
Terms & conditions | 3 | 3
Wine blog | 2 | 2
---|---|---
Total |95|96

## **Scope plane**

Due to a incredible amount of new knowledge and deadline for this project as for anything in life and to avoid scope creep, I used MoSCoW method to keep project on track and concentrate on delivering fully functional site. Unfortunately, since beginning of the project I knew I won't have time to implement everything I would like so decided to leave some features for future development.

* Must Have:
    + User register/login
    + User reviews
    + Full CRUD funcionality for user
    + Full CRUD funcionality for admin
    + About page
    + Contact form
    + Social media links

* Should Have:
    + User ability to book a tour through contact form
    + User ability to add photos to gallery
    + Wine blog
    + Password recovery

* Could Have:
    + User ability to edit/cancel booking online
    + User ability to delete previously added photos

* Won't Have:
    + User profile
    + Reservation management system for admin
    + Newsletter list
    + Booking reminder by email
    + Terms & conditions
    + Option to pay for booking online
    + Booking confirmation on page
    + Booking confirmation by email

## **Structure plane**

### **Developer Tasks & User Stories**

|   EPIC                    |ID|    Task        |
|:--------------------------|--|:---------------|
|SET UP & DEPLOYMENT        |  ||
|                           |  | As a developer, I can create a new Github repository to store my project files online|
|                           |  | As a developer, I can create a new workspace on Gitpod, install Django and add required libraries to have access to cloudbased images and postgress database|
|                           |  | As a developer, I can create a Heroku app and deploy project early to confirm funcionality|
|                           |  ||

<br>

|   EPIC                    |ID|    User Story  |
|:--------------------------|--|:---------------|
|NAVIGATION AND CONTENT     |  ||
|                           |  | As a user, I can navigate through website easily|
|                           |  | As a user, I can clearly understand the purpose of the site|
|                           |  | As a user, I can read relevant content|
|USER REGISTRATION & LOGIN  |  ||
|                           |  | As a user, I can register on the site|
|                           |  | As a user, I can login using USERNAME and password|
|                           |  | As a user, I can logout|
|BOOKING                    |  ||
|                           |  | As a user, I can book a tour|
|                           |  | As a logged-in user, I can see my booking|
|                           |  | As a logged-in user, I can edit my booking|
|                           |  | As a logged-in user, I can cancel my booking|
|REVIEWS                    |  ||
|                           |  | As a user, I can read reviews from other visitors|
|                           |  | As a logged-in user, I can leave a review|
|                           |  | As a logged-in user, I can add my photo taken at wine cellar when leaving a review|
|                           |  | As a logged-in user, I can delete my previously added photo to review|
|                           |  | As a logged-in user, I can edit my review|
|                           |  | As a logged-in user, I can delete my review|
|BLOG                       |  ||
|                           |  | As a user, I can see a paginated list of posts|
|                           |  | As a user, I can click on a post to see full text|
|COMMENTS                   |  ||
|                           |  | As a logged-in user, I can write a comment on post|
|                           |  | As a logged-in user, I can edit my comment|
|                           |  | As a logged-in user, I can delete my comment|
|                           |  | As a user, I can read other people comments|
|GALLERY                    |  ||
|                           |  | As a user, I explore images in gallery|
|CONTACT                    |  ||
|                           |  | As a user, I can find wine cellar's opening hours|
|                           |  | As a user, I can find wine cellar's location|
|                           |  | As a user, I can contact someone at wine cellar|
|ADMIN                      |  ||
|                           |  | As an admin, I can login to access admin panel|
|                           |  | As an admin, I can add/edit content|
|                           |  | As an admin, I can create draft posts|
|                           |  | As an admin, I can create, read, update and delete posts|
|                           |  | As an admin, I can delete inappropriate reviews/photos|
|                           |  | As an admin, I can approve comments|
|                           |  | As an admin, I can delete inappropriate comments|
|                           |  | As an admin, I can upload/ delete images from gallery|
|                           |  | As an admin, I can add description to images in gallery|
|DEVELOPER                  |  ||
|                           |  | As a developer, I can create wireframes|
|                           |  | As a developer, I can create a fully responsive site|
|                           |  | As a developer, I can choose color scheme and style of the website|
|                           |  | As a developer, I can choose fonts|
|                           |  ||

### **Flowchart**

To help with a flow of the website, I created a flowchart using [Draw.io](https://www.drawio.com/)

![Flowchart](static/docs/flowchart.drawio.png)

## **Skeleton plane**

### **Wireframes**

Wireframes for both desktop and mobile were created with [Balsamiq](https://balsamiq.com/) and can be seen below:

#### **Original wireframes:**

#### **Desktop wireframes:**

<details><summary>Home Page</summary><img src="static/docs/wireframes/home-page-desktop.png"></details>

<details><summary>About Page</summary><img src="static/docs/wireframes/about-page-desktop.png"></details>

<details><summary>Gallery Page</summary><img src="static/docs/wireframes/gallery-page-desktop.png"></details>

<details><summary>Book a Tour Page</summary><img src="static/docs/wireframes/book-a-tour-page-desktop.png"></details>

<details><summary>Contact Page</summary><img src="static/docs/wireframes/contact-page-desktop.png"></details>

<details><summary>Login Page</summary><img src="static/docs/wireframes/login-page-desktop.png"></details>

#### **Mobile wireframes:**

<details><summary>Home Page</summary><img src="static/docs/wireframes/home-page-mobile.png"></details>

<details><summary>About Page</summary><img src="static/docs/wireframes/about-page-mobile.png"></details>

<details><summary>Gallery Page</summary><img src="static/docs/wireframes/gallery-page-mobile.png"></details>

<details><summary>Book a Tour Page</summary><img src="static/docs/wireframes/book-a-tour-page-mobile.png"></details>

<details><summary>Contact Page</summary><img src="static/docs/wireframes/contact-page-mobile.png"></details>

<details><summary>Login Page</summary><img src="static/docs/wireframes/login-page-mobile.png"></details>

#### **New wireframes:**

#### **Desktop wireframes:**

<details><summary>Home Page</summary><img src="static/docs/wireframes/home-page-desktop-new.png"></details>

<details><summary>About Page</summary><img src="static/docs/wireframes/about-page-desktop-new.png"></details>

<details><summary>Gallery Page</summary><img src="static/docs/wireframes/gallery-page-desktop-new.png"></details>

<details><summary>Reviews Page</summary><img src="static/docs/wireframes/review-page-desktop-new.png"></details>

<details><summary>Blog Page</summary><img src="static/docs/wireframes/blog-page-desktop-new.png"></details>

<details><summary>Blog post Page</summary><img src="static/docs/wireframes/blog-post-page-desktop-new.png"></details>

<details><summary>Contact Page</summary><img src="static/docs/wireframes/contact-page-desktop-new.png"></details>

<details><summary>Contact Success Page</summary><img src="static/docs/wireframes/contact-successful-page-desktop-new.png"></details>

<details><summary>Login Page</summary><img src="static/docs/wireframes/login-page-desktop-new.png"></details>

<details><summary>Logout Page</summary><img src="static/docs/wireframes/logout-page-desktop-new.png"></details>

<details><summary>Register Page</summary><img src="static/docs/wireframes/sign-up-page-desktop.png"></details>

#### **Mobile wireframes:**

<details><summary>Home Page</summary><img src="static/docs/wireframes/home-page-mobile-new.png"></details>

<details><summary>About Page</summary><img src="static/docs/wireframes/about-page-mobile-new.png"></details>

<details><summary>Gallery Page</summary><img src="static/docs/wireframes/gallery-page-mobile-new.png"></details>

<details><summary>Reviews Page</summary><img src="static/docs/wireframes/review-page-mobile-new.png"></details>

<details><summary>Blog Page</summary><img src="static/docs/wireframes/blog-page-mobile-new.png"></details>

<details><summary>Blog post Page</summary><img src="static/docs/wireframes/blog-post-page-mobile-new.png"></details>

<details><summary>Contact Page</summary><img src="static/docs/wireframes/contact-page-mobile-new.png"></details>

<details><summary>Contact Success Page</summary><img src="static/docs/wireframes/contact-successful-page-mobile-new.png"></details>

<details><summary>Login Page</summary><img src="static/docs/wireframes/login-page-mobile-new.png"></details>

<details><summary>Logout Page</summary><img src="static/docs/wireframes/logout-page-mobile-new.png"></details>

<details><summary>Register Page</summary><img src="static/docs/wireframes/sign-up-page-desktop.png"></details>

### **Database schema**

![Database schema](static/docs/database-schema.drawio.png)

## **Surface plane**

### **Color Scheme**

The color palette chosen for Wine O'Clock app reflects a thoughtful blend of elegance and richness inspired by the world of wines. The soft and inviting Seasalt shade `#fafafa` serves as the symbol of the purity and clarity found in the process of winemaking. The use of Muted gold shade `#daa520` represents the allure of gold, mirroring the excellence and sophistication associated with wines bringing a sense of warmth to project. This golden hue speaks to the refined taste and quality that defines the Wine O'Clock experience. Accentuating the palette are deep, juicy tones of Bordeaux `#4c0013`, evoking the essence of rich red wines, and a Classic black `#000000`, representing the depth and complexity found in a perfectly aged bottle. Each color is carefully selected to embody the journey from vine to cellar, culminating in a visual harmony that encapsulates the luxurious world of Bordeaux wines at Wine O'Clock.

![Color palette](static/docs/color/color-palette.png)

To add more depth and interest to design but not make it overwhelming for user to look at, I created a pattern for background using one my colors - Classic black `#000000`:

![Pattern](static/docs/color/pattern.png)

### **Typography**

In planning the visual identity of my website, I meticulously selected two fonts, Parisienne and Montserrat, to convey a harmonious blend of elegance and readability. Parisienne, with its delicate and flowing script, exudes a touch of sophistication, making it ideal for captivating headings that leave a lasting impression. Complementing this, Montserrat provides a clean and modern sans-serif typeface for content, ensuring optimal legibility and a seamless reading experience. Together, these fonts not only reflect the timeless allure of France and wine industry but also contribute to an aesthetically pleasing and engaging design, inviting visitors to explore our content with both style and clarity.

# **Agile Development**

I have included details of agile development in a separate file [AGILE.md](AGILE.md).

# **Features & Future Development**

## **Features**

## **Future Development**

In the second half of development I realized what I won't be able to implement due to dealine fast approaching. I decided to leave following features for future development:
* Map with marker so that location is easier to find
* Option to book and edit a tour online
* Option to book special occasions online
* Option to pay for everything online
* I would like to add an option to purchase wine directly from site

# **Technologies used**

* HTML
* CSS
* Javascript
* Python
* Django
* Django allAuth
* Bootstrap
* [Heroku](https://www.heroku.com/)
* [Neon](https://console.neon.tech/)
* Jinja
* Whitenoise
* Cloudinary
* Summernote

# **Testing**

I have included details of testing in a separate file [TESTING.md](TESTING.md).

# **Deployment**

I have included details of testing in a separate file [DEPLOYMENT.md](DEPLOYMENT.md).

# **Acknowledgement & Credits**

* [Pattern Monster](https://pattern.monster/) - background pattern
* [Google Fonts](https://fonts.google.com/) - fonts
* [Font Awesome](https://fontawesome.com/) - icons

# **Media**

## **Page images**
* [Vecteezy](https://www.vecteezy.com/) - Home page image by Chinnachart Martmoh, available at this [link](https://www.vecteezy.com/photo/6660921-red-wine-and-white-wine-in-a-glass-of-wine-wooden-tabletop-there-is-a-wine-cellar-on-the-table-and-red-and-green-grapes-the-background-is-an-underground-wine-cellar-3d-rendering)
* [Freepik](https://www.freepik.com/) - About page image by wirestock, available at this [link](https://www.freepik.com/free-photo/beautiful-shot-large-agricultural-field-countryside-with-hills-amazing-cloudy-sky_15695562.htm#page=2&query=wine%20cellar&position=24&from_view=search&track=ais&uuid=f149cfd0-a789-4804-9520-8783151b7d53)
* [Vecteezy](https://www.vecteezy.com/) - Reviews page image by somchai sanvongchaiya, available at this [link](https://www.vecteezy.com/photo/29630339-pouring-red-wine-into-a-glass-in-the-vineyard-french-red-wine)
* [Vecteezy](https://www.vecteezy.com/) - Contact page image by icon ade, available at this [link](https://www.vecteezy.com/photo/32944686-old-fashioned-letter-with-ancient-calligraphy-on-parchment)

## **Blog images**
* [Vecteezy](https://www.vecteezy.com/) - blog image by icon ade, available at this [link](https://www.vecteezy.com/photo/32937082-farmers-harvesting-fresh-fruit-in-the-autumn-sunlight-heat)
* [Vecteezy](https://www.vecteezy.com/) - blog image by Idalba Granada, available at this [link](https://www.vecteezy.com/photo/36222024-ai-generated-gourmet-food-wine-cheese-bread-and-variety-generated-by-ai)
* [Vecteezy](https://www.vecteezy.com/) - blog image by Idalba Granada, available at this [link](https://www.vecteezy.com/photo/36222005-ai-generated-gourmet-wineglass-on-table-celebrating-with-elegance-generated-by-ai)
* [Vecteezy](https://www.vecteezy.com/) - blog image by Chinnachart Martmoh, available at this [link](https://www.vecteezy.com/photo/6667071-red-and-white-wine-in-clear-glass-many-blurred-wine-whisky-and-brandy-bottle-backgrounds-place-it-on-a-wooden-and-mable-floor-with-a-wooden-board-wall-the-cellar-tasting-production-concept)

## **Review images**
* [Pexels](https://www.pexels.com/) - review image by Grape Things, available at this [link](https://www.pexels.com/photo/woman-in-white-long-sleeve-shirt-sitting-on-green-grass-field-7347162/)
* [Vecteezy](https://www.vecteezy.com/) - review image by Iftikhar Alam, available at this [link](https://www.vecteezy.com/photo/35779505-ai-generated-close-up-of-wineglasses-with-red-wine-in-vineyard-blurred-image-of-friends-toasting-wine-in-a-vineyard-in-the-daytime-outdoors-ai-generated)
* [Vecteezy](https://www.vecteezy.com/) - review image by Yulia Gapeenko, available at this [link](https://www.vecteezy.com/photo/29559149-woman-raises-her-wine-glass-to-a-couple-of-friends)
* Other review images were generated by me using [Adobe Firefly](https://firefly.adobe.com/)

## **Gallery images**
* [Vecteezy](https://www.vecteezy.com/) - gallery image by Pierluigi Palazzi, available at this [link](https://www.vecteezy.com/photo/5893154-vineyard-with-tractor)
* [Vecteezy](https://www.vecteezy.com/) - gallery image by Chinnachart Martmoh, available at this [link](https://www.vecteezy.com/photo/6660079-red-wine-bottle-and-clear-glass-with-red-wine-put-on-a-wooden-tank-with-many-wine-fermentation-tanks-at-cellar-placed-close-to-the-red-brick-wall-3d-rendering)
* [Vecteezy](https://www.vecteezy.com/) - gallery image by icon ade, available at this [link](https://www.vecteezy.com/photo/30655839-vineyard-with-rows-of-vines-in-the-background-and)
* [Vecteezy](https://www.vecteezy.com/) - gallery image by Giuseppe Ramos, available at this [link](https://www.vecteezy.com/photo/25494680-sun-kissed-grapes-harvested-for-organic-winemaking-perfect-for-autumn-picnics-generated-by-ai)
* [Vecteezy](https://www.vecteezy.com/) - gallery image by Chinnachart Martmoh, available at this [link](https://www.vecteezy.com/photo/6666904-red-wine-in-clear-glass-red-grapes-green-grapes-and-wine-fermentation-tank-on-a-table-with-a-wooden-floor-or-tree-bark-the-background-image-was-a-morning-mountain-fog-and-morning-sun-3d-rendering)
* [Vecteezy](https://www.vecteezy.com/) - gallery image by Kseniia Chunaeva, available at this [link](https://www.vecteezy.com/photo/27895081-wine-barrels-in-a-old-wine-cellar)
* [Vecteezy](https://www.vecteezy.com/) - gallery image by Chinnachart Martmoh, available at this [link](https://www.vecteezy.com/photo/6666923-wooden-barrels-for-wine-fermentation-room-for-storing-multiple-wine-fermentation-tanks-the-brick-wall-is-red-orange-3d-rendering)
* [Vecteezy](https://www.vecteezy.com/) - gallery image by Irina Kryvasheina, available at this [link](https://www.vecteezy.com/photo/35756202-ai-generated-many-people-are-laughing-while-toasting)
* [Freepik](https://freepik.com/) - gallery image by freepik, available at this [link](https://www.freepik.com/free-photo/medium-shot-woman-tasting-wine_27260416.htm#fromView=search&page=1&position=7&uuid=edae1f89-c433-4e03-b036-d6e263e3f303)
* [Freepik](https://www.freepik.com/) - gallery image by pressfoto, available at this [link](https://www.freepik.com/free-photo/smell-wine_5402327.htm#fromView=search&page=1&position=42&uuid=edae1f89-c433-4e03-b036-d6e263e3f303)
* [Freepik](https://www.freepik.com/) - gallery image by lookstudio, available at this [link](https://www.freepik.com/free-photo/ginger-lady-green-trendy-dress-holding-glass-with-wine-sitting-with-short-haired-girl-white-cool-tshirt-outdoor_23993417.htm#fromView=search&page=2&position=7&uuid=edae1f89-c433-4e03-b036-d6e263e3f303)
* [Pexels](https://www.pexels.com/) - gallery image by furkanfdemir, available at this [link](https://www.pexels.com/photo/modern-restaurant-with-wine-cellar-in-daylight-6309844/)
