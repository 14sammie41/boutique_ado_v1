# Boutique Ado

## User Needs

+ This will be a full stack trial run for me.
+ Designed to show I can use the authentication methods needed for shopping and card payments.
+ As a result of this there will not be a lot of detail in here.
+ I will use this document to annotate area's which i struggled with and how I resolved them.

## Deployment to Heroku:

1. Ensure you have the following downloaded:
    + Python version 3.8 at least.
    + Git
    + The Heroku CLI
2. Use the following link - ![Heroku Website](https://www.heroku.com/) to either log in or sign up to the Heroku software.
3. Ensure you have the PostgreSQL add-on (This is a Heroku default)
4. Install the following packages through your terminal using the `pip install` command:
    + `gunicorn`
    + `dj-database-url`
    + `whitenoise`
    + `psycopg2-binary`
        + Be aware that some commands may differ depending on your operating system
5. Add all of the installed packages into your `requirements.txt` file using `pip freeze > requirements.txt` in your terminal.
6. Update `settings.py` to include:
    + `import os`
    + `import dj_database_url`
    + Secret keys - to be protected through Heroku
    + Allowed hosts - may differ depending on your operating system
    + Static root - to include BASE DIR
    + Static file storage - Whitenoise will be used for this
7. Create a Procfile and add `web: gunicorn <your_project_name>.wsgi` replacing your_project_name with the project folder name.
8. On the Heroku website click the "New" button in the top right corner.
9. Select "Create new app"
10. Add the name of the app into the name section.
11. Choose your local region.
12. Click "Create app".
13. Go to the "Deploy" tab at the top.
14. Under the "Deployment method" options, ensure you are using GitHub.
15. Ensure under the "Settings" tab at the top, the Buildpack is set to Python (Heroku/Python).
16. Scroll to the "Config Vars" section of settings and click "Reveal Config Vars".
17. Add your secret keys in here.
18. Create an `.env` file to put your Secret keys in.
19. Ensure you have `os.environ.get()` in your `settings.py` file to allow for those secret keys to be found at deployment.
20. Ensure before you deploy to Heroku you have run the following commands in your terminal:
    + `python manage.py migrate`
    + `python manage.py collectstatic`
21. On the Heroku website go to the deploy tab at the top and scroll down to click the "Deploy branch" button.
22. Finally click the "Open App" button to see your deployed site.
### Issues:

+