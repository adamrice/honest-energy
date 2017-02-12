from flask_wtf import Form
from wtforms.fields.html5 import EmailField
from wtforms import validators

class SignUpForm(Form):
    email = EmailField('email', validators=[
        validators.DataRequired(),
        validators.Email()
        ]
    )
