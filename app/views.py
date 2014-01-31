# -*- coding: utf-8 -*-
from flask import render_template, redirect, flash, request, session
from app import app, db
#from models import User, LessonPlan

@app.route('/', methods= ['GET', 'POST'])
@app.route('/index', methods= ['GET', 'POST'])
def index():
	weeks = range(1,17)
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
	title16= "ProgressCon: App Fair / Hire This Coder"
	titles = [title1, title2, title3, title4, title5, title6, title7, title8, title9, title10, title11, title12, title13, title14, title15, title16]
	week1lessontitles = ["The Big Picture: Why us and why now?","Setting Up for (a) Movement: Staying healthy and happy while we learn and work","Master's Tools, Remastered Tools, Native Tools: Critical-conceptual app design using things we already know",u"Our Compañeros: Meeting our larger community of support", "Relax, Reboot, Reimagine: Visioning and planning the tools we'll build in this program"]
	return render_template("index.html", weeks = weeks, title = titles, week1lessontitles = week1lessontitles)

@app.route('/lessons/<shortcode>', methods = ['GET', 'POST'])
def lesson(shortcode):
	if shortcode == "1":
		return render_template("lessonplan0101.html", shortcode=shortcode)
	if shortcode == "2":
		return render_template("lessonplan0102.html", shortcode=shortcode)
	if shortcode == "3":
		return render_template("lessonplan0103.html", shortcode=shortcode)
	if shortcode == "4":
		return render_template("lessonplan0104.html", shortcode=shortcode)
	if shortcode == "5":
		return render_template("lessonplan0105.html", shortcode=shortcode)




