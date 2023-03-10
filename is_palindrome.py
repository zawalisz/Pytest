def is_palindrome(n):
  n = str(n).replace(' ', '').lower()
  return n == n[::-1]