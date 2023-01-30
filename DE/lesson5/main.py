from flask import Flask
import json

app = Flask(__name__)
db = ['egg', 'wasd', 'bob', 'qwe', 'rty', 'foo', '7', '8', '9', '10', ]


@app.route('/api/last_10_records', methods=['GET'])
def get_records():
    response = 'last 10 added records: ' + str(db[-10:])
    return json.dumps(response)


@app.route('/api/add_record/<record>', methods=['GET', 'POST'])
def add_record(record):
    db.append(record)
    response = "New added record:" + str(record)
    return json.dumps(response)


@app.route('/api/delete_record/<record>', methods=['GET', 'DELETE'])
def delete_record(record):
    try:
        db.remove(record)
        response = "Removed record:" + str(record)
        return json.dumps(response)
    except ValueError:
        return "Value doesn't exist."


if __name__ == '__main__':
    app.run(debug=False)
