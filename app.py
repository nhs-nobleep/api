import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask.ext.cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:////tmp/test.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

from model import *


@app.route('/')
def index():
    return 'Banish The Beep API'


@app.route('/create_all')
def create_tables():
    db.create_all()
    return jsonify({ 'success' : True })


@app.route('/drop_all')
def drop_tables():
    db.drop_all()
    return jsonify({ 'success' : True })


@app.route('/job/create', methods=['POST'])
def create():
    # TODO VALIDATION
    team_id = request.form['team_id']
    patient_id = request.form['patient_id']
    urgency = request.form['urgency']
    creator_comment = request.form['creator_comment']
    doctor_comment = request.form['doctor_comment'] if 'doctor_comment' in request.form else ''
    bed = request.form['bed']
    ward = request.form['ward']
    location = request.form['location'] if 'location' in request.form else ''
    creator_name = request.form['creator_name']

    job = Job(team_id, patient_id, urgency, creator_comment, doctor_comment, bed, ward, location, creator_name)

    db.session.add(job)
    db.session.commit()

    return jsonify({ 'success' : True })


@app.route('/job/read')
def read_all():
    #rows = db.session.query(Team, Job, Doctor).filter(Job.done is None).all()
    rows = Job.query.filter_by(done=None)

    json_jobs = []
    for job in rows:
        json_jobs.append({
            'id': job.id,
            'team_id': job.team_id,
            'patient_id': job.patient_id,
            'urgency': job.urgency,
            'creator_comment': job.creator_comment,
            'doctor_comment': job.doctor_comment,
            'bed': job.bed,
            'ward': job.ward,
            'location': job.location,
            'creator_id': job.creator_id,
            'creator_name': job.creator_name,
            'acknowledged': job.acknowledged,
            'done': job.done,
            'created_at': job.created_at
            })

    return jsonify({ 'jobs' : json_jobs })


@app.route('/job/read/<team_id>')
def read(team_id):
    rows = Job.query.filter_by(team_id=team_id, done=None)

    json_jobs = []
    for job in rows:
        json_jobs.append({
            'id': job.id,
            'team_id': job.team_id,
            'patient_id': job.patient_id,
            'urgency': job.urgency,
            'creator_comment': job.creator_comment,
            'doctor_comment': job.doctor_comment,
            'bed': job.bed,
            'ward': job.ward,
            'location': job.location,
            'creator_id': job.creator_id,
            'creator_name': job.creator_name,
            'acknowledged': job.acknowledged,
            'done': job.done,
            'created_at': job.created_at
            })

    return jsonify({ 'jobs' : json_jobs })


@app.route('/job/update/<id>', methods=['POST'])
def update(id):
    job = Job.query.get(id)

    if 'team_id' in request.form:
        job.team_id = request.form['team_id']
    if 'patient_id' in request.form:
        job.patient_id = request.form['patient_id']
    if 'urgency' in request.form:
        job.urgency = request.form['urgency']
    if 'creator_comment' in request.form:
        job.creator_comment = request.form['creator_comment']
    if 'doctor_comment' in request.form:
        job.doctor_comment = request.form['doctor_comment']
    if 'bed' in request.form:
        job.bed = request.form['bed']
    if 'ward' in request.form:
        job.ward = request.form['ward']
    if 'location' in request.form:
        job.location = request.form['location']
    if 'creator_name' in request.form:
        job.creator_name = request.form['creator_name']
    if 'acknowledged' in request.form:
        job.acknowledged = datetime.now() 
    if 'done' in request.form:
        job.done = datetime.now() 

    db.session.add(job)
    db.session.commit()

    return jsonify({ 'success' : True })

if not app.debug:
    import logging
    from logging import FileHandler
    file_handler = FileHandler('app_debug.log')
    file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)

if __name__ == "__main__":
    app.run()
