import os
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
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
    doctor_comment = request.form['doctor_comment']
    bed = request.form['bed']
    ward = request.form['ward']
    location = request.form['location']
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


@app.route('/job/update/<id>')
def update(id):
    team_id = request.form['team_id']
    patient_id = request.form['patient_id']
    urgency = request.form['urgency']
    creator_comment = request.form['creator_comment']
    doctor_comment = request.form['doctor_comment']
    bed = request.form['bed']
    ward = request.form['ward']
    location = request.form['location']
    creator_name = request.form['creator_name']

    job = Job.query.get(id)

    if team_id is not None:
        job.team_id = team_id
    if patient_id is not None:
        job.patient_id = patient_id
    if urgency is not None:
        job.urgency = urgency
    if creator_comment is not None:
        job.creator_comment = creator_comment
    if doctor_comment is not None:
        job.doctor_comment = doctor_comment
    if bed is not None:
        job.bed = bed
    if ward is not None:
        job.ward = ward
    if location is not None:
        job.location = location
    if creator_name is not None:
        job.creator_name = creator_name

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
