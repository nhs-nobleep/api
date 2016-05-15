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

        result = self.app.get('/job/read')
        data = json.loads(result.data.decode('utf-8'))
        assert(data['jobs'][0]['id'] is 1)
        assert(data['jobs'][0]['patient_id'] == 'patient_id')

    def test_read_team_id_response(self):
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

        result = self.app.get('/job/read/1')

        self.assertEqual(rv.mimetype, 'application/json')

    def test_read_team_id(self):
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

        result = self.app.get('/job/read/10')
        data = json.loads(result.data.decode('utf-8'))
        assert(data['jobs'][0]['team_id'] is 10)

    def test_update_response(self):
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

        up = self.app.post('/job/update/1', data={
            'team_id': 20
        }, follow_redirects=True)

        self.assertEqual(up.mimetype, 'application/json')

    def test_update(self):
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

        up = self.app.post('/job/update/1', data={
            'team_id': 20
        }, follow_redirects=True)

        result = self.app.get('/job/read')

        data = json.loads(result.data.decode('utf-8'))
        assert(data['jobs'][0]['id'] is 1)
        assert(data['jobs'][0]['team_id'] is 20)


    def tearDown(self):
        db.drop_all()


if __name__ == '__main__':
    unittest.main()
