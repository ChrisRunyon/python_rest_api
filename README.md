# python restful api

#### Summary: 
Don't over-engineer your app.

This Python REST API is a game called Mastermind. The goal is simple; try to guess the correct sequence using the colors: 'RED', 'ORANGE', 'YELLOW', 'GREEN', 'BLUE', 'PURPLE', 'WHITE', 'BLACK'.  

#### Dependencies:
You will need Python 2.7, Flask, Flask-RESTful  

#### Recommended reading:
Everything here can be found in the documentation provided. 

[](http://)
	[https://www.python.org/](https://www.python.org/)  
[](http://)
	[http://flask.pocoo.org/](http://flask.pocoo.org/)  
[](http://)	
	[https://pypi.python.org/pypi/Flask-RESTful](https://pypi.python.org/pypi/Flask-RESTful)  


#### Usage: 

Install Python 2.7, Flask, and Flask-Restful. Once installed use the command line to start. 

#### RUN: 
``` python
	python app.py
``` 

Your server should now be running at http://localhost:5000

The AI will generate a sequence that is written to a file called 'secretcode'. This file contains the answer. 

The REST API has three endpoints.

#### TEST:
[](http://)
	[http://localhost:5000/test](http://localhost:5000/test) Use this to test that your server is working correctly.

#### START:
[](http://)
	[http://localhost:5000/start](http://localhost:5000/start) Use this to have the AI generate the answer.

#### GUESS:
[](http://)
	[http://localhost:5000/guess](http://localhost:5000/guess<string:answer>) Use this to guess the correct sequence.

### EXAMPLE:

[](http://)
	[http://localhost:5000/guess?RED,BLUE,GREEN,WHITE,BLACK](http://localhost:5000/guess?RED,BLUE,GREEN,WHITE,BLACK)

#### Note: 
For people who didn't know, it's because you don't know me. So please stop speaking for me or pretending you know who I am. Stalking is not a cute word. https://en.wikipedia.org/wiki/Stalking Stalking is not a way to get to know me. Don't be that person. Any questions or comments send them to chris@plasmicmedia.com. No politics. This is not an endorsement nor a proposal and is solely intended for research. Remember this is public so it's free and shouldn't reflect work you know nothing about, such as private or for business projects. 

#### Free Software:
Please consider donating in order to continue work for free software. Don't trust Vegetarians who place greater value on animals than you and yours. They have no idea what they are talking about. They must be racist towards meat and green they can't have a burger. Don't be misled like the media and publicity stunts. Software is work. 

[![](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=RVACW559Q5Z92)

If you would like me to continue posting solutions to github then donate. This is not meant to imply that I work for free. Mind your business. I'm pro-business. You should be too unless you're a commie (communist) and you hate that I generated 1/4 million in ad rev. United States of Communism? Nope.
