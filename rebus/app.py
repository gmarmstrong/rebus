from flask import Flask, jsonify, send_from_directory

app = Flask(__name__) # app is our Flask object

@app.route('/')
def index():
    return send_from_directory("../public/", "index.html")

@app.route('/js/<path:filename>')
def js(filename):
    return send_from_directory("../public/js", filename)

@app.route('/css/<path:filename>')
def css(filename):
    return send_from_directory("../public/css", filename)


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
                                    'width': 200,
                                    'height': 199,
                                    'color': '#444444',
                                    'fill': True
                                    }
                                ],
							'circles': []
                            },
						'imageElements':[]
                        }
                    }
                )
            )
