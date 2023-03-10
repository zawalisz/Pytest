from is_palindrome import is_palindrome
def test_is_palindrome():
  assert is_palindrome("atak kata")
  assert is_palindrome("ada bzy zbada")
def test_is_not_palindrome():
  assert not is_palindrome("mama")
  assert not is_palindrome("wiedzieć")
  assert not is_palindrome("mmazurek.dev")