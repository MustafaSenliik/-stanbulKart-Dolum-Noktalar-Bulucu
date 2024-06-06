# tests/test_controllers.py

# -*- coding: utf-8 -*-
import unittest
import sys
import os
from unittest.mock import patch

# Proje kök dizinini sys.path'e ekleyin
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controllers import get_directions

class TestControllers(unittest.TestCase):
    @patch('controllers.requests.get')
    def test_get_directions(self, mock_get):
        # Mock response data
        mock_response = {
            'status': 'OK',
            'routes': [{
                'legs': [{
                    'distance': {'text': '10 km'},
                    'duration': {'text': '15 mins'}
                }]
            }]
        }
        mock_get.return_value.json.return_value = mock_response
        
        directions, distance, duration = get_directions('start', 'end')
        
        self.assertEqual(distance, '10 km')
        self.assertEqual(duration, '15 mins')
        self.assertIsNotNone(directions)

if __name__ == '__main__':
    unittest.main()
