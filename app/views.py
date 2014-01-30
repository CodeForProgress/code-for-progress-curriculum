from flask import render_template, redirect, flash, request, session
from app import app, db
#from models import User, LessonPlan

@app.route('/', methods= ['GET'])
@app.route('/index', methods= ['GET'])
def index():
	weeks = range(1,17)
	return render_template("index.html", weeks = weeks)
