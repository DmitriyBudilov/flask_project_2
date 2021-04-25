from flask import render_template, request, redirect, url_for
import os
import json
import random

from app import app, db
from app.data import goals, teachers
from app.forms import AllTeachers, MyRequest, Booking
from app.models import Goal, Teacher, Request

def read_teachers_from_file(file):
    with open(os.path.join(os.getcwd(), file), "r") as json_file:
        teachers = json.load(json_file)
    return teachers

@app.route('/', methods=["GET"])
def index():
    teachers = db.session.query(Teacher).all()
    random.shuffle(teachers)
    return render_template('index.html', goals=goals, teachers=teachers[:6])

@app.route('/all/', methods=["GET", "POST"])
def all():
    teachers = db.session.query(Teacher).all()
    form = AllTeachers()
    if request.method == "POST":
        return render_template('all.html', teachers=teachers, form=form, sorting=request.form["sortes_field"])
    else:
        random.shuffle(teachers)
        return render_template('all.html', teachers=teachers, form=form, sorting="randomly")

@app.route('/profile/<int:id>/')
def profile(id):
    teacher = db.session.query(Teacher).filter(Teacher.id==id).first()
    return render_template('profile.html', teacher=teacher)

@app.route('/booking/<int:id>/<string:day>/<int:time>/', methods=["GET", "POST"])
def booking(id, day, time):
    form = Booking(request.form)
    teacher = db.session.query(Teacher).filter(Teacher.id==id).first()
    if request.method == "POST" and form.validate_on_submit():
        with open("booking.json", "r") as json_file:
            data_from_json_file = json_file.read()
            if data_from_json_file != '':
                content = json.loads(data_from_json_file)
            else:
                content = []
        data_from_form = {"name": form.name.data, "phone number": form.phone.data, "day": day, "time": time}
        content.append(data_from_form)
        with open("booking.json", "w") as json_file:
            json.dump(content, json_file, indent=4, ensure_ascii=False)
        return render_template('booking_done.html', day=day, time=time, name=form.name.data, phone=form.phone.data)

    return render_template('booking.html', form=form, teacher=teacher, day=day, time=time)

@app.route('/booking_done/', methods=["POST"])
def booking_done():
    form = Booking(request.form)
    teachers = read_teachers_from_file("data.json")
    if request.method == "POST" and form.validate_on_submit():
        print('qweqew')
        for teacher in teachers:
            if teacher["id"] == id:
                print('qweqew')
        return render_template('booking_done.html')
    return render_template('booking_done.html')

@app.route('/goal/<string:id>')
def goal(id):
    goal = db.session.query(Goal).filter(Goal.goal==id).first()
    teachers = goal.teachers
    return render_template('goal.html', teachers=teachers, goal=goal)

@app.route('/request/', methods=["GET", "POST"])
def render_request():
    form = MyRequest(request.form)
    if request.method == "POST" and form.validate_on_submit():
        req_post = Request(name=form.name.data, phone=form.phone.data, goal=form.radio_1.data, duration=form.radio_2.data)
        db.session.add(req_post)
        db.session.commit()
        goal = db.session.query(Goal).filter(Goal.goal==form.radio_1.data).first()
        return render_template('request_done.html', goal=goal, data=form.data)
    return render_template('request.html', form=form)

@app.errorhandler(404)
def http_404_handler(error):
    return "<p><h1>404 Страница не найдена</h1></p>", 404

@app.errorhandler(500)
def http_500_handler(error):
    return "<p><h1> 500 Ошибка сервера</h1></p>", 500

@app.route('/add_to_db/')
def add_to_db():
    for key, goal in goals.items():
        value = Goal(goal=key,
                     title=goal["title"],
                     symbol=goal["symbol"])
        db.session.add(value)
    db.session.commit()
    for teacher in teachers:
        value = Teacher(name=teacher['name'],
                        about=teacher['about'],
                        rating=teacher['rating'],
                        picture=teacher['picture'],
                        price=teacher['price'],
                        free=teacher['free'],
                        goals=[db.session.query(Goal).filter(Goal.goal==item).first() for item in teacher['goals']])
        # db.session.add(value)
    db.session.commit()
    return redirect(url_for('index'))