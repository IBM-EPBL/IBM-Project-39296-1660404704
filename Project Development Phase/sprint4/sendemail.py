import smtplib
import sendgrid as sg
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, To, Content
SUBJECT = "personal expense tracker"
s = smtplib.SMTP('smtp.gmail.com', 587)

def sendmail(TEXT,email):
    from_email = Email("elson2534126@gmail.com") 
    to_email = To(email) 
    subject = "Sending with SendGrid is Fun"
    content = Content("text/plain",TEXT)
    mail = Mail(from_email, to_email, subject, content)
    try:
        sg=SendGridAPIClient('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')
        response = sg.send(mail)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)
    # print("sorry we cant process your candidature")
    # s = smtplib.SMTP('smtp.gmail.com', 587)
    # s.starttls()
    # # s.login("il.tproduct8080@gmail.com", "oms@1Ram")
    # s.login("tour7107@gmail.com", "1234567890123456")
    # message  = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    # # s.sendmail("il.tproduct8080@gmail.com", email, message)
    # s.sendmail("tour7107@gmail.com", email, message)
    # s.quit()
# def sendgridmail(user,TEXT):
  
#     # # from_email = Email("shridhartp24@gmail.com")
#     # from_email = Email("tour7107@gmail.com") 
#     # to_email = To(user) 
#     # subject = "Sending with SendGrid is Fun"
#     # content = Content("text/plain",TEXT)
#     # mail = Mail(from_email, to_email, subject, content)

#     # # Get a JSON-ready representation of the Mail object
#     # mail_json = mail.get()
#     # # Send an HTTP POST request to /mail/send
#     # response = sg.client.mail.send.post(request_body=mail_json)
#     # print(response.status_code)
#     # print(response.headers)
#     message = Mail(
#     from_email='tour7107@gmail.com',
#     to_emails='mani.deepthi2001@gmail.com',
#     subject='Sending with Twilio SendGrid is Fun',
#     html_content='<strong>and easy to do anywhere, even with Python</strong>')
# try:
#     sg=SendGridAPIClient('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')
#     response = sg.send(message)
#     print(response.status_code)
#     print(response.body)
#     print(response.headers)
# except Exception as e:
#     print(e)
