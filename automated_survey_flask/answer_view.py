from . import app, db
from .models import Question, Answer
from flask import url_for, request, session
from twilio import twiml
from twilio.rest import TwilioRestClient

account_sid = "AC2a7fd23053a652eed46e874124bda301"
auth_token = "37950282565a26a01034b0c2b47c7652"
client = TwilioRestClient(account_sid, auth_token)
test_phone = "+15005550006"

class StudentInfo:

    def __init__(self, sid, phone):
        self.sid = sid
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


@app.route('/answer/<question_id>', methods=['POST'])
def answer(question_id):
    question = Question.query.get(question_id)

    db.save(Answer(content=extract_content(question),
                   question=question,
                   session_id=session_id(),
                   phone_number=get_phone_number()))

    send_enrypted_code_twiml(question_id)
    next_question = question.next()
    redirect_twiml(next_question)
    else:
        return


def extract_content(question):
    if is_sms_request():
        return request.values['Body']
    elif question.kind == Question.TEXT:
        return 'Transcription in progress.'
    else:
        return request.values['Digits']


def redirect_twiml(question):
    response = twiml.Response()
    response.redirect(url_for('question', question_id=question.id),
                      method='GET')
    return str(response)


def send_enrypted_code_twiml(question_id):
    response = twiml.Response()
    sid = extract_content(Question.query.get(question_id))
    if is_sms_request():
        response.message("Thank you for attending the lecture! Your code is " + StudentInfo(sid, get_phone_number()).encryptedCode())
        redirect_twiml(next_question)
    else:
        response.say("Thank you for attending the lecture! Your code is " + StudentInfo(sid, get_phone_number()).encryptedCode())
        response.hangup()
    if 'question_id' in session:
        del session['question_id']
    return str(response)


def is_sms_request():
    return 'MessageSid' in request.values.keys()


@app.route('/answer/transcription/<question_id>', methods=['POST'])
def answer_transcription(question_id):
    session_id = request.values['CallSid']
    content = request.values['TranscriptionText']
    phone_number = request.values['PhoneNumber']
    Answer.update_content(session_id, question_id, content, phone_number)
    return ''

def session_id():
    return request.values.get('CallSid') or request.values['MessageSid']

def get_phone_number():
    print(request.values.get('From', None))
    return request.values.get('From', None) or request.values['PhoneNumber']

def error_message(msg):
    response = twiml.Response()
    if is_sms_request():
        response.message(msg)
    else:
        response.say(msg)
        response.hangup()
    return
