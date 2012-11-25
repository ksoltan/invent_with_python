import caesar

print 'd,hi,13 -> ', caesar.getTranslatedMessage('decrypt', 'hi', 13)
print 'd,uv,13 -> ', caesar.getTranslatedMessage('decrypt', 'uv', 13)
print 'e,hi,1 -> ', caesar.getTranslatedMessage('encrypt', 'hi', 1)

print 'd,abxyz,13 -> ', caesar.getTranslatedMessage('decrypt', 'abxyz', 13)
print 'd,noklm,13 -> ', caesar.getTranslatedMessage('decrypt', 'noklm', 13)
