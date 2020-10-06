from flask import (Flask,request,render_template,flash,session)
from pymongo import errors
from bson.objectid import ObjectId

import tmdbsimple as tmdb
import json,os
import random
import pymongo

app = Flask(__name__)

app.secret_key = 'slfjafdaaskldfd489'

#mongodb atlas connection
client = pymongo.MongoClient("mongodb+srv://admin:admin@database.lauyn.mongodb.net/MovieReview?retryWrites=true&w=majority")
#db = client.test

#database api initial parameters
tmdb.API_KEY = 'c1bd16583e5f87b398699fddf8a8571f'
search = tmdb.Search()
base_url = "https://image.tmdb.org/t/p/original"

#movies list retreval
with open('movie_details.txt','r') as filehandle:
    movies_list = json.load(filehandle)


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('signin.html')
    else:
        sample_list = random.sample(movies_list,24)
        return render_template('home.html',data = sample_list)


@app.route('/movies')
def movies():
    if session.get('logged_in'):
        sample_list = random.sample(movies_list,24)
        return render_template('movies.html',data = sample_list)
    else:
        return render_template('signin.html',heading="Login Required!",error = "You need to Login.")

@app.route('/signin')
def signin():
    if not session.get('logged_in'):
        return render_template('signin.html')
    else:
        return render_template('thankyou.html',error="You have already Logged In.")

@app.route('/signup')
def signup():
    error = ""
    return render_template('signup.html',error = error)

#verifying the user
@app.route('/login',methods=["GET","POST"])
def login():
    error = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if client.MovieReview.Login.find_one({"email":email,"password":password}):
            error = 'Welcome to the website'
            user_data = client.MovieReview.Login.find_one({"email":email,"password":password})
            session['id']= str(user_data.get('_id'))
            session['logged_in'] = True
            sample_list = random.sample(movies_list,24)
            return render_template('home.html',data = sample_list,heading="Login Success!",error = error)
        else:
            error = 'Email or Password is Incorrect,Please Try again'
            return render_template('signin.html',error = error)
    else:
        return render_template('abort.html',error="Sorry the page you are looking is not found.")

@app.route('/signout')
def signout():
    if session.get('logged_in'):
        session['logged_in'] = False
        return render_template('signin.html',note = "Thank you!, Have A Nice Day.")
    else:
        return render_template('signin.html',heading="Login Required!",error = "You need to Login.")

@app.route('/history')
def history():
    if session.get('logged_in'):
        p = client.MovieReview.Login.find_one({"_id":ObjectId(session['id'])})
        data = p['history']
        return render_template('history.html',data=data,error = "The page is under development :(    ")
    else:
        return render_template('signin.html',heading="Login Required!",error = "You need to Login.")

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')



@app.errorhandler(404)
def page_not_found(e):
    return render_template('abort.html',error="Sorry the page you are looking is not found."),404

@app.route('/register',methods=["GET","POST"])
def register():
    error = None
    if request.method == 'POST':
        name = request.form['name']
        register_email = request.form['register_email']
        password = request.form['password']
        try:
            if client.MovieReview.Login.insert_one({"name":name,"email":register_email,"password":password}):
                heading = "Registration is Successful! "
                note = 'Now Login to the Website'
                return render_template('signin.html',heading = heading,note = note)
            else:
                error = 'There is a Server problem,Please try after sometime.'
                return render_template('signup.html',error = error)

        except errors.DuplicateKeyError:
            error = 'Email is already taken, Please Try again'
        return render_template('signup.html',error = error)
    else:
        return render_template('abort.html',error="Sorry the page you are looking is not found.")

#Movies Info
@app.route('/movie_info',methods=['GET','POST'])
def movie_info():
    if session.get('logged_in'):
        if request.method == 'POST':
            title = request.form['title']
            response = search.movie(query = title)
            if len(response['results']) == 0:
                return render_template('abort.html',error = "The Movie you are Searching is Not Found, ")
            identity = tmdb.Movies(response['results'][0]['id']).info()
            gen = identity['genres']
            str = ""
            for i in gen:
                str = str + i['name'] + ' ,'
            str = str[0:len(str)-1]
            client.MovieReview.Login.update_one(
            {"_id":ObjectId(session['id'])},
            {"$push":{"history":title}}
            )


            return render_template('movies_info.html',response = response,identity = identity,genres = str)
        elif request.method == 'GET':
            title = request.args.get('title')
            response = search.movie(query = title)
            identity = tmdb.Movies(response['results'][0]['id']).info()
            gen = identity['genres']
            str = ""
            for i in gen:
                str = str + i['name'] + ' ,'
            str = str[0:len(str)-1]
            client.MovieReview.Login.update_one(
            {"_id":ObjectId(session['id'])},
            {"$push":{"history":title}}
            )
            return render_template('movies_info.html',response = response,identity = identity,genres = str)
        else:
            return render_template('abort.html',error="Sorry the page you are looking is not found.")
    else:
        return render_template('signin.html',heading="Login Required!",error = "You need to Login.")


if __name__ == '__main__':
    app.run(debug=True)
