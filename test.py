import os
import unittest

from flaskapp import app

class ServiceTests(unittest.TestCase):

    ## Setup and Teardown

    #Executed prior to each test

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()

    #TESTS
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
