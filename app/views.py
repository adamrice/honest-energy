from flask import render_template
from app import app
from .forms import SignUpForm
from config import GOOGLE_ANALYTICS_ID
from app.util.mailchimp_helper import add_subscriber


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = SignUpForm()

    if form.validate_on_submit():
        add_subscriber(form.email.data)
        return render_template(
            'thank_you.html',
            google_analytics_id=GOOGLE_ANALYTICS_ID
        )

    return render_template(
        'index.html',
        form=form,
        google_analytics_id=GOOGLE_ANALYTICS_ID
    )


@app.errorhandler(404)
def not_found_error(error):
    return render_template(
        '404.html',
        title='Page Not Found',
        google_analytics_id=GOOGLE_ANALYTICS_ID), 404


@app.errorhandler(500)
def internal_error(error):
    form = SignUpForm()

    return render_template(
        'index.html',
        form=form,
        google_analytics_id=GOOGLE_ANALYTICS_ID
    )
