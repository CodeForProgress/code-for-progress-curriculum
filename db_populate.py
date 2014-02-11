from app import db, models

for week in range(1,17):
	for day in range(1,6):
		if week <=9:
			shortcode = "0"+str(week)+"-0"+str(day)
		else:
			shortcode = str(week)+"-0"+str(day)
		lesson = models.LessonPlan(week = week, day = day, shortcode = shortcode)
		db.session.add(lesson)

db.session.commit()

