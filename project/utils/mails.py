# project/api/utils/mails.py

from flask_mail import Message
from flask import render_template, request
from project import mail


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)


def welcome_new_user(user):
    send_email("Welcome to Flask Base Api! %s" % user.username,
               sender = app.config['MAIL_SENDER'],
               recipients = [user.email],
               text_body = render_template("auth/welcome_new_user.txt",
                               user=user),
               html_body = render_template("auth/welcome_new_user.html",
                               user=user))


def password_recovery_user(user, token):
    href = request.base_url + '/' + token
    send_email("Password Recovery by Flask Base Api! %s" % user.username,
               sender='marcerossi21@gmail.com',
               recipients=['marcerossi21@gmail.com'],
               text_body=render_template("auth/password_recovery_user.txt", user=user),
               html_body=render_template("auth/password_recovery_user.html", user=user, href=href)
               #'<body>  <div> <h4><strong>Password recovery by Flask Base Api -'
               #+ user.username + '</strong></h4><h1> Click the following link to create your new password </h1><a href="' + href + '">click here</a>  </div></body>')
               )

