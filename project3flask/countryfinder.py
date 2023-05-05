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
    
    url = "http:/127.0.0.1:2224/data"
    response= requests.get(url)

    data= response.json()

    for country in data:
        print(f"""{country['name']} -- {country['country']}, 
        {country['latitude']}, {country['longitude']}""")
        

@app.route("/")
def landingpage():
    return render_template("countryfinder.html")

@app.route("/countrychoice", methods=["POST"])
def countrychoice():
    pick= request.form.get("countryname")
        # if a value was posted, grab that value and put it in a variable
    if pick:
        for country in data:
            if country["name"] == pick:
                return json.dumps(country)
        return redirect(url_for(randomcountry))
        
    else: 
        return "Please enter a country name."
            


@app.route("/country")
def randomcountry():
    """returns a random country"""
    if request.form["country"]:
        randomcountry = random.choice(country)
    return json.dumps(randomcountry)

flag= f'<img src="https://flagsapi.com/{'country'}/flat/64.png" />'

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port=2224, debug=True)
