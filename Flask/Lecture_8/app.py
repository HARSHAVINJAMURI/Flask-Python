from flask import Flask, render_template, request, flash
from form import ContactForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'HaRSHa'

@app.route('/')
def home():
    return "Welcome to WTForms Tutorial part-2"

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if request.method == 'POST' and form.validate_on_submit():
        return 'Form Posted Successfully'
    else:
        flash('All Fields are required')
        return render_template('contact.html', form=form)

    return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
