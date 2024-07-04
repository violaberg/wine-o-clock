# **DEPLOYMENT**

## **Table of Contents**

* [**Table of Contents**](#table-of-contents)
* [**Initial Deployment**](#initial-deployment)
    * [**Create and setup repository**](#create-and-setup-repository)
    * [**Create Heroku App**](#create-heroku-app)
    * [**Set up Heroku for use via the console**](#set-up-heroku-for-use-via-the-console)
* [**Create a Fork**](#create-a-fork)
* [**Clone Repository**](#clone-repository)

## **Initial Deployment**

### **Create and setup repository**

* Log in your Github account (or register if you don't have one yet) and create a new repository. I used CI Full Gitpod template for this as I decided to develop my project on Gitpod for easy access in case if tutor assistance was needed. Plus very handy if as me someone is using 2 devices - PC and laptop in my case, once you push to Github, all your code is available from anywhere with ease.
* In repository go to 'Projects' tab and click 'Link a project', select 'Create new project' from dopdown menu.
* Click on 'Board' and rename it.
* Click on 'Workflows' and 'Item added' to project and 'Edit'.
* Click 'Issue', 'Pull Request' and unselect pull request (this way it will define item as an issue).
* Set value as 'To Do'. Save and turn on 'Workflow'. Exit workflow.
* Open 'Settings' from ... menu located in the top corner. In 'Danger zone' change board to public (if needed to be accessible by others). Go back to 'Settings' tab.
* Scroll to 'Features', within 'Issues' click 'Set up templates', choose 'Custom template'.
* Preview it and click 'pen item' to edit. Add description using template.
* 'Propose changes' and 'commit'.
* To create user story, click on 'Issues', then 'New Issue', 'Get Started'. Fill in the blanks.
* Click on 'Projects' and select appropriate.
* Click 'Submit new issue'.
* Go to 'Projects' tab, click on 'User Stories Kanban Board' to see the user story in 'ToDo' list.
* Populate board with neccessary User Issues to help with project planning and development.<hr>

* Open repository, in my case with Gitpod so I don't need to activate virtual environment as I would otherwise in VS Code Desktop.
* In terminal type <code>pip3 install Django~ =4.2.1</code>(choose Django version you would like to use)
* Install supporting libraries <code>pip3 install dj_database_url</code>, <code>pip3 install psycopg2</code>
* Install gunicorn <code>pip3 install gunicorn</code>
* Create a file Procfile in root and declare web process followed by command <code>web: gunicorn <YOUR_PROJECT_NAME>.wsgi:application</code>
* Create requirements.txt <code>pip3 freeze -r requirements.txt</code>
* Create .gitignore and env.py file for credentials and partS of project that should be  ignored by git, therefore not pushed to Github.
* Create a project <code>django-admin startproject <YOUR_PROJECT_NAME></code>
* Create Initial commit and push to Github.
* Create an app within the project <code>python3 manage.py startapp <YOUR_APP_NAME></code>
* Add the new app to the list of installed apps in settings.py
* Migrate changes <code>python3 manage.py migrate</code>
* Test server to ensure it works locally <code>python3 manage.py runserver</code>

### **Create Heroku App**

Either login or create an account with [Heroku](https://id.heroku.com/login) and sign in.

* Create a new Heroku app. Click 'New' in the top right corner of the landing page, then click 'Create new app'.
* Choose the app a unique name - this will be part of the URL.
* Select the nearest location for yourself and click 'Create App'.
* On the next page click 'Settings' tab and scroll down to 'Config Vars'. This is the place where you hide things like credentials and API keys.
* Scroll down to Buildpacks. The buildpacks will install further dependencies that are not included in the requirements.txt. For this project, the buildpack required is Python.
* Go to 'Deploy' tab and enable deployment method with Github. You will need authorisation if it's first time deploying to Heroku.
* Find app repository by typing in search bar and click 'Connect' for the correct one.
* Enable 'Automatic Deploys' (unless you prefer to keep it manual) then click 'Deploy'
* Once this is done, a message should appear letting know that the app was successfully deployed with a view button to see the app.
* You can either choose to use Heroku offered database (not free) or add your chosen database to config vars. To use Heroku Postgres:
    * Navigate to the 'Resources' tab of the app dashboard. Under the heading 'Add ons' search for 'Heroku Postgres' and click on it when it appears.

## Set up Heroku for use via the console

* Click on Account Settings
* Scroll down to the API Key section and click Reveal. Copy the API key.
* Log in to Heroku via the console and enter your details.
    * heroku login-i
    * When prompted, enter your Heroku username
    * Enter copied API key as the password

* Get your app name from Heroku - <code>heroku apps</code>
* Set Heroku remote - <code>heroku git:remote -a <app_name></code>
* Add, Commit, Pust to GitHub - <code>git add . && git commit -m "Deploy to Heroku via CLI"</code>
* Push to GitHub and Heroku - <code>git push origin main</code>, <code>git push heroku main</code>

## Create a Fork
* Navigate to the [repository](https://github.com/violaberg/wine-o-clock)
* In the top-right corner of the page click on the fork button and select create a fork.
* You can change the name of the fork and add description 
* Choose to copy only the main branch or all branches to the new fork. 
* Click Create a Fork. A repository should appear in your GitHub

## Clone Repository
* Navigate to the [repository](https://github.com/violaberg/wine-o-clock)
* Click on the Code button on top of the repository and copy the link. 
* Open Git Bash and change the working directory to the location where you want the cloned directory. 
* Type git clone and then paste the link.
* Press Enter to create your local clone.

[Back to Readme](README.md)
