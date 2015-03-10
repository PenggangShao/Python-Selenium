"""Combine tests for gnosis.xml.objectify package (req 2.3+)"""
#import sys,re,os,math
#sys.path.append(r"C:\Users\shaopenggang\Desktop\selenium\test_case")
print "------------------> set path"
import unittest,doctest
import HTMLTestRunner
from traceback import print_exc
from allcase_list import *
alltestnames = caselist()
suite = doctest.DocTestSuite()
'''
suite.addTest(unittest.makeSuite(aem_asset.Asset))
suite.addTest(unittest.makeSuite(aem_login.Login))
suite.addTest(unittest.makeSuite(aem_site.Site))
'''
if __name__ == '__main__':
    for test in alltestnames:
        try:
            suite.addTest(unittest.defaultTestLoader.loadTestsFromName(test))
        except Exception:
            print "Error: Skipping test from %s" % (test)
            try:
                __import__(test)
            except ImportError:
                print "Could not import this test"
            else:
                print "Could not load the test suite"
            print_exc()
    print "Running the test..."
    filename = r"C:\Users\shaopenggang\Desktop\selenium\test_result\result.html"
    fp = file(filename,"wb")
    runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title="Report_title",
    description="Report_description")
    runner.run(suite)
