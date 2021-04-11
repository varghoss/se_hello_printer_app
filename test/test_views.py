import json
import unittest
from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        s = str(rv.data)
        ','.join(SUPPORTED) in s

    def test_msg_with_output(self):
        test_data = {"imie": "Karol", "msg": "Hello World!"}
        rv = self.app.get('/?output=json')
        js = json.loads(rv.data)
        self.assertEqual(test_data['msg'], js['msg'])
        self.assertEqual(test_data['imie'], js['imie'])

    def test_msg_with_output2(self):
        rv = self.app.get('/?output=xml')
        self.assertEqual(b'<?xml version="1.0" encoding="UTF-8"?> <root> <imie>\
Karol</imie> <mgs>Hello World!</mgs> </root>', rv.data)
