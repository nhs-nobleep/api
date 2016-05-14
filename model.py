from app import db
from datetime import datetime

class Team(db.Model):
    team_id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(120))

    def __init__(self, team_name):
        self.team_name = team_name

    def __repr__(self):
        return '<Team %r>' % self.team_id


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.String(120))
    patient_id = db.Column(db.String(120))
    urgency = db.Column(db.Integer)
    comment = db.Column(db.String(120))
    location = db.Column(db.String(120))
    creator_name = db.Column(db.String(120))
    acknowledged = db.Column(db.DateTime)
    done = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime)

    def __init__(self, team_id, patient_id, urgency, comment, location, creator_name):
        self.team_id = team_id
        self.patient_id = patient_id
        self.urgency = urgency
        self.comment = comment
        self.location = location
        self.creator_name = creator_name
        self.acknowledged = datetime.now()
        self.done = datetime.now()
        self.created_at = datetime.now()

    def __repr__(self):
        return '<Job %r>' % self.id


class Audit(db.Model):
    audit_id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer)
    action = db.Column(db.String(120))
    audit_time = db.Column(db.DateTime)
    user_id = db.Column(db.Integer)

    def __init__(self, action, user_id):
        self.action = action
        self.user_id = user_id

    def __repr__(self):
        return '<Audit %r>' % self.job_id

