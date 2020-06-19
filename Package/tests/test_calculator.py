from Package.project.Calculator import Calculator
from parameterized import parameterized, parameterized_class
import unittest
from Package.project.CsvReader import CsvReader

class TestCalculator(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.calculator = Calculator()
    @classmethod
    def tearDownClass(self):
        if self.calculator is not None:
            self.calculator = None
        
    @parameterized.expand(CsvReader('Addition.csv').readFile())
    def test_add(self,a,b, expected_sum):
        result = self.calculator.add(int(a),int(b))
        self.assertEqual(result,int(expected_sum))
           
    def test_add_error(self):
        with self.assertRaises(ValueError):
            result = self.calculator.add('hello','world')
    
    @parameterized.expand(CsvReader('Subtraction.csv').readFile())      
    def test_subtract(self,a,b,expected_result):
        result = self.calculator.minus(int(a),int(b))
        self.assertEqual(result,int(expected_result))
    
    @parameterized.expand(CsvReader('Division.csv').readFile())
    def test_divide(self,a,b,expected_result):
        print(f'a:{a} b:{b} expected:{expected_result}')
        result = self.calculator.divide(float(b),float(a))
        self.assertAlmostEqual(result,float(expected_result))
        
    def test_divide_error(self):
        with self.assertRaises(ValueError):
            result = self.calculator.divide(9,0)
        
    @parameterized.expand(CsvReader('Multiplication.csv').readFile())
    def test_multiply(self,a,b,expected_result):
        result = self.calculator.multiply(int(b),int(a))
        self.assertEqual(result,int(expected_result))
        
    @parameterized.expand(CsvReader('Square.csv').readFile())
    def test_square(self,a,expected_result):
        result = self.calculator.square(int(a))
        self.assertEqual(result,int(expected_result))
        print(f"Sqare test: {a}^2 ={expected_result}" )
    
    @parameterized.expand(CsvReader('Square Root.csv').readFile())
    def test_sqrt(self,a,expected_result):
        result = self.calculator.sqrt(int(a))
        self.assertAlmostEqual(result,float(expected_result))