""" Program to test Banking """
import io
import unittest
import unittest.mock
from main import deposit
from main import withdraw
from main import enquiry

class TestBanking(unittest.TestCase):
    """ Class to test Banking """
    def test_deposit(self):
        """ Test that it can deposit """
        result = deposit(0, 100)
        self.assertEqual(result, 100)
    def test_withdraw_sufficient(self):
        """ Test that it can withdraw when sufficient balance """
        result = withdraw(100, 10)
        self.assertEqual(result, 90)
    def test_withdraw_insufficient(self):
        """ Test that it cannot withdraw when insufficient balance """
        result = withdraw(100, 1000)
        self.assertEqual(result, 100)
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_enquire(self, mock_stdout):
        """ Test that it can enquire """
        enquiry(100)
        self.assertEqual(mock_stdout.getvalue(), 'Your Balance = 100\n')

if __name__ == '__main__':
    unittest.main()
