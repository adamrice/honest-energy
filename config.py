import os

basedir = os.path.abspath(os.path.dirname(__file__))

ENV = os.environ.get('ENV', 'test')

DEBUG = False if ENV == 'production' else True

WTF_CSRF_ENABLED = True
SECRET_KEY = os.environ.get('SECRET_KEY', 'xxxyyyzzz111222333')

GOOGLE_ANALYTICS_ID = os.environ.get('GOOGLE_ANALYTICS_ID', 'UA-XXXXX-X')

MAILCHIMP_USERNAME = os.environ.get('MAILCHIMP_USERNAME')
MAILCHIMP_SECRET_KEY = os.environ.get('MAILCHIMP_SECRET_KEY')
# MailChimp email lists
MAILCHIMP_LISTS = {
    'Leads': 'c3fa5fc97b',
}
