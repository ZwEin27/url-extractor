# -*- coding: utf-8 -*-
# @Author: ZwEin
# @Date:   2016-06-30 15:05:04
# @Last Modified by:   ZwEin
# @Last Modified time: 2016-07-26 13:51:52

import os
import sys
import time
import json
import unittest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from url_extractor import URLExtractor

def load_groundtruth(path=os.path.join(os.path.dirname(__file__), "groundtruth.json")):
    input_fh = open(path, 'rb')
    lines = input_fh.readlines()
    json_obj = json.loads(''.join(lines))
    jsonlines = json_obj['jsonlines']
    return jsonlines



def cmp_extraction(ext1, ext2):
    return set(ext1) == set(ext2)

class TestMethods(unittest.TestCase):
    def setUp(self):
        self.groundtruth_data = load_groundtruth()
        
    def tearDown(self):
        pass

    def test_groundtruth(self):
        total = 0
        correct = 0
        for data in self.groundtruth_data:
            text = data['text']
            ext_gt = data['extraction']
            ext_pd = URLExtractor.extract(text)
            
            if cmp_extraction(ext_gt, ext_pd):
                correct += 1
            else:
                print '#'*50
                print '### original ###'
                print text.encode('ascii','ignore')
                print '### groundtruth data ###'
                print ext_gt
                print '### extracted data ###'
                print ext_pd

            total += 1
        print 60*'-'
        print 'pass', correct, 'out of', total

    def test_extract(self):
        text = ''
        print URLExtractor.extract(text)
            

if __name__ == '__main__':
    def run_main_test():
        suite = unittest.TestSuite()

        suite.addTest(TestMethods('test_groundtruth'))
        suite.addTest(TestMethods('test_extract'))

        runner = unittest.TextTestRunner()
        runner.run(suite)

    run_main_test()

