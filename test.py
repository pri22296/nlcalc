import unittest
from nlcalc import NLCalculator
from nlcalc.utils import is_numeric, convert_to_numeric, text2int


class NaturalLanguageQueryTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = NLCalculator()

    def check(self, query, result):
        self.assertEqual(self.calculator.calculate(query), result)

    # ************ Addition *********************************

    def test_keyword_add(self):
        self.check('add 4 and 2', 6)

    def test_keyword_sum(self):
        self.check('sum of 4 and 2', 6)

    def test_keyword_plus(self):
        self.check('4 plus 2', 6)

    def test_keyword_addition(self):
        self.check('addition of 4 and 2', 6)

    def test_keyword_total(self):
        self.check('total of 4 and 2', 6)

    def test_keyword_summation(self):
        self.check('summation of 4 and 2', 6)

    def test_keyword_added(self):
        self.check('4 and 2 are added', 6)

    def test_keyword_added_modifier_with(self):
        self.check('4 is added with 2', 6)

    def test_keyword_added_modifier_to(self):
        self.check('4 is added to 2', 6)

    # ************ Subtraction *********************************

    def test_keyword_subtract(self):
        self.check('subtract 4 and 2', 2)

    def test_keyword_difference(self):
        self.check('difference between 4 and 2', 2)

    def test_keyword_minus(self):
        self.check('4 minus 2', 2)

    def test_keyword_subtraction(self):
        self.check('subtraction of 4 and 2', 2)

    def test_keyword_subtracted(self):
        self.check('4 and 2 are subtracted', 2)

    def test_keyword_added_modifier_from(self):
        self.check('2 is subtracted from 4', 2)

    # ************ Multiplication *********************************

    def test_keyword_into(self):
        self.check('4 into 2', 8)

    def test_keyword_multiply(self):
        self.check('multiply 4 by 2', 8)

    def test_keyword_multiply_modifer_by(self):
        self.check('4 multiply by 2', 8)

    def test_keyword_times(self):
        self.check('4 times 2', 8)

    def test_keyword_product(self):
        self.check('product of 4 and 2', 8)

    def test_keyword_multiplied(self):
        self.check('4 and 2 are multiplied', 8)

    def test_keyword_multiplied_modifier_to(self):
        self.check('4 is multiplied to 2', 8)

    def test_keyword_multiplied_modifier_with(self):
        self.check('4 is multiplied with 2', 8)

    def test_keyword_multiplied_modifier_by(self):
        self.check('4 is multiplied by 2', 8)

    def test_keyword_multiplication(self):
        self.check('multiplication of 4 and 2', 8)

    # ************ Division *********************************

    def test_keyword_divide(self):
        self.check('divide 4 by 2', 2)

    def test_keyword_divide_modifier_by(self):
        self.check('4 divide by 2', 2)

    def test_keyword_division(self):
        self.check('division of 4 and 2', 2)

    def test_keyword_over(self):
        self.check('4 over 2', 2)

    def test_keyword_divided(self):
        self.check('4 divided by 2', 2)

    # ************ Factorial *********************************

    def test_keyword_factorial(self):
        self.check('5 factorial', 120)

    def test_keyword_factorial_modifier_of(self):
        self.check('factorial of 5', 120)

    # ************ Exponent *********************************

    def test_keyword_power(self):
        self.check('4 raised to power 2', 16)

    def test_keyword_root(self):
        self.check('root 4', 2)

    def test_keyword_square(self):
        self.check('4 square', 16)

    def test_keyword_square_modifier_of(self):
        self.check('square of 4', 16)

    def test_keyword_square_modifier_root(self):
        self.check('square root of 4', 2)

    def test_keyword_cube(self):
        self.check('4 cube', 64)

    def test_keyword_cube_modifier_of(self):
        self.check('cube of 4', 64)

    def test_keyword_cube_modifier_root(self):
        self.check('cube root of 8', 2)

    # ************ Constants *********************************

    def test_keyword_pi(self):
        import math
        self.check('what is pi', math.pi)

    def test_keyword_e(self):
        import math
        self.check('what is e', math.e)

    # ************ Invalid *********************************

    def test_invalid_type1(self):
        with self.assertRaises(ValueError):
            self.calculator.calculate('who are you')

    def test_invalid_type2(self):
        with self.assertRaises(ValueError):
            self.calculator.calculate('2 and 3')


class IsNumericTestCase(unittest.TestCase):

    def test_integer(self):
        self.assertTrue(is_numeric('5'))

    def test_decimal(self):
        self.assertTrue(is_numeric('5.5'))

    def test_non_numeric(self):
        self.assertFalse(is_numeric('hello'))


class Convert2NumericTestCase(unittest.TestCase):

    def test_integer(self):
        result = convert_to_numeric('5')
        self.assertEqual(result, 5)
        self.assertIsInstance(result, int)

    def test_decimal(self):
        result = convert_to_numeric('5.5')
        self.assertEqual(result, 5.5)

    def test_non_numeric(self):
        with self.assertRaises(ValueError):
            convert_to_numeric('hello')

class Text2IntTestCase(unittest.TestCase):

    def test_no_number(self):
        result = text2int('what is up')
        self.assertEqual(result , 'what is up')

    def test_simple_number(self):
        result = text2int('what is five plus three')
        self.assertEqual(result, 'what is 5 plus 3')

    def test_big_number(self):
        result = text2int('fifty six thousand birds')
        self.assertEqual(result, '56000 birds')

    def test_with_and(self):
        result = text2int('five and two')
        self.assertEqual(result, '5 and 2')

    def test_with_and_in_number(self):
        result = text2int('five hundred and two birds')
        self.assertEqual(result, '502 birds')


if __name__ == '__main__':
    unittest.main()
