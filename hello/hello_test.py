import unittest

from .hello_app import app


class MyTestCase(unittest.TestCase):

    def assert_contains(self, substring, string):
        assert substring in string


class HelloTest(MyTestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_root(self):
        self.assert_contains('Hello', self.app.get('/').data)
