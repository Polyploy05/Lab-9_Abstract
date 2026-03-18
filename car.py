'''
Name: Daniel Puerto & Jacob Miranda
Date: 3/17/26
Group: 13
Description:
'''


import vehicle
import random 

class Car(Vehicle):
  def special_move(self, obs_loc):
    if self.energy < 15:
            self._location += 1
            return f"{self.name} did not have enough energy for nitro and moved 1 space."

    self._energy -= 15
    
    distance = int(1.5 * self.speed) + random.randint(-1, 1)
    target = self.location + distance

    if obs_loc is not None and obs_loc <= target:
      self._location = obs_loc
      return (
            f"{self.name} used nitro for {distance} spaces but CRASHED at obstacle "
            f"at {obs_loc}!"
      )

    self._location = target
    return f"{self.name} used nitro and moved {distance} spaces."
