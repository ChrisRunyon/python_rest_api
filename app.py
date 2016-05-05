from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import random

app = Flask(__name__)
api = Api(app)
pegs = [] 
match = []
counter = 0
tries = 0
error = 0

class Test(Resource):
    def get(self):
        result = jsonify({'Result':'Success!'})
        return result

class Start(Resource):
    def get(self):
        global pegs
        colors = ['RED', 'ORANGE', 'YELLOW', 'GREEN', 'BLUE', 'PURPLE', 'WHITE', 'BLACK']
        
        for i in range(5):
            pegs.insert(i, random.choice(colors));

        with open('secretcode','w') as secret_code:
            secret_code.write(','.join(pegs))

        return jsonify({'Result':'Start!'})

class Guess(Resource):
    def get(self, answer):
        global tries, error, counter, pegs, match
        match = []
        counter = 0
        if tries != 7:
            guess = answer.split(',')
            #return len(pegs)
            if error != 12:
                if len(guess) == 5:
                    for i in range(5):
                        if guess[i] in pegs[i]:
                            match.insert(i, 'RED')
                            counter += 1
                        else: 
                            match.insert(i, 'WHITE')

                    if counter == 5:
                        result = jsonify({'WINNER!': [', '.join(match)]})      
                        tries = 7
                    else:
                        result = jsonify({'Try Again.': [', '.join(match)]})
                        tries += 1

                    return result
                else:
                    result = jsonify({'Error': 'Please enter 5 colors'})
                    error += 1
                    return result
            else:
                result = jsonify({'Result':'You LOST!'})
                return result;
        else: 
            result = jsonify({'Result':'Game Over.'})
            return result
 
api.add_resource(Guess, '/guess/<string:answer>') #comma delimited string of colors
api.add_resource(Start, '/start')
api.add_resource(Test, '/test')

if __name__ == '__main__':
    app.run(debug=True)