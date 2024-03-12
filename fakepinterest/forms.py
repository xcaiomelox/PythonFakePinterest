#criar os formulários do site
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
from fakepinterest.models import User
class FormLogin(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    password = PasswordField("Senha", validators=[DataRequired()])
    confirm_button = SubmitField("Fazer Login")

class FormCreateAccount(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired(), Email()])
    username = StringField("Nome de usuário", validators=[DataRequired()])
    password = PasswordField("Senha", validators=[DataRequired(), Length(6,20)])
    confirm_password = PasswordField("Confirme a sua senha", validators=[DataRequired(), EqualTo("password")])
    confirm_button = SubmitField("Cadastrar conta")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            return ValidationError("E-mail já cadastrado, faça o login para continuar")

