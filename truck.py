'''
Name: Daniel Puerto & Jacob Miranda
Date: 3/17/26
Group: 13
Desc: Creates class for truck and the special move 
'''

import vehicle
import random

class Truck(Vehicle):

  def special_move(self, obs_loc):

    if self.energy < 20:
      self._location += 1
      return f"{self.name} did not have enough energy and moved 1 space."


    #Deducts energy
    self._energy -= 20


    #Calculates distance
    distance = (2 * self.speed) + random.randint(-1,1)
    start = self.location 
    target = start + distance


    if obs_loc is not None and obs_loc <= target:

      self._location = target 
      return(
          f"{self.name} used its ramming power, smashed through an obstacle at
          f"{obs_loc}, and moved {distance} spaces!"
      )

    self._location = target
    return f"{self.name} used its ramming power and moved {distance} spaces."
