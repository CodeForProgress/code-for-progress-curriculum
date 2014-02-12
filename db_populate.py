# -*- coding: utf-8 -*-

from app import db, models

week1lessontitles = ["Code, Power, and the Big Picture: Why us and why now?","Setting Up for (a) Movement: Staying healthy and happy while we learn and work","Master's Tools, Remastered Tools, Native Tools: Critical-conceptual app design using things we already know",u"Our Compañeros: Meeting our larger community of support", "Relax, Reboot, Reimagine: Visioning and planning the tools we'll build in this program"]


title1= "Radical Welcomings"
title2= "Grassroots and Building Blocks"
title3= "Doors and Phones and Code and Power: Seeing communities through data"
title4= "Code for Ordinary People... (Take It Slow): A toolkit"
title5= "Fast, Furious Data-Driving"
title6= "Who runs the world? urls."
title7= "No More Drama: Project planning for peace and usability"
title8= "For Activists Who Have Considered Leaving When the Movement is Not Enough: Another toolkit"
title9= "Architects and Model Glue: How social-justice software sticks together"
title10= "Empowered APIs (that talk with each other)"
title11= "Of Hemlines and JavaScript: Designing for Humans"
title12= "Observing, Researching, Volunteering = Amazing Code"
title13= "Community Project: Development"
title14= "Community Project: Development"
title15= "Community Project: Development"
title16= "ProgressCon: App Fair / Hire This Coder"
weektitles = [title1, title2, title3, title4, title5, title6, title7, title8, title9, title10, title11, title12, title13, title14, title15, title16]


for week in range(1,17):
	for day in range(1,6):
		shortcode = str(week)+"-"+str(day)
		lesson = models.LessonPlan(week = week, day = day, shortcode = shortcode, weektitle = weektitles[week-1])
		if week ==1:
			lesson.title = week1lessontitles[day-1]
		db.session.add(lesson)
db.session.commit()
