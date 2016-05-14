from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

from model import *

@app.route('/job/create', methods=['POST'])
def create():
    # TODO VALIDATION
    team_id = request.form('team_id')
    patient_id = request.form('patient_id')
    urgency = request.form('urgency')
    comment = int(request.form('comment'))
    location = request.form('location')
    creator_name = request.form('creator_name')

    job = Job(team_id, patient_id, urgency, comment, location, creator_name)
    db.session.add(job)
    db.session.commit()

    return jsonify({ 'success' : True })


@app.route('/job/read')
def read_all():
    jobs = Job.query.all()
    return jsonify(jobs)


@app.route('/job/read/<team_id>')
def read(team_id):
    jobs = Job.query.filter_by(team_id=team_id)
    return jsonify(jobs)


@app.route('/job/update/<id>')
def update(id):
    job = Job.query.get(id)
    return jsonify({ 'success' : True })


if __name__ == "__main__":
    app.run(debug=True)
