from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app=Flask(__name__)
app.config['SECRET_KEY']='HARSHA'

class ContactForm(FlaskForm):
    name=StringField("What's is your name?", validators=[DataRequired()])
    submit=SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():
    form=ContactForm()
    name=None
    if form.validate_on_submit():
        name=form.name.data
        form.name.data=' '
    return render_template('index.html',contact=form,name=name)
if __name__ =='__main__':
    app.run(debug=True)  