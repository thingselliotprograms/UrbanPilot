
from flask import Flask, render_template, request, jsonify, redirect, url_for, Response, make_response
from flask_sqlalchemy import SQLAlchemy

import os
import requests

clientKey = 'kfaYZm8NDkrYyPX2MEuZ9kt0ynEWY1ejhohhLq5pLwojmll9ZP99aDaI1PFZQUi8'

app = Flask(__name__)

POSTGRES = {
    'user': 'postgres',
    'pw': 'database',
    'db': 'urban_pilot',
    'host': 'localhost',
    'port': '5432'
    }

app.config.update(
    DEBUG = True,
    TESTING = False,
    CSRF_ENABLED = True,
    SECRET_KEY = 'urban-pilot-secret-key'
    )
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


import models


# Make the WSGI interface available at the top level so wfastcgi can get it.
#wsgi_app = app.wsgi_app


@app.route('/')
def index():
    return redirect(url_for('signup'))

@app.route('/signup', methods=['GET','POST'])
def signup():

    if request.method == 'GET':
        return render_template("signup.html")
    elif request.method =='POST':

        
        fname = request.form.get('fname')
        mname = request.form.get('mname')
        lname = request.form.get('lname')
        zip = request.form.get('zip')
        email = request.form.get('email')


        submission = models.InfoSubmission(
            fname = fname,
            mname = mname,
            lname = lname,
            zip = zip,
            email = email,
            city = "",
            county = "",
            state = ""
            )

        db.session.add(submission)

        try:
            db.session.commit()
            userinfo = db.session.query(models.InfoSubmission).filter(models.InfoSubmission.email == email).one()
            infoJSON = userinfo.toJSON

            zipcode =  str(infoJSON['zip'])
            print (infoJSON['zip'])
            callstring =  "https://www.zipcodeapi.com/rest/"+clientKey+"/info.json/" + zipcode + "/radians"
            r = requests.get(callstring)
            print (r.json())
            resp = r.json()
            if 'error_msg' in resp:
                pass
            else:
                respcity = resp['city']
                respstate = resp['state']
                userinfo.city = respcity
                userinfo.state = respstate
                db.session.add(userinfo)
                db.session.commit()
            res = make_response(jsonify(infoJSON), 202)
            return res
        except:
            res = make_response("Error", 400)
            return res

@app.route('/ranklocations' , methods=['POST'])
def rank_locations():
    zips = db.session.query(models.InfoSubmission.zip).distinct()
    zipscount = db.session.query(models.InfoSubmission).count()
    print (zipscount)
    db.session.query(models.LocationRanks).delete()
    db.session.commit()
    for zip in zips:
        print (zip[0])
        zipcount = db.session.query(models.InfoSubmission).filter(models.InfoSubmission.zip == zip[0]).count()
        print (zipcount)
        print ((float(zipcount)/zipscount)*100)

        locationrank = models.LocationRanks(
            zip = zip[0],
            total = zipcount,
            portion = ((float(zipcount)/zipscount)*100)
            )
        db.session.add(locationrank)
        db.session.commit()


    return make_response("OK",200)


if __name__ == '__main__':
    HOST = 'localhost'
    PORT = 5000
    app.run(HOST, PORT,debug=True)

