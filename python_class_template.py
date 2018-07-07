#!/usr/bin/python
##################################################################################
# ClassName: Description
# Author: 
# Usage:
''' 
'''
#################################################################################
import requests
# for poorly configured ssl
#from requests.packages.urllib3.exceptions import InsecureRequestWarning
#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import argparse

class PythonClassTemplate:
    ''' Template Python Class '''
    def __init__(self, name):
        ''' Min info required to intract the class '''
        self.name = name
        
    def function(self):
        ''' '''
        return ''
    
def parse_args():
    ''' Command line options '''
    parser = argparse.ArgumentParser(description='Python Class Template')
    parser.add_argument('--name', default='', help='')
    args = parser.parse_args()
    return args

def main():
    args = parse_args()

    pct = PythonClassTemplate(args.name)
    return pct.function()
    
if __name__ == '__main__':
    main()
