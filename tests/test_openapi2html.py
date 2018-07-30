#!/usr/bin/env python3

'''
test_raml2html
----------------------------------
Tests for `openapi2html` module.
'''

import unittest
import subprocess
import sys
import os
from os import path

sys.path.append(path.join(path.dirname(__file__), '..'))

from openapipreparer.builders.openapi2html import openapi2html

class OPENAPI2HTMLTestCase(unittest.TestCase):
    '''
    Tests for the OPENAPI2HTML method
    '''

    def test_openapi2html_is_html(self):
        '''
        Is the output of openapi2html actually HTML?
        '''
        test_openapi = path.join(os.getcwd(), 'tests', 'src', 'openapi.json')
        output_file = path.join(os.getcwd(), 'tests',
                                'dest', 'test_is_html')
        self.assertIn('<html>', openapi2html(test_openapi, output_file))

    def test_openapi2html_without_json(self):
        '''
        Does non-JSON input fail?
        '''
        test_not_openapi = path.join(os.getcwd(), 'tests', 'src', 'tester.txt')
        output_file = path.join(os.getcwd(), 'tests',
                                'dest', 'test_isnt_html')
        self.assertRaises(TypeError, openapi2html, [test_not_openapi, output_file])


if __name__ == '__main__':
    unittest.main()
