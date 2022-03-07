


from flask import Flask
from flask import jsonify
from flask import request
from flask.typing import StatusCode

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET', 'POST'])
def home():
    result = {
        'message': 'Hello World Tuần đây',
        'status': 'Success'
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(port=5000,host="0.0.0.0",debug=True)