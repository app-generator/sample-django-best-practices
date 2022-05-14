# Django Best Practices

A simple `Django` codebase that provides best practices for a secure production deployment.

> Status: **WIP** (not stable)

<br />

> Checklist

| Status | Item | info |
| --- | --- | --- |
| ✔️ | `Up-to-date Dependencies` | - |
| ✔️ | Simple Django Project | - |
| ✔️ | BS5 for styling | Local path (latest BS5 stable version) |
| ✔️ | Simple Custom Login / Register pages | - |
| ✔️ | Unitary tests | - |
| ✔️ | SCSS to CSS compilation | - |
| ✔️ | Rate Limiter for Login & Register | - |
| ✔️ | Page Compression | - |
| ✔️ | Deployment | - |
| ✔️ | HEROKU integration | - |
| ✔️ | Docker | - |

<br />

## ✨ Build from sources

```bash
$ # Clone the sources
$ git clone https://github.com/app-generator/sample-django-best-practices.git
$ cd sample-django-best-practices
$
$ # Virtualenv modules installation (Unix based systems)
$ virtualenv env
$ source env/bin/activate
$
$ # Virtualenv modules installation (Windows based systems)
$ # virtualenv env
$ # .\env\Scripts\activate
$
$ # Install requirements
$ pip3 install -r requirements.txt
$
$ # Run the application
$ python manage.py makemigrations && python manage.py migrate && python manage.py runserver
```

> Note: To use the app, please access the registration page and create a new user. After authentication, the app will unlock the private pages.

<br />

## ✨ Build from docker

```bash
# Run using docker-compose
docker-compose build  # This will build the containers
docker-compose up     # This will bring up the application
```

## ✨ Deploy on github workflow

```bash
# First set the git secrets using this https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository
# Add the following keys to the secrets : HEROKU_APP_NAME , HEROKU_EMAIL , HEROKU_API_KEY
# In the Dockerfile comment the line `CMD [ "uwsgi", "--socket", "0.0.0.0:5000", "--protocol", "http", "--wsgi", "run:app" ]`
# Use the direct flask application run by uncommenting/adding the line `CMD [ "python", "run.py"]`
# on push to the master/main the GH workflow will automatically create and push the image to your heroku
```

## ✨ Code-base structure

The project has a super simple structure, represented as below:

```
< PROJECT ROOT >
   |
   |-- app/
   |    |
   |    |-- __init__.py                 # Initialization of app
   |    |-- config.py                   # Handlers for the front end routes
   |    |-- setup_security.py                      
   |    |-- auth/
   |    |
   |    |   |-- __init__.py
   |    |   |-- email.py
   |    |   |-- forms.py
   |    |   |-- models.py               # Database models for storing data
   |    |   |-- routes.py               # REST API hanlder
   |    |
   |    |-- static/                     # CSS files, Javascripts files
   |    |   
   |    |   |-- css/
   |    |   |
   |    |   |   |-- bootstrap.min.css
   |    |   |   |-- bootstrap.min.css.map
   |    |   |   |-- style.css
   |    |   |
   |    |   |-- js/
   |    |   |
   |    |   |   |-- bootstrap.min.js
   |    |   |   |-- jquery.min.js
   |    |   |
   |    |-- templates/
   |    |
   |    |    |-- auth/                    # Auth related pages login/register
   |    |    |
   |    |    |    |-- login.html
   |    |    |    |-- register.html
   |    |    |    |-- reset_password.html
   |    |    |    |-- reset_password_request.html
   |    |    |
   |    |    |-- bootstrap/
   |    |    |
   |    |    |    |-- bs5_base.html
   |    |    |
   |    |    |-- email/
   |    |    |  
   |    |    |    |-- reset_password.html
   |    |    |    |-- reset_password.txt
   |    |    |
   |    |    |-- forms/
   |    |    |
   |    |    |    |-- forms.html
   |    |    |
   |    |    |-- navbar/
   |    |    |  
   |    |    |    |-- messages.html
   |    |    |    |-- navbar.html
   |    |    |-- base.html
   |    |
   |    |-- utils/
   |    |
   |    |    |-- __init__.py
   |    |    |-- app_logger.py
   |    |    |-- decorators.py
   |    |    |-- mailer.py
   |    |
   |-- requirements.txt
   |-- run.py
   |
   |-- ************************************************************************
```
  


---
**Django Best Practices** - Provided by AppSeed
