# -*- coding: utf-8 -*-
from flask import render_template, redirect, flash, request, session, g, url_for
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm
from forms import LessonPlanForm, LoginForm
from models import User, LessonPlan


@lm.user_loader
def load_user(id):
	return User.query.get(int(id))

@app.route('/login', methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = form.get_user()
		login_user(user)
		return redirect(url_for('index'))
	return render_template('login.html', form = form)



@app.route('/', methods= ['GET', 'POST'])
@app.route('/index', methods= ['GET', 'POST'])
@login_required
def index():
	lessons = LessonPlan.query.order_by("week").order_by("day").all()
	return render_template("index.html", lessons = lessons)


@app.route('/lesson/<shortcode>', methods = ['GET', 'POST'])
@login_required
def lesson(shortcode):
	lesson = LessonPlan.query.filter_by(shortcode = shortcode).first()
	nextlesson = LessonPlan.query.get(lesson.id+1)
	previouslesson = LessonPlan.query.get(lesson.id-1)
	return render_template("lesson_plan.html", lesson = lesson, nextlesson=nextlesson, previouslesson = previouslesson)


@app.route('/edit_lesson/<shortcode>', methods = ['GET', 'POST'])
@login_required
def edit_lesson(shortcode):
	lesson = LessonPlan.query.filter_by(shortcode = shortcode).first()
	nextlesson = LessonPlan.query.get(lesson.id+1)
	previouslesson = LessonPlan.query.get(lesson.id-1)
	form = LessonPlanForm(obj=lesson)    
	if form.validate_on_submit():
		form.populate_obj(lesson)
		db.session.add(lesson)
		db.session.commit()
		return redirect('/index')
	return render_template("edit_lesson.html", lesson = lesson, form = form, previouslesson = previouslesson, nextlesson=nextlesson)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
