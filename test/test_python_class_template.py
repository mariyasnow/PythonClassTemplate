#!/usr/bin/python
################################################################
# export sensitive args to your env
# Usage: docker run -it -v `pwd`:/home python:3 bash
#        cd /home && pip install -r requirements.txt
#        python -m unittest -v test.test_python_class_template
'''
python -m unittest -v test.test_python_class_template 
test_function (test.test_python_class_template.TestPythonClassTemplate)
should do things ... ok

----------------------------------------------------------------------
Ran 1 test in 0.001s

OK

'''
################################################################

from python_class_template import PythonClassTemplate
import HtmlTestRunner
import unittest
import os

class MockArgs:
    def __init__(self, *args):
        self.name = os.environ.get('name', 'test_class_name')
        
class TestPythonClassTemplate(unittest.TestCase):
    ''' Tests for PythonClassTemplate '''

    @classmethod
    def setUpClass(self):
        ''' set up once '''
        args = MockArgs()
        self.pct = PythonClassTemplate(args.name)
        
    def test_function(self):
        ''' should do things '''

        actual = self.pct.function()
        expected = ''
        self.assertEqual(actual, expected)

    @classmethod
    def tearDownClas(self):
        pass
    
def main():
    pass

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='PythonClassTemplate'))
