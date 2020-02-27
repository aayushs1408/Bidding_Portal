from flask_wtf import FlaskForm
from wtforms import StringField,SelectField,PasswordField,SubmitField, BooleanField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):

    username= StringField('Username', validators=[DataRequired('Username can not be empty'),
    Length(min=5,max=20)])

    password = PasswordField('Password',validators=[DataRequired('Enter the Password')])

    role= SelectField('Login As',validators=[DataRequired()],choices=[('admin','Admin'),('vendor','Vendor')]) 

    login= SubmitField("Login")

    remember = BooleanField('Remember Me')