
# RED Website 
## Notes:
1. Models.py   
   - Whenever you make changes in the model you have to make migrations to update the database:
    python manage.py  makemigrations
    apply changes: python manage.py migrate
2. settings.py
    - LOGIN_EXEMPT_URLS = pages that logged out users can see
    - EMAIL_HOST = virtual email simulator
3. Middleware.py
    - Restricts access depending on whether user is logged in or out
4. admin.py
    - Customize admin page

## Issues:
1. Confirm page did not open if the user wanted to reset the password:
    Solution: change the format of url in LOGIN_EXEMPT_URLS for password_reset_confirm

## Instructions:

2. To create new app:
    - django-admin startapp appName 
    - add to settings file in Installed app
    - in RED/urls.py add the link for new app
    - in appName/ create urls.py file
3. Github commit:
    1. git add . 
    2. git commit -m ""
    3. git push
4. Creating forms:
    1. create forms.py file within an app directory
    2. in forms.py create a class for the forma
    3. use this class from form in views.py
5. To test email run:
python -m smtpd -n -c DebuggingServer localhost:1025
https://stackoverflow.com/questions/5802189/django-errno-111-connection-refused/5802348#5802348
6. To run through django-admin command:
    1. check django setting module: env | grep DJANGO_SETTINGS_MODULE
    2. export the path: export DJANGO_SETTINGS_MODULE=RED.settings.dev or prod
    3. export PYTHONPATH = "/Users/nurpeiis/Desktop/RED_Co-LAB/RED"
7. Requirements:
    1. pip install -r RED/requirements/dev.txt
8. Hosting static files:
    1. Inefficient in the main file in production
    2. Use AWS
9. To start server:
    1. export PYTHONPATH=/Users/nurpeiis/Desktop/RED_Co-LAB/RED
    2. export DJANGO_SETTINGS_MODULE=RED.settings.dev or prod depending on the stage
    3. django-admin runserver
10. Hierarchial representation of the data for form with MPTT
11. Notes not to forget:
    - Purchase license single from bootstrapmade: https://bootstrapmade.com/license/
Created by Nurpeiis Baimukan on 9/19/18.

Copyright © 2018 Nurpeiis Baimukan. All rights reserved.
