# -*- coding: utf-8 -*-
from flask import render_template, redirect, flash, request, session
from app import app, db
from forms import LessonPlanForm
from models import User, LessonPlan

@app.route('/', methods= ['GET', 'POST'])
@app.route('/index', methods= ['GET', 'POST'])
def index():
	lessons = LessonPlan.query.order_by("week").order_by("day").all()
	return render_template("index.html", lessons = lessons)


@app.route('/lesson/<shortcode>', methods = ['GET', 'POST'])
def lesson(shortcode):
	lesson = LessonPlan.query.filter_by(shortcode = shortcode).first()
	nextlesson = LessonPlan.query.get(lesson.id+1)
	previouslesson = LessonPlan.query.get(lesson.id-1)
	return render_template("lesson_plan.html", lesson = lesson, nextlesson=nextlesson, previouslesson = previouslesson)


@app.route('/edit_lesson/<shortcode>', methods = ['GET', 'POST'])
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
