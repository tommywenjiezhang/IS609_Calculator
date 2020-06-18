import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from parameterized import parameterized, parameterized_class
import HtmlTestRunner
import os.path
ROOT_DIR = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
print(ROOT_DIR)
@parameterized_class(('a', 'b', 'expected_sum'), CsvReader('Addition.csv').readFile())
class TestAdd(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.calculator = Calculator()
    @classmethod
    def tearDownClass(self):
        if self.calculator is not None:
            self.calculator = None
    def test_add(self):
        result = self.calculator.add(int(self.a),int(self.b))
        self.assertEqual(result,int(self.expected_sum))
        
        
@parameterized_class(('a', 'b', 'expected_result'), CsvReader('Subtraction.csv').readFile())
class TestSubtract(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.calculator = Calculator()
    @classmethod
    def tearDownClass(self):
        if self.calculator is not None:
            self.calculator = None
    def test_subtract(self):
        result = self.calculator.minus(int(self.a),int(self.b))
        self.assertEqual(result,int(self.expected_result))

@parameterized_class(('a', 'b', 'expected_result'), CsvReader('Subtraction.csv').readFile())
class TestSubtract(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.calculator = Calculator()
    @classmethod
    def tearDownClass(self):
        if self.calculator is not None:
            self.calculator = None
    def test_subtract(self):
        result = self.calculator.minus(int(self.a),int(self.b))
        self.assertEqual(result,int(self.expected_result))
        
        
@parameterized_class(('a', 'b', 'expected_result'), CsvReader('Division.csv').readFile())
class TestDivide(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.calculator = Calculator()
    @classmethod
    def tearDownClass(self):
        if self.calculator is not None:
            self.calculator = None
    def test_divide(self):
        result = self.calculator.divide(float(self.b),float(self.a))
        self.assertAlmostEqual(result,float(self.expected_result))
        

@parameterized_class(('a', 'b', 'expected_result'), CsvReader('Multiplication.csv').readFile())
class TestMultiply(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.calculator = Calculator()
    @classmethod
    def tearDownClass(self):
        if self.calculator is not None:
            self.calculator = None
    def test_divide(self):
        result = self.calculator.multiply(int(self.b),int(self.a))
        self.assertEqual(result,int(self.expected_result))
        
@parameterized_class(('a', 'expected_result'), CsvReader('Square.csv').readFile())
class TestSquare(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.calculator = Calculator()
    @classmethod
    def tearDownClass(self):
        if self.calculator is not None:
            self.calculator = None
    def test_square(self):
        result = self.calculator.square(int(self.a))
        self.assertEqual(result,int(self.expected_result))
        print(f"Sqare test: {self.a}^2 ={self.expected_result}" )
        

@parameterized_class(('a', 'expected_result'), CsvReader('Square Root.csv').readFile())
class TestSqrt(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.calculator = Calculator()
    @classmethod
    def tearDownClass(self):
        if self.calculator is not None:
            self.calculator = None
    def test_sqrt(self):
        result = self.calculator.sqrt(int(self.a))
        print(f"Sqare root test: {self.a} sqrt2 ={self.expected_result}" )
        self.assertAlmostEqual(result,float(self.expected_result))
             
def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(TestAdd('test_add'))
    test_suite.addTest(TestSubtract('test_subtract'))
    test_suite.addTest(TestDivide('test_divide'))
    test_suite.addTest(TestSquare('test_square'))
    test_suite.addTest(TestSqrt('test_sqrt'))
    return test_suite

def text_runner():
    runner = unittest.TextTestRunner()
    runner.run(suite())
    
def build_html_report():
    test_suite = suite()
    html_runner = HtmlTestRunner.HTMLTestRunner()
    html_runner.run(test_suite)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="index" ,output=ROOT_DIR + "/docs/"))
    
   