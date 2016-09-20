from . import app
from . import question_view
from . import answer_view
from . import survey_view
from flask import render_template
from .models import Question


class StudentInfo:
    def __init__(self, name, sid, phone):
        self.sid = sid
        self.name = name
        if (len(sid) > 8 or len(sid) < 0):
            error_message("Invalid Student ID number")
        self.phone = phone
        self.hash = 13

    def setHash(self, newhash):
        self.hash = newhash

    def encryptedCode(self):
        hex_code = hex(self.hash * int(self.sid))
        return hex_code[2:].upper()

    def decryptCode(self, code):
        return int(code, 0) / self.hash

student_list_group = {
    "+15106935609": StudentInfo("Sophia Liu", "25233063", "+15106935609"),
    "+19165090941": StudentInfo("Bry Bach", "25024475", "+19165090941"),
    "+17609201596": StudentInfo("Madison Pauly", "24319964", "+17609201596"),
    "+17073865096": StudentInfo("Dayna Tran", "24250109",  "+17073865096"),
    "+15102834827": StudentInfo("Jo Jin Leong", "25418470", "+15102834827"),
    "+15104565229": StudentInfo("Surina Gulati", "25115313", "+15104565229")
}

student_list = [
        StudentInfo("Bry Bach", "25024475", "+19165090941"),
        StudentInfo("Surina Gulati", "25115313", "+15104565229"),
        StudentInfo("Jo Jin Leong", "25418470", "+15102834827"),
        StudentInfo("Sophia Liu", "25233063", "+15106935609"),
        StudentInfo("Madison Pauly", "24319964", "+17609201596"),
        StudentInfo("Dayna Tran", "24250109",  "+17073865096")
        ]

def get_attendance():
    rows = [str(num) for num in range(14)]
    before_class = Question.query.get(2).answers.all()
    after_class = Question.query.get(2).answers.all()
    code = [res.content for res in after_class if res.content not in rows]
    rows = [res.content for res in after_class if res.content in rows]

    return student_list

@app.route('/')
def root():
    questions = Question.query.all()
    attendance = get_attendance()
    return render_template('index.html', questions=questions, attendance=attendance)
