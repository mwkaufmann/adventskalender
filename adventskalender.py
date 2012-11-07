"""
THIS IS AN ADVENTSKALENDER SCRIPT.
IT WILL DISPLAY A NEW IMAGE EVERY DAY FROM 1ST DECEMBER TO 24. DECEMBER.


@author: Mario W. Kaufmann
"""

from bottle import route, get, post, run
from bottle import error, template, request, response, static_file, redirect
import datetime
import os
import re


# config stuff and sanity checks
PASSWORD = "blah"
PORT = 8080
MONTH = 11

COOKIESECRET = os.urandom(24)
SUPPORTEDFILETYPES = ["png", "jpg"]
IMAGEDIR = "static/images"

IMAGES = os.listdir(os.path.join(os.getcwd(), IMAGEDIR ))
try:
    IMAGES = sorted([int(img.split(".")[0]) for img in IMAGES])
except:
    print "image names can only contain numbers!"
    raise SystemExit

print "The following images have been loaded"
print IMAGES

if IMAGES == range(1,25):
    print "all images are ready!"
    print "STARTING"

else:
    print "not enough images"
    missingImages = list(set(range(1,25)) - set(IMAGES))
    print "please add the following images: " + str(missingImages)
    raise SystemExit


# decorator used for authentication
def checkAuth():
    """ handler for the main page of the adventskalender """
    password = request.get_cookie("password", secret=COOKIESECRET)
    if not password:
        redirect("/login")


@route('/')
def showIndex():
    checkAuth()
    """ handler for the main page of the adventskalender """
    index = open("views/adventskalender.html").read() % str(datetime.date.today().day)
    return index
    
@get("/login")
def showLogin():
    """ handler for showing the password form """
    loginText = """
    <h1>Bitte das Passwort eingeben, um den Adventskalender zu sehen</h1>
    <form action="/login" method="post">
        <input type="password" name="password" min="1" max="10">
        <input type="button" value="submit">
    </form>
    """
    return loginText

@post("/login")
def showLogin():
    """ handler for doing the actual login """
    password = request.forms.get('password')
    if password == PASSWORD:
        response.set_cookie("password", password, secret=COOKIESECRET)
        response.set_header('location', "/")
        response.status = 303
    else:
        return "Falsches Passwort! Bitte nochmal versuchen."

@error(404)
def showError404(error):
    """ redirect to root, if the requested handler does not exist """
    response.set_header('location', "/")
    response.status = 303

@route('/static/<path>')
def serveStatic(path):
    """ handler for the static files (javascript, css...) """
    return static_file(path, "./static/")

@route("/static/images/<day>")
def getImage(day):

    checkAuth()

    if "day" in day:
        return ""
    
    # check constraints
    today =  datetime.date.today()
    isDecember = today.month == MONTH 
    isChristmasTime = (today.day >= 1 and today.day <= 24)
    isNotFromTheFuture = int(day.split(".")[0]) <= today.day
    
    if isDecember and isNotFromTheFuture: 
        if os.path.isfile("static/images/" + day):
            return static_file(day, "static/images")
        elif os.path.isfile("static/images/" + day.split(".")[0] + ".jpg"):
            return static_file(day.split(".")[0] + ".jpg", "static/images")
        else:
            return "ERROR: image not found"
    else:
        return static_file("closed.jpg", "./static/")


# MAIN
if __name__ == "__main__":
    run(host='localhost', port=PORT)
