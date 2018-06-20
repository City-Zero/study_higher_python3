# coding=utf-8
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/upload',methods=['POST'])
def post():
    return str(request.files) +'\n' +  str(request.form)

if __name__ == '__main__':
    app.run(debug=True)