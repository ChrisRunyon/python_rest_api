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
