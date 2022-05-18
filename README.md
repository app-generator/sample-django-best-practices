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
$ python manage.py makemigrations  
$ python manage.py migrate
$ python manage.py runserver
```

<br />

## ✨ Pre-compile and compressing styles files

These processes are automatically handled when the server is running. For this, we are using django packages such as:

- [django-static-precompiler](https://github.com/andreyfedoseev/django-static-precompiler)
- [django-compressor](https://django-compressor.readthedocs.io/en/stable/)
- [django-libsass](https://github.com/torchbox/django-libsass)

## ✨ Build from docker

Before building the containers with Docker, create a `.env` file. You can check `.env.sample` file for the structure of the environment 
file. You will need to have a `SECRET_KEY` and `DEBUG` variables. You can check [djecrety](https://djecrety.ir/).

```bash
SECRET_KEY=
DEBUG=
```

And finally, build and run the containers. The `Dockerfile.dev` at the root of the project is used for the Django application.

```bash
docker-compose up --build -d
```

The application will be running at http://localhost:85

## ✨ Deploy on github workflow

For the deployment on Heroku, there no need to use `docker-compose`. Heroku just need a Dockerfile. You can find
an example of a `Dockerfile` for Heroku deployment at the [root of the project](https://github.com/app-generator/sample-django-best-practices/blob/main/Dockerfile).

First set the git secrets using this https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository
Add the following keys to the secrets : HEROKU_APP_NAME , HEROKU_EMAIL , HEROKU_API_KEY. 
Note that the test job will run before the deploy is triggered.

## ✨ Code-base structure

The project has a super simple structure, represented as below:

```shell
.dockerignore
.github
   |-- workflows
   |   |-- django.yaml
.gitignore
Dockerfile
Dockerfile.dev
LICENSE
README.md
apps
   |-- __init__.py
   |-- apps.py
   |-- authentication
   |   |-- __init__.py
   |   |-- admin.py
   |   |-- apps.py
   |   |-- forms.py
   |   |-- migrations
   |   |   |-- __init__.py
   |   |-- models.py
   |   |-- tests.py
   |   |-- urls.py
   |   |-- views.py
   |-- home
   |   |-- __init__.py
   |   |-- urls.py
   |   |-- views.py
   |-- static
   |   |-- font-awesome-4.7.0
   |   |   |-- HELP-US-OUT.txt
   |   |   |-- css
   |   |   |   |-- font-awesome.css
   |   |   |   |-- font-awesome.min.css
   |   |   |-- fonts
   |   |   |   |-- FontAwesome.otf
   |   |   |   |-- fontawesome-webfont.eot
   |   |   |   |-- fontawesome-webfont.svg
   |   |   |   |-- fontawesome-webfont.ttf
   |   |   |   |-- fontawesome-webfont.woff
   |   |   |   |-- fontawesome-webfont.woff2
   |   |   |-- less
   |   |   |   |-- animated.less
   |   |   |   |-- bordered-pulled.less
   |   |   |   |-- core.less
   |   |   |   |-- fixed-width.less
   |   |   |   |-- font-awesome.less
   |   |   |   |-- icons.less
   |   |   |   |-- larger.less
   |   |   |   |-- list.less
   |   |   |   |-- mixins.less
   |   |   |   |-- path.less
   |   |   |   |-- rotated-flipped.less
   |   |   |   |-- screen-reader.less
   |   |   |   |-- stacked.less
   |   |   |   |-- variables.less
   |   |   |-- scss
   |   |   |   |-- _animated.scss
   |   |   |   |-- _bordered-pulled.scss
   |   |   |   |-- _core.scss
   |   |   |   |-- _fixed-width.scss
   |   |   |   |-- _icons.scss
   |   |   |   |-- _larger.scss
   |   |   |   |-- _list.scss
   |   |   |   |-- _mixins.scss
   |   |   |   |-- _path.scss
   |   |   |   |-- _rotated-flipped.scss
   |   |   |   |-- _screen-reader.scss
   |   |   |   |-- _stacked.scss
   |   |   |   |-- _variables.scss
   |   |   |   |-- font-awesome.scss
   |   |-- img
   |   |   |-- Finished Website.png
   |   |   |-- b.png
   |   |   |-- background.jpg
   |   |   |-- background2.png
   |   |   |-- bootstrap2.png
   |   |   |-- features.png
   |   |-- scss
   |   |   |-- styles.scss
   |-- templates
   |   |-- accounts
   |   |   |-- home.html
   |   |   |-- login.html
   |   |   |-- register.html
   |   |-- includes
   |   |   |-- base.html
   |   |-- index.html
   |-- user
   |   |-- __init__.py
   |   |-- admin.py
   |   |-- apps.py
   |   |-- migrations
   |   |   |-- 0001_initial.py
   |   |   |-- __init__.py
   |   |-- models.py
   |   |-- tests.py
   |   |-- views.py
core
   |-- __init__.py
   |-- asgi.py
   |-- settings.py
   |-- urls.py
   |-- wsgi.py
docker-compose.yaml
manage.py
nginx
   |-- nginx.dev.conf
pytest.ini
requirements.txt
staticfiles
   |-- .gitkeep
```

---
**Django Best Practices** - Provided by AppSeed
