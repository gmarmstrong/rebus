from flask import Flask, jsonify

app = Flask(__name__) # app is our Flask object

@app.route('/')
def index():
    return('Hello, world!')

@app.route('/puzzle')
def puzzle():
    return(
            jsonify(
                {
                    'answer': 'Read between the lines',
                    'elements': {
                        'textElements': {
                            'text': '|R|E|A|D|',
                            'x': 77,
                            'y': 88,
                            'font': '99px Comic Sans MS',
                            'color': 'red'
                            },
                        'shapeElements': {
                            'lines': [
                                {
                                    'x1': 0,
                                    'y1': 0,
                                    'x2': 100,
                                    'y2': 200,
                                    'color': 'red'
                                    }
                                ],
                            'rects': [
                                {
                                    'x': 8,
                                    'y': 9,
                                    'width': 20,
                                    'height': 30,
                                    'color': '#444444',
                                    'fill': True
                                    }
                                ]
                            }
                        }
                    }
                )
            )
