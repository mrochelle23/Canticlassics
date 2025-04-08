import unittest
from app import app

class CantiClassicsTestCase(unittest.TestCase):
   
    def test_home_page(self):
        """Test home page loads successfully."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Home', response.data)
    
    def test_events_page(self):
        """Test events page loads successfully."""
        response = self.app.get('/events')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Events', response.data)
    
    def test_recordings_page(self):
        """Test recordings page loads successfully."""
        response = self.app.get('/recordings')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Recordings', response.data)
    
    def test_artists_page(self):
        """Test artists page loads successfully."""
        response = self.app.get('/artists')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Artists', response.data)
    
    def test_archives_page(self):
        """Test archives page loads successfully."""
        response = self.app.get('/archives')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Archives', response.data)
    
    def test_about_page(self):
        """Test about page loads successfully."""
        response = self.app.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About', response.data)

if __name__ == '__main__':
    unittest.main()
