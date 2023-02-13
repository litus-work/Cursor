from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    name = StringField('Product name', [validators.Length(min=4, max=25)])
    description = StringField('Description', [validators.Length(min=6, max=350)])
    price = StringField('Product price', [validators.NumberRange(min=1, max=5, message=None)])
    img_name = StringField('img_name', [validators.Length(min=4, max=25)])
    id = StringField('Product id', [validators.UUID(message=None)])

