"""Tests for the engine_upgrades function in engine_upgrades.py
"""

import unittest
from engine_upgrades import engine_upgrades

class TestEngineUpgrades(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_low_budget_performance_criteria(self):
        bmw_specs = {
            "model": "BMW 330i X-Drive",
            "year": 2022,
            "engine": "2.0L Turbocharged 4-Cylinder",
            "drive_train": "All-Wheel Drive",
            "horsepower": 255,
            "torque": 295
        }
        budget = 'low'
        criteria = 'performance'
        expected_output = ['A', 'B', 'C']
        self.assertEqual(engine_upgrades(bmw_specs, budget, criteria), expected_output)
    
    # Repeat for other budget and criteria combinations
    
if __name__ == '__main__':
    unittest.main()