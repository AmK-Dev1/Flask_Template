from flask_mail import Mail, Message
from flask import Flask  # Import Flask

class SMTPMailer:
    def __init__(self, app=None):
        """Initialize mailer with a Flask app."""
        self.mail = None
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Configure and initialize Flask-Mail."""
        app.config['MAIL_SERVER'] = 'smtp.gmail.com'
        app.config['MAIL_PORT'] = 587
        app.config['MAIL_USE_TLS'] = True
        app.config['MAIL_USE_SSL'] = False
        app.config['MAIL_USERNAME'] = 'email'
        app.config['MAIL_PASSWORD'] = 'password'  # Use an App Password, NOT your Gmail password!
        app.config['MAIL_DEFAULT_SENDER'] = NULL

        self.mail = Mail(app)

    def send_email(self, to, subject, body):
        """Send an email using Flask-Mail."""
        if not self.mail:
            raise ValueError("Mail instance is not initialized. Call init_app(app) first.")

        msg = Message(subject, recipients=[to], body=body)
        self.mail.send(msg)
        return "Email sent successfully!"

