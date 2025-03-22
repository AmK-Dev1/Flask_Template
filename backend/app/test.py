from flask import Flask
from mailer import SMTPMailer  # Import your SMTPMailer class
from utils import generate_confirmation_code
# Step 1: Create a Flask app instance
app = Flask(__name__)

# Step 2: Initialize mailer with Flask app
mailer = SMTPMailer()
mailer.init_app(app)  # Manually initialize app settings

# Step 3: Create a test function to send an email
def test_email():
    recipient_email = "anis.mokhtari2005@gmail.com"  # Replace with a valid email
    subject = "Welcome to Baraka"
    code = generate_confirmation_code()
    body = f"Hello ANIS! \n Here you are your confimation code : {code} (Please do not share it)."

    with app.app_context():  # Required for Flask-Mail to work outside Flask routes
        result = mailer.send_email(recipient_email, subject, body)
        print(result)

# Step 4: Run the test function
if __name__ == "__main__":
    test_email()
