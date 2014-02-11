# -*- coding: utf-8 -*-
from flask import render_template, redirect, flash, request, session
from app import app, db
from forms import LessonPlanForm
from models import User, LessonPlan

@app.route('/', methods= ['GET', 'POST'])
@app.route('/index', methods= ['GET', 'POST'])
def index():
	weeks = range(1,17)
	title1= "Radical Welcomings"
	title2= "Grassroots and Building Blocks"
	title3= "Doors and Phones and Code and Power"
	title4= "Code for Ordinary People... (Take It Slow): A toolkit"
	title5= "Fast, Furious Data-Driving"
	title6= "Who runs the world? urls."
	title7= "No More Drama: Project planning for peace and usability"
	title8= "For Activists Who Have Considered Leaving When the Movement is Not Enough: Another toolkit"
	title9= "Architects and Model Glue: How social-justice software sticks together"
	title10= "Empowered APIs"
	title11= "Of Hemlines and JavaScript: Designing for Humans"
	title12= "Observing, Researching, Volunteering = Amazing Code"
	title13= "Community Project: Development"
	title14= "Community Project: Development"
	title15= "Community Project: Development"
	title16= "ProgressCon: App Fair / Hire This Coder"
	titles = [title1, title2, title3, title4, title5, title6, title7, title8, title9, title10, title11, title12, title13, title14, title15, title16]
	week1lessontitles = ["Code, Power, and the Big Picture: Why us and why now?","Setting Up for (a) Movement: Staying healthy and happy while we learn and work","Master's Tools, Remastered Tools, Native Tools: Critical-conceptual app design using things we already know",u"Our Compañeros: Meeting our larger community of support", "Relax, Reboot, Reimagine: Visioning and planning the tools we'll build in this program"]
	return render_template("index.html", weeks = weeks, titles = titles, week1lessontitles = week1lessontitles)

@app.route('/lesson/<shortcode>', methods = ['GET', 'POST'])
def lesson(shortcode):
	lesson = LessonPlan.query.filter_by(shortcode = shortcode).first()
	return render_template("lesson_plan.html", lesson = lesson)


@app.route('/edit_lesson/<shortcode>', methods = ['GET', 'POST'])
def edit_lesson(shortcode):
	lesson = LessonPlan.query.filter_by(shortcode = shortcode).first()
	form = LessonPlanForm(obj=lesson)    
	if form.validate_on_submit():
		form.populate_obj(lesson)
		db.session.add(lesson)
		db.session.commit()
		return redirect('/lessons/<shortcode>')
	return render_template("edit_lesson.html", lesson = lesson, form = form)




'''
Full titles
	title1= "Radical Welcomings"
	title2= "Grassroots and Building Blocks"
	title3= "Doors and Phones and Code and Power (Looking at communities through data analysis)"
	title4= "Ordinary People... Take It Slow: (Making a really useful, simple toolkit for people who don't do code)"
	title5= "Fast and Furious Data-Driving (that Moves Lots of People)"
	title6= "Who runs the world? urls. (Digging into how the Internet works to move even more people)"
	title7= "No More Drama (Project planning for sanity and usability)"
	title8= "For Smart Activists Who Have Considered Leaving Because Tech Has Said They're Not Enough (Making another regular people toolkit)"
	title9= "Architects and Model Glue (Fitting parts together to make apps)"
	title10= "Empowered APIs (Apps that talk to each other)"
	title11= "Designing for Humans"
	title12= "Observing, Researching, Volunteering (Making sure to code an amazing Community Project by doing things that aren't coding)"
	title13= "Community Project: Development"
	title14= "Community Project: Development"
	title15= "Community Project: Development"
	title16= "ProgressCon: App Fair / Hire This Coder"'''
