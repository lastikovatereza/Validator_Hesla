import unittest
from validator_hesla import ValidatorHesla

class ValidatorHeslaTests(unittest.TestCase):

    def test_validni_heslo(self):
        validator = ValidatorHesla()
        self.assertTrue(validator.je_validni("abc123"))

    def test_kratke_heslo(self):
        validator = ValidatorHesla()
        self.assertFalse(validator.je_validni("ab1"))

    def test_heslo_bez_cislice(self):
        validator = ValidatorHesla()
        self.assertFalse(validator.je_validni("abcdefg"))

    def test_prazdne_heslo(self):
        validator = ValidatorHesla()
        self.assertFalse(validator.je_validni(""))

if __name__ == '__main__': unittest.main()