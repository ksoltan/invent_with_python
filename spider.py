# SPIDER
#  SPINS
#   LINE
#  REELS
#     IN
#-------
# INSECT

def RemoveFromRange(num_range, vals):
  for val in vals:
    if val in num_range:
      num_range.remove(val)

answers = []
# S cannot be 0 (because SPIDER should not start with 0) and
# cannot be 9 (because S + anything - will result extra digit)
for s in range(1, 9):
  p_range = range(10)
  RemoveFromRange(p_range, [s])
  print 'Checking s =', s
  for p in p_range:
    # I cannot be 0 (because IN should not start with 0)
    i_range = range(1, 10)
    RemoveFromRange(i_range, [s, p])
    print 'Checking p =', p
    for i in i_range:
      d_range = range(10)
      RemoveFromRange(d_range, [s, p, i])
      # print 'Checking i =', i
      for d in d_range:
        e_range = range(10)
        RemoveFromRange(e_range, [s, p, i, d])
        for e in e_range:
          # R cannot be 0 (because REELS should not start with 0)
          r_range = range(1, 10)
          RemoveFromRange(r_range, [s, p, i, d, e])
          for r in r_range:
            n_range = range(10)
            RemoveFromRange(n_range, [s, p, i, d, e, r])
            for n in n_range:
              # L cannot be 0 (because LINE should not start with 0)
              l_range = range(1, 10)
              RemoveFromRange(l_range, [s, p, i, d, e, r, n])
              for l in l_range:
                c_range = range(10)
                RemoveFromRange(c_range, [s, p, i, d, e, r, n, l])
                for c in c_range:
                  t_range = range(10)
                  RemoveFromRange(t_range, [s, p, i, d, e, r, n, l, c])
                  for t in t_range:
                    # SPIDER
                    #  SPINS
                    #   LINE
                    #  REELS
                    #     IN
                    #-------
                    # INSECT
                    if t != ((r + s + e + s + n) % 10):
                      continue
                    else:
                      sum_of_nums = \
                        100000*s + 10000*p + 1000*i + 100*d + 10*e + r + \
                                   10000*s + 1000*p + 100*i + 10*n + s + \
                                             1000*l + 100*i + 10*n + e + \
                                   10000*r + 1000*e + 100*e + 10*l + s + \
                                                              10*i + n
                      sum_from_digits = \
                        100000*i + 10000*n + 1000*s + 100*e + 10*c + t
                      if sum_of_nums == sum_from_digits:
                        answ = '''
s = {0},
p = {1}, 
i = {2},
d = {3},
e = {4},
r = {5},
n = {6},
l = {7},
c = {8},
t = {9}

{0}{1}{2}{3}{4}{5}
 {0}{1}{2}{6}{0}
  {7}{2}{6}{4}
 {5}{4}{4}{7}{0}
    {2}{6}
------
{2}{6}{0}{4}{8}{9}
'''.format(s, p, i, d, e, r, n, l, c, t)
                        print "Got answer:\n", answ
                        answers.append(answ)
