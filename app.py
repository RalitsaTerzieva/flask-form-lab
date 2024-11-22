import os
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, RadioField, SelectField, TextAreaField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db) 

class Puppy(db.Model):

    __tablename__ = 'puppies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer)

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Puppy {self.name} is {self.age} year/s old."

class InfoForm(FlaskForm):

    breed = StringField("What breed are you?", validators=[DataRequired()])
    neutered = BooleanField("have you been neutered?")
    mood = RadioField("Please choose your mood:", choices=[("mood_one", "Happy"), ("mood_two", "Excited")])
    food_choice = SelectField("Pick your favourite food:", choices=[('chi', 'Chicken'), ('bf', 'Beef'), ('fish', 'Fish')])
    feedback = TextAreaField()
    submit = SubmitField("Submit")


@app.route('/', methods=["GET", "POST"])
def index():
    breed = False
    form = InfoForm()

    if form.validate_on_submit():
        flash("You just clicked the button!")

        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data
       
        return redirect(url_for('thankyou'))

    return render_template('index.html', form=form, breed=breed)

@app.route('/thank-you')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)