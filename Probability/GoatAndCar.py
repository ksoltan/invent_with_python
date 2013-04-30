# Three doors: two goats and one car. Pick one door, the locutor opens a door with goat. Your choice: change your door, or stay with your first pick.

import random

GOAT = 0
CAR = 1

STRATEGY_KEEP = False
STRATEGY_CHANGE = True

class Game():
  def __init__(self, strategy):
    self.strategy = strategy
    self.doors = [GOAT, GOAT, CAR]
    random.shuffle(self.doors)
    self.firstIndex = -1
    self.secondIndex = -1
    self.thirdIndex = -1
    
  def PrintDebug(self):
    print 'Strategy:', self.strategy
    print 'Doors:', self.doors
    print 'First Index:', self.firstIndex
    print 'Second Index:', self.secondIndex
    print 'Third Index:', self.thirdIndex
    print 'Won:', self.Won()
  
  def Won(self):
    return self.doors[self.thirdIndex] == CAR

  def Play(self):
    self.FirstStep()
    self.SecondStep()
    self.ThirdStep()
    return self

  def StrategySuccessRate(self):
    if self.strategy:
      strategy_name = 'change'
    else:
      strategy_name = 'keep'
    iter_num = 10000
    success_total = 0.0
    for i in range(iter_num):
      if self.Play().Won():
        success_total += 1
    success_rate = (success_total / iter_num) * 100
    print "Strategy {0} success rate: {1}%".format(strategy_name, success_rate)
      
  def FirstStep(self):
    self.firstIndex = random.randint(0, 2)

  def SecondStep(self):
    all_indexes = range(len(self.doors))
    # remove first step index
    all_indexes.remove(self.firstIndex)
    # remove car index
    for i in all_indexes[:]:
      if self.doors[i] == CAR:
        all_indexes.remove(i)
    # pick random goat index
    random.shuffle(all_indexes)
    self.secondIndex = all_indexes[0]

  def ThirdStep(self):
    if self.strategy:
      self.__ThirdStepChange()
    else:
      self.__ThirdStepKeep()

  def __ThirdStepChange(self):
    all_indexes = range(len(self.doors))
    # remove first and second step indexes
    all_indexes.remove(self.firstIndex)
    all_indexes.remove(self.secondIndex)
    # pick the only index left
    self.thirdIndex = all_indexes[0]

  def __ThirdStepKeep(self):
    self.thirdIndex = self.firstIndex
