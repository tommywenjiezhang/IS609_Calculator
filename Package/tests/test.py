import unittest
import Package.tests.test_calculator as calculator_test
from parameterized import parameterized, parameterized_class
import HtmlTestRunner
import os.path

             
def suite():
    test_suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    test_suite.addTests(loader.loadTestsFromModule(calculator_test))
    return test_suite

def text_runner():
    runner = unittest.TextTestRunner()
    runner.run(suite())
    
def build_html_report():
    test_suite = suite()
    html_runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="index" ,report_title="Calculator Test", output=os.getcwd() + "/docs/")
    html_runner.run(test_suite)

if __name__ == '__main__':
    text_runner()
    
   