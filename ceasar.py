# This uses Caesar Cypher to encrypt or decrypt a message. 

MAX_KEY_SIZE = 26 # capital letters: global variable

def getMode():
  while True:
    print 'Do you wish to encrypt or decrypt a message?'
    mode = str(raw_input).lower()
    if mode in 'encrypt e decrypt d'.split():
      return mode
    else:
      print 'Print either "encrypt", "e", "decrypt", or "d".'

def getMessage():
  print 'Enter your message:'
  return input()

def getKey():
  key = 0
  while True:
    print 'Enter your key number, {0}:'.format(MAX_KEY_SIZE)
    key = int(input())
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
        if num > ord('a'):
            num += 26
      translated += chr(num)
    else:
      translated += symbol
  return translated

mode = getMode()
message = getMessage()
key = getKey()

print 'Your translated message is:'
print getTranslatedMessage(mode, message, key)