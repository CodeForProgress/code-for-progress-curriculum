
from app import db
import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(45), unique=True)
    password = db.Column(db.String(45))
    firstname = db.Column(db.String(45))
    lastname = db.Column(db.String(45))
    role = db.Column(db.Integer)    #Role = 0 is the superuser, #Role 1 is CFP staff, #Role = 2 guestinstructor

    def __repr__(self):
        return '<User %r>' % (self.email)

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.user_id

    def __unicode__(self):
        return self.email
        

class LessonPlan(db.Model):
	week = db.Column(db.Integer)
	day = db.Column(db.Integer)
	shortcode = db.Column(db.String) #i.e. Lesson 5 on Week 3 is 03-05
	projectedDate = db.Column(db.String(20))
	instructors = db.Column(db.String(200), default = "Aliya")
	learningOutcomes = db.Column(db.Text)
	materials = db.Column(db.Text)
	content = db.Column(db.Text)
