from crypt import methods
from distutils.log import debug
from re import template
# from django.shortcuts import redirect, render 
from flask import Flask, render_template, request, url_for, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('modal.html')

@app.route('/success/<user>')
def success(user):
    return render_template('callender.html', user=user)

@app.route('/login', methods=['POST', 'GET'])
def check_cred():
    if request.method == 'POST':
        user = request.form['uname']
        pwd = request.form['pswd']
        if user == "admin" and pwd == "hello":
            return redirect(url_for('success',user = user))
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
