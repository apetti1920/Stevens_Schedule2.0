import os.path
from flask import Flask, request, Response
import server.functions as server
import json


app = Flask(__name__)


def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))


def get_file(filename):  # pragma: no cover
    try:
        print(root_dir())
        src = os.path.join(root_dir(), filename)
        return open(src).read()
    except IOError as exc:
        return str(exc)

@app.route('/', methods=['GET'])
def index():
    content = get_file('../views/main.html')
    return Response(content, mimetype="text/html")

@app.route('/classnames', methods=['GET'])
def classnmes():
    names = server.getAllClassNames(server.getAllClasses('2018', 'F'))
    print(names)
    return json.dumps(names)


@app.route('/schedules', methods=['POST'])
def scedules():
    req_data = request.get_json(force=True)
    classes = req_data['classes']
    print('here')
    print(classes)

    return json.dumps(classes)

if __name__ == '__main__':
    app.run(debug=True)