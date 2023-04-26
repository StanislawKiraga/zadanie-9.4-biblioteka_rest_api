from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired


class BookForm(FlaskForm):
    title = StringField('Tytuł', validators=[DataRequired()])
    author = StringField('Autor', validators=[DataRequired()])
    description = TextAreaField('Opis', validators=[DataRequired()])
    read = BooleanField('Przeczytane?')  