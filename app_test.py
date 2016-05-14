import unittest
from app import *

class JobTestCase(unittest.TestCase):
    
    def setUp(self):
        db.create_all()
        self.app = app.test_client()

    def test_insert(self):
        rv = self.app.post('/job/create', data={
            'team_id': 'team_id',
            'patient_id' : 'patient_id',
            'urgency' : 1,
            'comment' : 'comment',
            'location' : 'location',
            'creator_name' : 'creator_name'
        }, follow_redirects=True)

        self.assertEqual(rv.mimetype, 'application/json')

    def test_read(self):
        rv = self.app.get('/job/read/team_id')

        self.assertEqual(rv.mimetype, 'application/json')


if __name__ == '__main__':
    unittest.main()
