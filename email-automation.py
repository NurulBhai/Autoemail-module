import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()

    except:
        pass


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('qumar.nurool@gmail.com', '$password')
    email = EmailMessage()
    email['From'] = 'qumar.nurool@gmail.com'
    email['To'] = receiver
    email['subject'] = subject
    email.set_content(message)
    server.send_message(email)


    #server.sendmail('qumar.nurool@gmail.com', 'noorul.quamar3@gmail.com', 'Hi automation check')


email_list = {'noorul': 'noorul.quamar3@gmail.com', 'dawood' : 'dawood@gmail.com'}


def get_email_info():
    talk('To who you want to send email?')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of email?')
    subject = get_info()
    talk('Tell me the email message...')
    message = get_info()
    send_email(receiver, subject, message)
    talk('Hey Nurul, Email send successfully')
    talk('Do you want to send more email?')
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


get_email_info()
print("press Enter to exit")
