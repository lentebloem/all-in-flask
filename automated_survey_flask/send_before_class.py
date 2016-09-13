# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "AC2a7fd23053a652eed46e874124bda301"
auth_token = "37950282565a26a01034b0c2b47c7652"
client = TwilioRestClient(account_sid, auth_token)
test_phone = "+15005550006"

class StudentInfo:

    def __init__(self, name, sid, phone, phone2 = None):
        self.name = name
        self.sid = sid
        self.phone = phone
        self.phone2 = phone2
        self.hash = 13

    def setHash(self, newhash):
        self.hash = newhash

    def encryptedCode(self):
        hex_code = hex(self.hash * self.sid)
        return hex_code[2:].upper()

    def decryptCode(self, code):
        return int(code, 0) / self.hash

    def sendCode(self):
        phone = self.phone
        message = client.messages.create(to=self.phone, from_=test_phone, body="Hello " + self.name + "! Your code is " + self.encryptedCode())
        print(message.sid)


# testing
# student_list is a dictionary. key: phone number; value: StudentInfo object
student_list_test = {"+15106935609": StudentInfo("Sophia Liu", 25233063, "+15106935609")}

student_list_group = {
    "+15106935609": StudentInfo("Sophia Liu", 25233063, "+15106935609"),
    "+19165090941": StudentInfo("Bry Bach", 25024475, "+19165090941"),
    "+17609201596": StudentInfo("Madison Pauly", 24319964, "+17609201596"),
    "+17073865096": StudentInfo("Dayna Tran", 24250109,  "+17073865096"),
    "+15102834827": StudentInfo("Jo Jin Leong", 25418470, "+15102834827"),
    "+15104565229": StudentInfo("Surina Gulati", 25115313, "+15104565229")
}
# callers = {
#     "+15106935609": "Sophia Liu",
#     "+19165090941": "Bry Bach",
#     "+17609201596": "Madison Pauly",
#     "+17073865096": "Dayna Tran",
#     "+15102834827": "Jo Jin Leong",
#     "+15104565229": "Surina Gulati",
# }

for student in student_list_test:
    student_list[student].sendCode()
