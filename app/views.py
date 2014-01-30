# -*- coding: utf-8 -*-
from flask import render_template, redirect, flash, request, session
from app import app, db
#from models import User, LessonPlan

@app.route('/', methods= ['GET', 'POST'])
@app.route('/index', methods= ['GET', 'POST'])
def index():
	weeks = range(1,17)
	titles = ["Radical Welcomings"]
	week1lessontitles = ["The Big Picture: Why us and why now?","Setting Up for (a) Movement: Staying healthy and happy while we learn and work","Master's Tools, Remastered Tools, Native Tools: Coding our first social justice app from things we know",u"Our Compañeros: Meeting our larger community of support", "Relax, Reboot, Reimagine: Visioning and planning the tools we'll build in this program"]
	return render_template("index.html", weeks = weeks, title = titles, week1lessontitles = week1lessontitles)

@app.route('/lessons/<shortcode>', methods = ['GET', 'POST'])
def lesson(shortcode):
	return render_template("lesson_plan.html")
