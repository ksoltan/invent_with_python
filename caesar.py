# This uses Caesar Cypher to encrypt or decrypt a message. 

MAX_KEY_SIZE = 26 # capital letters: global variable

def getMode():
  while True:
    print 'Do you wish to encrypt, decrypt, or brute force a message?'
    mode = raw_input().lower()
    if mode in 'encrypt e decrypt d brute b'.split():
      return mode
    else:
      print 'Print either "encrypt", "e", "decrypt", "d", "brute", "b"'

def getMessage():
  print 'Enter your message:'
  return raw_input()

def getKey():
  key = 0
  while True:
    print 'Enter your key number, {0}:'.format(MAX_KEY_SIZE)
    key = int(raw_input())
    if key >= 1 and key <= MAX_KEY_SIZE:
      return key
      
def getTranslatedMessage(mode, message, key):
  if mode[0] == 'd':
    key = -key
  translated = ''
  
  for symbol in message:
    if symbol.isalpha(): # only encrypting letters. if it is a letter, its ASCII will be changed.
      num = ord(symbol)
      num += key
      
      if symbol.isupper():
        if num > ord('Z'):
          num -= 26
        elif num < ord('A'):
          num += 26
      if symbol.islower():
        if num > ord('z'):
          num -= 26
        elif num < ord('a'):
            num += 26
      translated += chr(num)
    else:
      translated += symbol
  return translated

def main():
  mode = getMode()
  message = getMessage()
  if mode[0] != 'b': #why do you need mode[0]?
    key = getKey()

  print 'Your translated message is:'
  if mode[0] != 'b':
    print getTranslatedMessage(mode, message, key)
  else:
    for key in range(1, MAX_KEY_SIZE + 1):
      print key, getTranslatedMessage('decrypt', message, key)
