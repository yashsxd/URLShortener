URL Shortener using Python and Django
=====================================

An application for simple URL shortening service

This application relies of
- Python
- Django

Versions
--------
Before begining installation, make sure the python and pip versions are correct.
- Python==3.6.8
- pip==19.1.1

Instructions
------------
1. Clone 'git clone <url>'
2. Get into directory 'cd URLShortner'
3. Install virtual env 'virtualenvwrapper-win==1.2.5'
4. Make virtual env 'mkvirtualenv URL'
5. Go to Virtual env 'workon URL'
6. Install Django in virual env 'pip install Django==2.2.1'
7. Check installation 'django-admin --version'
8. Install requirements.txt
9. Install Postgresql and PGAdmin
10. Set up the database.
11. Change the database settings in 'local_settings.py'
12. Make database migration 'python manage.py makemigrations'
13. Migrate to database 'python manage.py migrate'
14. Run the console command 'python manage.py runserver'
15. Open browser and open the 'http://127.0.0.1:8000/'
