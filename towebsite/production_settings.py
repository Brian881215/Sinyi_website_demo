from .settings import *
import os
# Our production settings file
# Inherits all settings from settings.py
# Adds extra settings


DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': os.environ['CLOUD002_ADB'],
        'HOST': os.environ['CLOUD002_HOST'],
        'PORT': os.environ['CLOUD002_PORT'],
        'USER': os.environ['CLOUD002_USER'],
        'PASSWORD': os.environ['CLOUD002_PWD'],
        'OPTIONS': {'driver': 'ODBC Driver 17 for SQL Server',},
    },
    'ADS': {
        'ENGINE': 'mssql',
        'NAME': os.environ['DW001_ANC'],
        'HOST': os.environ['DW001_HOST'],
        'PORT': os.environ['DW001_PORT'],
        'USER': os.environ['DW001_USER'],
        'PASSWORD': os.environ['DW001_PWD'],
        'OPTIONS': {'driver': 'ODBC Driver 17 for SQL Server',},
    },
    # 'ADS': {
    #     'ENGINE': 'mssql',
    #     'NAME': os.environ['CLOUD002_ADS'],
    #     'HOST': os.environ['CLOUD002_HOST'],
    #     'PORT': os.environ['CLOUD002_PORT'],
    #     'USER': os.environ['CLOUD002_USER'],
    #     'PASSWORD': os.environ['CLOUD002_PWD'],
    #     'OPTIONS': {'driver': 'ODBC Driver 17 for SQL Server',},
    # },
}

# this is so we can generate URLs for routes hosted by our app when it is hosted
# on Azure or any other reverse proxy.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# replace this with your deployed app's public URL
ALLOWED_HOSTS = ['to-website.azurewebsites.net', 'to-website-staging.azurewebsites.net', 'to-website-development.azurewebsites.net']
# don't allow debug on prod
DEBUG = False
