from flask.ext.wtf import Form
from app import db
from models import User, LessonPlan
from wtforms import TextField, TextAreaField, DateField, SelectField, PasswordField
from wtforms.validators import Required, Email, EqualTo, Length, ValidationError, Optional


class LoginForm(Form):
	email = TextField('email', validators = [Required(message="We need to know your email address.")])
	password = PasswordField('password', validators = [Required(message="We need your password.")])

	def validate_email(self, field):
		user = self.get_user()
		if user is None:
			raise ValidationError('Invalid User')
		if user.password != self.password.data:
			raise ValidationError('Invalid Password')
			
	def get_user(self):
		return db.session.query(User).filter_by(email=self.email.data).first()


class LessonPlanForm(Form):
	title = TextField('title', validators = [Required()])
	projectedDate = TextField('projectedDate', validators =[])
	instructors = TextField('instructors', validators =[])
	learningOutcome1 = TextField('outcome1', validators = [])
	learningOutcome2 = TextField('outcome2', validators = [])
	learningOutcome3 = TextField('outcome3', validators = [])
	learningOutcome4 = TextField('outcome4', validators = [])
	learningOutcome5 = TextField('outcome5', validators = [])
	learningOutcome6 = TextField('outcome6', validators = [])
	learningOutcome7 = TextField('outcome7', validators = [])
	learningOutcome8 = TextField('outcome8', validators = [])
	learningOutcome9 = TextField('outcome9', validators = [])
	learningOutcome10 = TextField('outcome10', validators = [])
	prep = TextAreaField('prep', validators = [])
	materials = TextAreaField('materials', validators = [])
	participantMaterials = TextAreaField('studentMaterials', validators = [])
	time1 = TextField('time1', validators = [])
	time2 = TextField('time2', validators = [])
	time3 = TextField('time3', validators = [])
	time4 = TextField('time4', validators = [])
	time5 = TextField('time5', validators = [])
	time6 = TextField('time6', validators = [])
	time7 = TextField('time7', validators = [])
	time8 = TextField('time8', validators = [])
	time9 = TextField('time9', validators = [])
	time10 = TextField('time10', validators = [])
	activity1 = TextField('activity1', validators = [])
	activity2 = TextField('activity2', validators = [])
	activity3 = TextField('activity3', validators = [])
	activity4 = TextField('activity4', validators = [])
	activity5 = TextField('activity5', validators = [])
	activity6 = TextField('activity6', validators = [])
	activity7 = TextField('activity7', validators = [])
	activity8 = TextField('activity8', validators = [])
	activity9 = TextField('activity9', validators = [])
	activity10 = TextField('activity10', validators = [])
	activity1notes = TextAreaField('activity1', validators = [])
	activity2notes = TextAreaField('activity2', validators = [])
	activity3notes = TextAreaField('activity3', validators = [])
	activity4notes = TextAreaField('activity4', validators = [])
	activity5notes = TextAreaField('activity5', validators = [])
	activity6notes = TextAreaField('activity6', validators = [])
	activity7notes = TextAreaField('activity7', validators = [])
	activity8notes = TextAreaField('activity8', validators = [])
	activity9notes = TextAreaField('activity9', validators = [])
	activity10notes = TextAreaField('activity10', validators = [])
	trainernotes = TextAreaField('trainernotes', validators = [])
