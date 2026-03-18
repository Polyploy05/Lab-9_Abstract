'''
Name:
Date:
Group:
Description:

'''

import vehicle
import random


class Motorcycle(Vehicle):

  def special_move(self, obs_loc):

    if self.energy < 10:
      self._location += 1
      return f"{self.name} did not have enough energy and moved 1 space."

    if random.randint(0,1) == 0:
      return f"{self.name} attempted a stunt but FELL OVER and did not move!"

    self._energy -= 10

    distance = (2 * self.speed) + random.randint(-1, 1)
    target = self.location + distance


    if obs_loc is not None and obs_loc <= target:
      self._location = obs_loc
      return(
          f"{self.name} preformed a stunt for {distance} spaces but CRASHED " 
          f"into an obstacle at {obs_loc}!"
      )

    self._location = target
    return f"{self.name} preformed a stunt and moved {distance} spaces."
