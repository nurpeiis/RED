
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
10. Some reasoning behind production taken from "Simpleisbetterthancomplex":
    1. NGINX will receive all requests to the server. But it won’t try to do anything smart if the request data. All it is going to do is decide if the requested information is a static asset that it can serve by itself, or if it’s something more complicated. If so, it will pass the request to Gunicorn.

    The NGINX will also be configured with HTTPS certificates. Meaning it will only accept requests via HTTPS. If the client tries to request via HTTP, NGINX will first redirect the user to the HTTPS, and only then it will decide what to do with the request.

    We are also going to install this certbot to automatically renew the Let’s Encrypt certificates.
    2. Gunicorn is an application server. Depending on the number of processors the server has, it can spawn multiple workers to process multiple requests in parallel. It manages the workload and executes the Python and Django code.

    3. Django is the one doing the hard work. It may access the database (PostgreSQL) or the file system. But for the most part, the work is done inside the views, rendering templates, all those things that we’ve been coding for the past weeks. After Django process the request, it returns a response to Gunicorn, who returns the result to NGINX that will finally deliver the response to the client.

    4. The last step is to install Supervisor. It’s a process control system and it will keep an eye on Gunicorn and Django to make sure everything runs smoothly. If the server restarts, or if Gunicorn crashes, it will automatically restart it.

Created by Nurpeiis Baimukan on 9/19/18.

Copyright © 2018 Nurpeiis Baimukan. All rights reserved.
