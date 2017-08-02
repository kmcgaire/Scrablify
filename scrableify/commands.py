import sys


def scrableify():
  string = sys.argv[1]
  ret_val = ""
  points = 0
  for c in string:
    ret_val += emojify(c)
    points += get_char_value(c)
  print ret_val + " ({} points)".format(points)

def emojify(char):
  if char == " ":
    return ":scrabble-blank:"
  elif char.isalpha():
    return ":scrabble-{}:".format(char)
  else:
    return char

SCRABBLE_VALUES = {
  "a": 1,
  "b": 3,
  "c": 3,
  "d": 2,
  "e": 1,
  "f": 4,
  "g": 2,
  "h": 4,
  "i": 1,
  "j": 8,
  "k": 5,
  "l": 1,
  "m": 3,
  "n": 1,
  "o": 1,
  "p": 3,
  "q": 10,
  "r": 1,
  "s": 1,
  "t": 1,
  "u": 1,
  "v": 4,
  "w": 4,
  "x": 8,
  "y": 4,
  "z": 10,
}

def get_char_value(char):
  if char.isalpha():
    return SCRABBLE_VALUES[char.lower()]
  else:
    return 0


