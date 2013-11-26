from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/patients/')
def patients():
    data = {
        "patients": [
            {"name": "Henry Xie"},
            {"name": "Suneel Chakravorty"},
            {"name": "Stacy Kabernow"}
        ]
    }
    return jsonify(**data)


@app.route('/api/patients/<id>')
def patient_detail():
    data = {"name": "Henry Xie"}
    return jsonify(**data)


if __name__ == '__main__':
    app.run()
