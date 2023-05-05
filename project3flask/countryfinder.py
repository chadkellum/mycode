#!/usr/bin/env python3
"""Project 3 for Python Class | Country API | Chad Kellum, data from https://developers.google.com/public-data/docs/canonical/countries_csv"""

import json
import random
from flask import Flask, redirect, url_for, render_template, request
import requests

with open("country.json", "r") as foo:
    data= json.load(foo)

app= Flask(__name__, template_folder='templates', static_folder='static')

@app.route("/data")
def alldata():
    return data

@app.route("/")
def landingpage():
    return render_template("countryfinder.html")

@app.route("/countrychoice", methods=["POST"])
def countrychoice():
    pick= request.form.get("countryname")
        # if a value was posted, grab that value and put it in a variable
    if pick:
        for country in data:
            if country["name"].lower() == pick.lower():
                return render_template("countrydisplay.html", countrydict= country)
        return redirect(url_for("randomcountry"))
        
    else: 
        return "Please enter a country name."

@app.route("/country")
def randomcountry():
    """returns a random country"""
    randomcountry = random.choice(data)
    return render_template("countrydisplay.html", countrydict= randomcountry)



if __name__ == "__main__":
    app.run(host= "0.0.0.0", port=2224, debug=True)
