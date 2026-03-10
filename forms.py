from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField
from wtforms import EmailField
from wtforms import validators


class UserForm(Form):
    id = IntegerField('Id')

    nombre = StringField('Nombre', [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=50)
    ])

    apellidos = StringField('Apellidos', [
        validators.DataRequired(message='El campo es requerido')
    ])

    telefono = StringField('Teléfono', [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=10, max=15)
    ])

    email = EmailField('Correo', [
        validators.Email(message='Ingrese un correo valido')
    ])


class MaestroForm(Form):

    matricula = IntegerField('Matricula')

    nombre = StringField('Nombre', [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=50)
    ])

    apellidos = StringField('Apellidos', [
        validators.DataRequired(message='El campo es requerido')
    ])

    especialidad = StringField('Especialidad', [
        validators.DataRequired(message='El campo es requerido')
    ])

    email = EmailField('Correo', [
        validators.Email(message='Ingrese un correo valido')
    ])