#Heroku commands

#Create a new repository
git init

#Authenticate with Heroku
heroku login

#Create a new heroku app
heroku create app-name

# Set up requirements.txt and Procfile files

#Add all the files from the app folder to the git repository
git add .
git commit -m "Commit message"

#Set up remote destination on heroku for pushing files from git
heroku git:remote -a app-name

#Push the app to the web, verify the running app at http://app-name.herokuapp.com
git push heroku master