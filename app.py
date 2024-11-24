from flask import render_template, session, redirect, url_for, flash
from models import app, InfoForm


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