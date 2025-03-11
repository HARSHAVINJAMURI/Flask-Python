from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html',content='Flask Tutorials started')

@app.route('/index')
def index():
    return render_template('index.html',content="content page through python file") 

@app.route('/list')
def list():
    return render_template('list.html',content=['ML',"DL","AI","Py"])

if __name__=='__main__':
    app.run(debug=True)