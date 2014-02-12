from app import db
import datetime

class User(db.Model):
    __tablename__ = 'User'
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
	__tablename__ = 'LessonPlan'
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.Text)
	weektitle = db.Column(db.Text)
	week = db.Column(db.Integer)
	day = db.Column(db.Integer)
	shortcode = db.Column(db.String) #i.e. Lesson 5 on Week 3 is 03-05
	projectedDate = db.Column(db.String(40))
	instructors = db.Column(db.String(200), default = "Rahman")
	learningOutcome1 = db.Column(db.Text)
	learningOutcome2 = db.Column(db.Text)
	learningOutcome3 = db.Column(db.Text)
	learningOutcome4 = db.Column(db.Text)
	learningOutcome5 = db.Column(db.Text)
	learningOutcome6 = db.Column(db.Text)
	learningOutcome7 = db.Column(db.Text)
	learningOutcome8 = db.Column(db.Text)
	learningOutcome9 = db.Column(db.Text)
	learningOutcome10 = db.Column(db.Text)
	prep = db.Column(db.Text)
	materials = db.Column(db.Text)
	participantMaterials = db.Column(db.Text)
	time1 = db.Column(db.String(20), default = "9am-9:15am")
	time2 = db.Column(db.String(20))
	time3 = db.Column(db.String(20))
	time4 = db.Column(db.String(20))
	time5 = db.Column(db.String(20))
	time6 = db.Column(db.String(20))
	time7 = db.Column(db.String(20))
	time8 = db.Column(db.String(20))
	time9 = db.Column(db.String(20))
	time10 = db.Column(db.String(20), default = "4:45pm-5pm")
	activity1 = db.Column(db.String, default = "Start and overview today's schedule")
	activity2 = db.Column(db.String)
	activity3 = db.Column(db.String)
	activity4 = db.Column(db.String)
	activity5 = db.Column(db.String)
	activity6 = db.Column(db.String)
	activity7 = db.Column(db.String)
	activity8 = db.Column(db.String)
	activity9 = db.Column(db.String)
	activity10 = db.Column(db.String, default = "Closeout exercise and recap needs for tomorrow")
	trainernotes = db.Column(db.Text)
