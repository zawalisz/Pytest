from is_prime import is_prime
import pytest

@pytest.mark.parametrize("number, result", [(2,True), (3,True), (4,False), (5,True), (6,False), (7,True), (8,False), (9, False)])

def test_is_prime(number, result):
    assert is_prime(number) == result