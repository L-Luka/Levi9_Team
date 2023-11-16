import unittest
from basketball_app import app

class TestPlayerStatsAPI(unittest.TestCase):
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_get_player_stats(self):
        # Testiranje da li dobijamo odgovor u formatu JSON
        response = self.app.get('/player_stats/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')

        # Testiranje da li su povratne vrednosti tačne
        data = response.get_json()
        self.assertIn('avg_ftm', data)
        self.assertIn('avg_fta', data)

if __name__ == '__main__':
    unittest.main()
