import sys


def scrableify():
  string = sys.argv[1]
  ret_val = ""
  for c in string:
    ret_val += emojify(c)
  print ret_val

def emojify(char):
  if char == " ":
    return "    "
  else:
    return ":scrabble-{}:".format(char)

