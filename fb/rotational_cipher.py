
#O(n) spacetime
from string import ascii_lowercase as low, ascii_uppercase as up
numbers = "0123456789"

# memoization?
def rotate(char, rotation_factor):
  # lowercase case
  if char in low:
    return chr((ord(char)+rotation_factor-ord("a"))%26+ord("a"))
  # uppercase case
  elif char in up:
    return chr((ord(char)+rotation_factor-ord("A"))%26+ord("A"))
  # number case
  elif char in numbers:
    return chr((ord(char)+rotation_factor-ord("0"))%10+ord("0"))
  # else
  else:
    return char


def rotationalCipher(input, rotation_factor):
  # Write your code here
  res = []
  for char in input:
    res.append(rotate(char, rotation_factor))
  print(res)
  return "".join(res)
