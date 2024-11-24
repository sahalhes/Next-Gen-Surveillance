import unittest
from gps_tracker.tracker import track

class TestTracker(unittest.TestCase):
    def test_track_success(self):
        result = track({'culprit_id': 123})
        self.assertEqual(result['status'], 'Tracking started')
        self.assertEqual(result['culprit_id'], 123)

    def test_track_fail(self):
        result = track({'culprit_id': None})
        self.assertEqual(result['status'], 'Failed')
        self.assertEqual(result['message'], 'Culprit ID not provided')

if __name__ == '__main__':
    unittest.main()
