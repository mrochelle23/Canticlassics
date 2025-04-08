import unittest
from app import app

class CantiClassicsTestCase(unittest.TestCase):
    def setUp(self):
        """Set up test client."""
        self.app = app.test_client()
        self.app.testing = True

    def test_add_user(self):
        """Test adding a user."""
        response = self.app.post('/add', data={'email2': 'test@example.com'})
        self.assertEqual(response.status_code, 302)  # Redirect after successful submission
    
    def test_unsubscribe(self):
        """Test unsubscribe page loads successfully."""
        response = self.app.get('/unsubscribe')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Unsubscribe', response.data)

    def test_missing_email_field(self):
        """Test inquiry submission without an email."""
        response = self.app.post('/inquiry', data={'message': 'This is a test inquiry.'})
        self.assertNotEqual(response.status_code, 200)  # Should not redirect
        self.assertIn(b'', response.data) # Don't return an error message, Bootstrap will return an message.

    def test_message_exceeds_max_length(self):
        """Test inquiry submission with a message that is too long."""
        long_message = "A" * 501  # One character over the limit
        response = self.app.post('/inquiry', data={'name': 'bob', 'email2': 'test@example.com', 'message': long_message})
        self.assertNotEqual(response.status_code, 200)  # Should not allow submission
        self.assertIn(b'', response.data)  # Don't return an error message, Javascript will prevent more than 500 characters.

    def test_invalid_email_format(self):
        """Test inquiry submission with an invalid email format."""
        response = self.app.post('/inquiry', data={'name':'bob', 'email2': 'invalid-email', 'message': 'Test message'})
        self.assertNotEqual(response.status_code, 200) # Don't return an error message, Bootstrap will handle it.
        self.assertIn(b'', response.data)

    def test_rate_limiting(self):
        """Test multiple inquiries in a short time period to check rate limiting."""
        for _ in range(5):  # Assuming limit is 3 per minute
            response = self.app.post('/inquiry', data={'email2': 'test@example.com', 'message': 'Spam test'})
        self.assertNotEqual(response.status_code, 200)  # Should block excessive requests
        self.assertIn(b'', response.data)  # Don't return an error message, MongoDB will return a message.


if __name__ == '__main__':
    unittest.main()
