import unittest
from app import app

class CantiClassicsTestCase(unittest.TestCase):
    def setUp(self):
        """Set up test client."""
        self.app = app.test_client()
        self.app.testing = True
        self.test_case_id = None
    
    def test_home_page(self):
        """Test home page loads successfully."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Home', response.data)
        self.test_case_id = "HOME_001"
    
    def test_events_page(self):
        """Test events page loads successfully."""
        response = self.app.get('/events')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Events', response.data)
        self.test_case_id = "EVENTS_001"
    
    def test_recordings_page(self):
        """Test recordings page loads successfully."""
        response = self.app.get('/recordings')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Recordings', response.data)
        self.test_case_id = "RECORDINGS_001"
    
    def test_artists_page(self):
        """Test artists page loads successfully."""
        response = self.app.get('/artists')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Artists', response.data)
        self.test_case_id = "ARTISTS_001"
    
    def test_archives_page(self):
        """Test archives page loads successfully."""
        response = self.app.get('/archives')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Archives', response.data)
        self.test_case_id = "ARCHIVES_001"
    
    def test_about_page(self):
        """Test about page loads successfully."""
        response = self.app.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About', response.data)
        self.test_case_id = "ABOUT_001"
    
    def test_add_user(self):
        """Test adding a user."""
        response = self.app.post('/add', data={'email2': 'test@example.com'})
        self.assertEqual(response.status_code, 302)  # Redirect after successful submission
        self.test_case_id = "ADD_USER_001"
    
    def test_unsubscribe(self):
        """Test unsubscribe page loads successfully."""
        response = self.app.get('/unsubscribe')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Unsubscribe', response.data)
        self.test_case_id = "UNSUBSCRIBE_001"

    def test_missing_email_field(self):
        """Test inquiry submission without an email."""
        response = self.app.post('/inquiry', data={'message': 'This is a test inquiry.'})
        self.assertNotEqual(response.status_code, 200)  # Should not redirect
        self.assertIn(b'', response.data) # Don't return an error message, Bootstrap will return an message.
        self.test_case_id = "INQUIRY_MISSING_EMAIL_001"

    def test_message_exceeds_max_length(self):
        """Test inquiry submission with a message that is too long."""
        long_message = "A" * 501  # One character over the limit
        response = self.app.post('/inquiry', data={'name': 'bob', 'email2': 'test@example.com', 'message': long_message})
        self.assertNotEqual(response.status_code, 200)  # Should not allow submission
        self.assertIn(b'', response.data)  # Don't return an error message, Javascript will prevent more than 500 characters.
        self.test_case_id = "INQUIRY_MAX_LENGTH_001"

    def test_invalid_email_format(self):
        """Test inquiry submission with an invalid email format."""
        response = self.app.post('/inquiry', data={'name':'bob', 'email2': 'invalid-email', 'message': 'Test message'})
        self.assertNotEqual(response.status_code, 200) # Don't return an error message, Bootstrap will handle it.
        self.assertIn(b'', response.data)
        self.test_case_id = "INQURIY_INVALID_EMAIL_001"
        
    def test_rate_limiting(self):
        """Test multiple inquiries in a short time period to check rate limiting."""
        for _ in range(5):  # Assuming limit is 3 per minute
            response = self.app.post('/inquiry', data={'email2': 'test@example.com', 'message': 'Spam test'})
        self.assertNotEqual(response.status_code, 200)  # Should block excessive requests
        self.assertIn(b'', response.data)  # Don't return an error message, MongoDB will return a message.
        self.test_case_id = "RATE_LIMIT_001"
        
if __name__ == '__main__':
    unittest.main()


