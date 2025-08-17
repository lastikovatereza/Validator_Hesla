import pytest
from validator_hesla import ValidatorHesla

@pytest.mark.parametrize("heslo, expected", [
    ("abc123", True),       # validní heslo
    ("ab1", False),         # příliš krátké
    ("abcdefg", False),     # bez číslice
    ("", False),            # prázdné heslo
    ("123456", True),       # jen čísla, validní
])
def test_je_validni(heslo, expected):
    assert ValidatorHesla.je_validni(heslo) == expected