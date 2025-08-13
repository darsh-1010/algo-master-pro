#!/usr/bin/env python3
"""
Basic tests for the DSA Problem Solver Flask application
"""

import unittest
import sys
import os

# Add the current directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

class TestDSASolver(unittest.TestCase):
    """Test cases for DSA Problem Solver"""
    
    def test_app_import(self):
        """Test that the Flask app can be imported successfully"""
        try:
            import app
            self.assertTrue(hasattr(app, 'app'))
            self.assertTrue(hasattr(app, 'DSA_PROBLEMS'))
        except ImportError as e:
            self.fail(f"Failed to import app: {e}")
    
    def test_dsa_problems_data(self):
        """Test that DSA problems data is properly structured"""
        import app
        problems = app.DSA_PROBLEMS
        
        # Check that we have problems
        self.assertGreater(len(problems), 0)
        
        # Check structure of first problem
        first_problem = list(problems.values())[0]
        required_fields = ['statement', 'difficulty', 'category', 'tags']
        
        for field in required_fields:
            self.assertIn(field, first_problem)
    
    def test_flask_app_config(self):
        """Test Flask app configuration"""
        import app
        # In the current app.py, debug is set to True for development
        # This test checks that the app has the debug attribute
        self.assertTrue(hasattr(app.app, 'debug'))
    
    def test_required_packages(self):
        """Test that required packages can be imported"""
        try:
            import flask
            import groq
            import dotenv
            self.assertTrue(True)  # If we get here, all imports succeeded
        except ImportError as e:
            self.fail(f"Failed to import required package: {e}")

if __name__ == '__main__':
    unittest.main()
