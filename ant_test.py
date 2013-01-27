import ant

WEIGHTS = [
    [  0, 44, 72, 91, 47, ],
    [ 63, 50, 69, 33, 61, ],
    [ 16, 35, 84, 57, 76, ],
    [ 55, 88, 50, 35, 24, ],
    [ 48, 66, 19, 41,  0 ]
]

print 'indeces of 44 (0, 1):', ant.FindIndex(44)
print 'indeces of 57 (2, 3):', ant.FindIndex(57)
print 'indeces of 66 (4, 1):', ant.FindIndex(66)

x = ant.FindAllPaths([], 0)
print 'starting from 0:', x