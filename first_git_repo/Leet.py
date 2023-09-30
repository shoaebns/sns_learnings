def is_palindrome(string):
  for i in range(len(string) // 2):
    if string[i] != string[-i - 1]:
      return False
  return True
    

str = (input())

is_palindrome(str)
