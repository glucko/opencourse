from flask import Flask, redirect, request, url_for, blueprint
import requests

from models import User, Course, db

courses = Blueprint('courses', __name__)

@courses.route("/course", methods=["POST"])
@courses.route("/course/<int:course_id>", methods=["GET"])
def create_course():
    if request.method == "GET":
        try:
            course = Course.query.get(course_id)
            return course.to_json()
        except:
            return "Course not found", 404
  
    content = request.form['content']
    name = request.form['name']
    user_id = current_user.id
    course = Course(name=name, content=content, created_by=user_id)
    db.session.add(course)
    db.session.commit()
    return redirect(url_for("index"))

@courses.route("/courses")
def courses():
    courses = Course.query.all()
    return render_template("courses.html", courses=courses)
 #course_id=course.id, user_id=current_user.id
 #/<int:course_id>/<int:user_id>
@courses.route("/course/save", methods=["POST"])
def save_course():
    course = Course.query.get(request.form['course_id'])
    user = User.query.get(request.form['user_id'])
    user.saved_posts.coursesend(course)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for("courses"))