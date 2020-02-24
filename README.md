# g0ng0n.dev personal webapp

This is the repository for my personal webapp that is was created using python3
and django

## Getting Started

### Introduction
I developed this small app with Python3 and Django, you can use sqlite3 or postgresql
depends on you choice, but if you choose postgresql you need to setup more Enviroment variables
because the settings.py file gets some values from those variables

### pre requisites for development purposes
* python3
* pip3
* Enviroment variables needed :
  * SECRET_KEY
  * STATIC_URL ex: ('/static')
  * STATICFILES_DIRS_ONE ex: ('/static')
  * STATIC_ROOT ex: ('/static')
  * MEDIA_ROOT ex: ('/media')
  * MEDIA_URL ex: ('/media')

### Starting the app

1 - run in a terminal `pip3 install -r requirements.txt`
2 - run in a terminal `python3 manage.py start`
3 - in a browser go to `http://127.0.0.1` or the url that you set up in the settings.py

## production

This webapp was deploy in production vps. you can check it out in [here](https://www.g0ng0n.dev)
