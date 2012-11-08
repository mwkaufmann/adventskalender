Adventskalender Webapp
===============

![Screenshot of the Adventskalender Webapp](https://github.com/mwkaufmann/adventskalender/blob/master/adventskalender.png)

Overview
---------------

Adventskalender is a little *webapp* which brings the old German Christmas tradition of *Adventskalenders* into the digital age.

For more information about Adventskalenders read the [Wikipedia Entry.](http://en.wikipedia.org/wiki/Advent_calendar)

The app grants access to a new picture every day during the Christmas month (the time from december 1st to december 24th).

Features
---------------

- password protected
- somewhat easy to deploy ;)

Requirements
---------------
- a python interpreter installed on your system
- a current webbrowser (tested in Chrome and Firefox)


History
---------------

I created this app in 2010 for my girlfriend and filled it with pictures of both of us that I collected over the year.
It was a great success. :)

Since then I completely changed the technology stack before redeploying it every year.
Why? Because it's fun.

Here are the relevant evolution steps.

1.0 (2010)

- python cgi in the backend
- simple javascript in the frontend

1.1 (2011)

- python tornado web in the backend
- jQuery in the frontend

1.2 (2012) NOW

- python bottle.py in the backend
- jQuery and angular.js in the frontend

1.3 (2013) FUTURE

- work on the design (add free Christmas graphics)
- thinking about turning thins into an android application (if I can convince the gf to trade her old phone for a smart one)


How do I get started?
---------------

Just clone the app
  
    git clone https://github.com/mwkaufmann/adventskalender.git

Add your own pictures to static/images folder.
The pictures need to be names 1.png to 24.png (jpg is also possible and will be detected automatically).
If there are pictures missing, the script will not start and tell you which ones are missing.

Open adventskalender.py and customize the following parameters
  
    PASSWORD = "yourPassword"
    PORT = 80
    MONTH = 12 

Start the app with
  
    python adventskalender.py

If no errors are shown, point your browser to
  
    http://localhost

Have fun and a happy winter solstice! ;)
