# A number of people are pulling matches. Some matches 
# are long, some are short. Those who get the long matches 
#win. When should you pull for the match?

import random

PEOPLE = 20
NUM_LONG = 3 
NUM_SHORT = PEOPLE - NUM_LONG
SHORT = 0
LONG = 1

class Game():
  def __init__(self):
    self.__SetUpMatches()
    self.draws = []
    self.wins = []
    
  # Create list of short and long matches
  def __SetUpMatches(self):
    self.matches = []
    [self.matches.append(LONG) for i in range(NUM_LONG)]
    [self.matches.append(SHORT) for i in range(NUM_SHORT)]
    random.shuffle(self.matches)
    # we will randoml pull indecies from "available_indecies"
    # and place them into "draws"
    self.available_indecies = range(len(self.matches))

  def Play(self):
    [self.Draw() for i in range(PEOPLE)]
    
  def Draw(self):
    next_idx = random.choice(self.available_indecies)
    self.available_indecies.remove(next_idx)
    self.draws.append(next_idx)
    # Did I win (pulled the long stick)?
    self.wins.append(self.matches[next_idx] == LONG)

  def PrintDebug(self):
    print 'Matches:', self.matches
    print 'Draws:', self.draws
    print 'Wins:', self.wins

def main():
  """docstring for main"""
  # Initialize wins aggregates
  wins_by_player = []
  [wins_by_player.append(0) for i in range(PEOPLE)]
  iter_num = 10000
  for i in range(iter_num):
    g = Game()
    g.Play()
    for j in range(PEOPLE):
      if g.wins[j]:
        wins_by_player[j] += 1
  success_rate_by_player = []
  [success_rate_by_player.append(100. * w / iter_num) for w in wins_by_player]
  print "Wins By Player:", wins_by_player
  print "Success rate By Player:", success_rate_by_player
  print "Equal-opportunity chance:", 100. * NUM_LONG / PEOPLE

if __name__ == '__main__':
  main()
  
  # def SuccessRate__(self):
  #   iter_num = 10000
  #   for i in range(iter_num):
  #     self.Iterate()
  #     for p in range(len(self.results)):
  #       if self.Won(p):
  #         self.successes[p] += 1.0
  #   for player in range(len(self.results)):
  #     success_rate = 100 * (self.successes[player] / iter_num)
  #     print 'Player {0}s success rate:', success_rate
  # 
  # def __SuccessRate(self, player):
  #   iter_num = 10000
  #   success_total = 0
  #   for i in range(iter_num):
  #     random.shuffle(self.matches)
  #     if self.Iterate().Won(player):
  #       success_total += 1.0
  #   success_rate = 100 * (success_total / iter_num)
  #   print 'Player {0}s success rate:', success_rate
  # 
  # def SuccessRate(self):
  #   for p in range(PEOPLE):
  #     self.__SuccessRate(p)
  # 
  # def Iterate(self):
  #   iter_num = 1000
  #   iterations = 0
  #   while iterations <= iter_num:
  #     self.results = []
  #     random.shuffle(self.matches)
  #     while len(self.results) != PEOPLE:
  #       self.Draw()
  #     for p in range(len(self.results)):
  #       if self.Won(p):
  #         self.successes[p] += 1.0
  #     iterations += 1
  #   print self.successes
  #   for p in range(len(self.successes)):
  #     success_rate = 100 * (self.successes[p] / iter_num)
  #     print 'Player {0}s success rate:'.format(p+1), success_rate
