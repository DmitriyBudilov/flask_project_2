from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, SelectField, RadioField
from wtforms.validators import DataRequired, InputRequired, Email

class AllTeachers(FlaskForm):
    sortes_field = SelectField(choices=[("randomly","В случайном порядке"), ("best", "Сначала лучшие по рейтингу"), ("expensive", "Сначала дорогие"), ("cheap", "Сначала недорогие")])
    submit = SubmitField("Сортировать")

class MyRequest(FlaskForm):
    radio_1 = RadioField('Какая цель занятий?', choices=[("travel", "Для путешествий"), ("study", "Для школы "), ("work", "Для работы"), ("relocate", "Для переезда"), ("programming", "Для программирования")])
    radio_2 = RadioField('Сколько времени есть?', choices=[("1-2 часа в неделю", "1-2 часа в неделю"), ("3-4 часа в неделю", "3-4 часа в неделю"), ("5-6 часов в неделю", "5-6 часов в неделю"), ("6-7 часов в неделю", "6-7 часов в неделю"), ("8-10 часов в неделю", "8-10 часов в неделю")])
    name = StringField('Вас зовут', [DataRequired()])
    phone = StringField('Ваш телефон', [DataRequired()])
    submit = SubmitField('Найдите мне преподавателя')

class Booking(FlaskForm):
    name = StringField('Вас зовут', [DataRequired()])
    phone = StringField('Ваш телефон', [DataRequired()])
    submit = SubmitField('Записаться на пробный урок')