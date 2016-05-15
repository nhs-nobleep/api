import unittest
from flask import json
from app import *


class JobTestCase(unittest.TestCase):

    def setUp(self):
        db.create_all()
        self.app = app.test_client()

    def test_insert_response(self):
        rv = self.app.post('/job/create', data={
            'team_id': 10,
            'patient_id': 'patient_id',
            'urgency': 3,
            'creator_comment': 'creator_comment',
            'doctor_comment': 'doctor_comment',
            'bed': 'bed',
            'ward': 'ward',
            'location': 'location',
            'creator_name': 'creator_name'
        }, follow_redirects=True)

        self.assertEqual(rv.mimetype, 'application/json')

    def test_read_all_response(self):
        rv = self.app.get('/job/read')
        self.assertEqual(rv.mimetype, 'application/json')

    def test_insert_and_read_all(self):
        self.app.post('/job/create', data={
            'team_id': 10,
            'patient_id': 'patient_id',
            'urgency': 3,
            'creator_comment': 'creator_comment',
            'doctor_comment': 'doctor_comment',
            'bed': 'bed',
            'ward': 'ward',
            'location': 'location',
            'creator_name': 'creator_name'
        }, follow_redirects=True)

        result = self.app.get('/job/read')
        data = json.loads(result.data.decode('utf-8'))
        self.assertEqual(data['jobs'][0]['id'], 1)
        self.assertEqual(data['jobs'][0]['patient_id'], 'patient_id')

    def test_read_team_id_response(self):
        self.app.post('/job/create', data={
            'team_id': 10,
            'patient_id': 'patient_id',
            'urgency': 3,
            'creator_comment': 'creator_comment',
            'doctor_comment': 'doctor_comment',
            'bed': 'bed',
            'ward': 'ward',
            'location': 'location',
            'creator_name': 'creator_name'
        }, follow_redirects=True)

        result = self.app.get('/job/read/1')
        self.assertEqual(result.mimetype, 'application/json')

    def test_read_team_id(self):
        self.app.post('/job/create', data={
            'team_id': 10,
            'patient_id': 'patient_id',
            'urgency': 3,
            'creator_comment': 'creator_comment',
            'doctor_comment': 'doctor_comment',
            'bed': 'bed',
            'ward': 'ward',
            'location': 'location',
            'creator_name': 'creator_name'
        }, follow_redirects=True)

        result = self.app.get('/job/read/10')
        data = json.loads(result.data.decode('utf-8'))
        self.assertEqual(data['jobs'][0]['team_id'], 10)

    def test_update_response(self):
        self.app.post('/job/create', data={
            'team_id': 10,
            'patient_id': 'patient_id',
            'urgency': 3,
            'creator_comment': 'creator_comment',
            'doctor_comment': 'doctor_comment',
            'bed': 'bed',
            'ward': 'ward',
            'location': 'location',
            'creator_name': 'creator_name'
        }, follow_redirects=True)

        up = self.app.post('/job/update/1', data={
            'team_id': 20
        }, follow_redirects=True)

        self.assertEqual(up.mimetype, 'application/json')
        self.assertEqual(json.loads(up.data.decode('utf-8'))['success'], True)

    def test_update_team_id(self):
        self.app.post('/job/create', data={
            'team_id': 10,
            'patient_id': 'patient_id',
            'urgency': 3,
            'creator_comment': 'creator_comment',
            'doctor_comment': 'doctor_comment',
            'bed': 'bed',
            'ward': 'ward',
            'location': 'location',
            'creator_name': 'creator_name'
        }, follow_redirects=True)

        up = self.app.post('/job/update/1', data={
            'team_id': 20
        }, follow_redirects=True)

        self.assertEqual(json.loads(up.data.decode('utf-8'))['success'], True)

        result = self.app.get('/job/read')
        data = json.loads(result.data.decode('utf-8'))
        self.assertEqual(data['jobs'][0]['id'], 1)
        self.assertEqual(data['jobs'][0]['team_id'], 20)

    def test_update_done(self):
        self.app.post('/job/create', data={
            'team_id': 10,
            'patient_id': 'patient_id',
            'urgency': 3,
            'creator_comment': 'creator_comment',
            'doctor_comment': 'doctor_comment',
            'bed': 'bed',
            'ward': 'ward',
            'location': 'location',
            'creator_name': 'creator_name'
        }, follow_redirects=True)

        up = self.app.post('/job/update/1', data={
            'done': 'Sun May 15 2016 12:17:36 GMT+0100 (BST)'
        }, follow_redirects=True)

        self.assertEqual(json.loads(up.data.decode('utf-8'))['success'], True)

        result = self.app.get('/job/read')
        data = json.loads(result.data.decode('utf-8'))
        self.assertEqual(data, {'jobs': []})

    def test_update_acknowledged(self):
        self.app.post('/job/create', data={
            'team_id': 10,
            'patient_id': 'patient_id',
            'urgency': 3,
            'creator_comment': 'creator_comment',
            'doctor_comment': 'doctor_comment',
            'bed': 'bed',
            'ward': 'ward',
            'location': 'location',
            'creator_name': 'creator_name'
        }, follow_redirects=True)

        up = self.app.post('/job/update/1', data={
            'acknowledged': 'Sun May 15 2016 12:17:36 GMT+0100 (BST)'
        }, follow_redirects=True)

        self.assertEqual(json.loads(up.data.decode('utf-8'))['success'], True)

        result = self.app.get('/job/read')
        data = json.loads(result.data.decode('utf-8'))
        self.assertEqual(data['jobs'][0]['id'], 1)
        self.assertEqual(type(data['jobs'][0]['acknowledged']), str)

    def test_insert_urgency_4(self):
        rv = self.app.post('/job/create', data={
            'team_id': 10,
            'patient_id': 'patient_id',
            'urgency': 4,
            'creator_comment': 'creator_comment',
            'doctor_comment': 'doctor_comment',
            'bed': 'bed',
            'ward': 'ward',
            'location': 'location',
            'creator_name': 'creator_name'
        }, follow_redirects=True)

        self.assertEqual(rv.mimetype, 'application/json')

        result = self.app.get('/job/read')
        data = json.loads(result.data.decode('utf-8'))
        self.assertEqual(data, None)

    def test_insert_team_id_missing(self):
        rv = self.app.post('/job/create', data={
            'patient_id': 'patient_id',
            'urgency': 3,
            'creator_comment': 'creator_comment',
            'doctor_comment': 'doctor_comment',
            'bed': 'bed',
            'ward': 'ward',
            'location': 'location',
            'creator_name': 'creator_name'
        }, follow_redirects=True)

        self.assertEqual(rv.mimetype, 'application/json')

        result = self.app.get('/job/read')
        data = json.loads(result.data.decode('utf-8'))
        self.assertEqual(data, None)

    def test_insert_team_id_empty(self):
        rv = self.app.post('/job/create', data={
            'team_id': '',
            'patient_id': 'patient_id',
            'urgency': 3,
            'creator_comment': 'creator_comment',
            'doctor_comment': 'doctor_comment',
            'bed': 'bed',
            'ward': 'ward',
            'location': 'location',
            'creator_name': 'creator_name'
        }, follow_redirects=True)

        self.assertEqual(rv.mimetype, 'application/json')

        result = self.app.get('/job/read')
        data = json.loads(result.data.decode('utf-8'))
        self.assertEqual(data, None)

    def test_insert_team_id_none(self):
        rv = self.app.post('/job/create', data={
            'team_id': None,
            'patient_id': 'patient_id',
            'urgency': 3,
            'creator_comment': 'creator_comment',
            'doctor_comment': 'doctor_comment',
            'bed': 'bed',
            'ward': 'ward',
            'location': 'location',
            'creator_name': 'creator_name'
        }, follow_redirects=True)

        self.assertEqual(rv.mimetype, 'application/json')

        result = self.app.get('/job/read')
        data = json.loads(result.data.decode('utf-8'))
        self.assertEqual(data, None)

    def tearDown(self):
        db.drop_all()


if __name__ == '__main__':
    unittest.main()
