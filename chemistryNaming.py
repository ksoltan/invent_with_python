# How to name chemical compunds
# Practice wih classes

class IonicCompound():
  """docstring for IonicCompound"""
  def __init__(self, anion, cation):
    self.anion = anion
    self.cation = cation

class Ion():
  """docstring for Ion"""
  def __init__(self, anion, cation, anion_oxidation, cation_oxidation):
    #IonicCompound.__init__(self, anion, cation)
    self.anion = anion
    self.cation = cation
    self.anion_oxidation = anion_oxidation
    self.cation_oxidation = cation_oxidation
  def AnionName(self):
    """docstring for AnionNaming"""
    if self.anion_oxidation == 1 or self.anion_oxidation == 2 or self.anion in ['Ag', 'Zn', 'Cd', 'Al']:
      anion_name = self.anion + ' ion'
    else:
      anion_name = self.anion + ' ({0}) ion'.format(self.anion_oxidation)
    return anion_name
  def CationName(self):
    """docstring for CationNaming"""
    if len(self.cation) == 1:
      if self.cation.endswith('on'):
        cation_name = self.cation - 'on' + 'ide'
      if self.cation.endswith('ine'):
        cation_name = self.cation - 'ine' + 'ide'
    else:
      cation_name = 0
    return cation_name
