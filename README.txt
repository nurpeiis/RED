to test email run:
python -m smtpd -n -c DebuggingServer localhost:1025
https://stackoverflow.com/questions/5802189/django-errno-111-connection-refused/5802348#5802348

 

Notes:
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

Issues:
1. Confirm page did not open if the user wanted to reset the password:
    Solution: change the format of url in LOGIN_EXEMPT_URLS for password_reset_confirm

Instructions:
1. Run development server (pwd = print working directory):
    - https://www.youtube.com/watch?v=DgVBKMQoQIE&index=41&list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj
    - django-admin runserver
2. To create new app:
    - django-admin startapp appName 