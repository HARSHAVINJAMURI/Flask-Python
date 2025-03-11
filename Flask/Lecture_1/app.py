from flask import Flask,redirect ,url_for
app=Flask(__name__)

@app.route('/')
def home():
    return "<h1> Welcome to the Harsha Learning Place</h1>"

@app.route('/course')
def course():
    return "Welcome to the Free courses"

@app.route('/<name>')
def name(name):
    return f"Hello {name}!"

@app.route('/admin')
def admin():
    return redirect(url_for('/'))

@app.route('/other')
def other():
    return redirect('/')


if __name__=='__main__':
    app.run(debug=True)