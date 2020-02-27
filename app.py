from flask import Flask, render_template,jsonify,request,flash,redirect,url_for
from forms import LoginForm

from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson import ObjectId



app= Flask(__name__)

app.config['SECRET_KEY']='5hfkfn89906543i'

'''client= MongoClient("mongodb://127.0.0.1:27017")
db1=client.Admin_Details
info=db1.AdminLoginInfo'''



@app.route('/login',methods=['GET', 'POST'])
def login():
    form= LoginForm()
    if form.validate_on_submit():
        flash('Log In Successful!')
        return redirect(url_for('home'))
    return render_template('login.html',form=form)


@app.route('/home',methods=['GET'])
@app.route('/',methods=['GET', 'POST'])
def home():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
