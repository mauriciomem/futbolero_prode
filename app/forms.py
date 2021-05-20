from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms import FormField, FieldList, IntegerField, Form
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, NumberRange, InputRequired
from app.models import User
from app import connect

class LoginForm(FlaskForm):

    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Recordarme')
    submit = SubmitField('Ingresar')

class RegistrationForm(FlaskForm):

    username = StringField('Nombre de usuario', validators=[DataRequired()])
    email = StringField('Correo', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repetir Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrar')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Por favor usar otro nombre de usuario')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Por favor usar otro correo electrónico')

class EditProfileForm(FlaskForm):
    
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    fav_squad = SelectField('Fav\' Squad', choices=connect.team('PL'))
    submit = SubmitField('Guardar')

    # constructor to check if the user is logged
    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):

    # This username is saved as an instance variable, and checked in the validate_username() method.
    # If the username entered in the form is the same as the original username, 
    # then there is no reason to check the database for duplicates.
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Por favor usar otro nombre de usuario')

class BetForm(Form):
    home = IntegerField()
    away = IntegerField()

class GamblingForm(FlaskForm):
    bet = FieldList(FormField(BetForm), min_entries=10, max_entries=10)
    
    def validate_bet(form, bet):
        for field in bet.data:
            if field['home'] == None or field['away'] == None:
                raise ValidationError('Completar los campos numéricos')
            elif field['home'] < 0 or field['away'] < 0:
                raise ValidationError('Por favor completar con números Positivos')