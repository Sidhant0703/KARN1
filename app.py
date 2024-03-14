from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)

with app.app_context():
    db.create_all()  # Create the database tables if they don't exist

@app.route('/')
def home():
    return render_template("karn.html")

@app.route('/karn')
def karn():
    return render_template("karn1.html")

@app.route('/faq', methods=['GET', 'POST'])
def faq():
    return render_template("FAQs.html")

@app.route('/services', methods=['GET', 'POST'])
def services():
    return render_template('services.html')

@app.route('/message-us', methods=['GET', 'POST'])
def contact():
    return render_template('message-us.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')  # Use 'sign.html' for both login and registration

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('sign.html')


@app.route('/logout')
def logout():
    session.pop('email', None)  # Use 'email' for consistency
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
