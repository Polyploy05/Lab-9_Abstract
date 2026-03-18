'''
Name: Daniel Puerto & Jacob Miranda
Date: 3/17/26
Group: 13
Description: Creates the class for Car and creates the special move and calculates the distance for the special move
'''


import vehicle
import random 

class Car(Vehicle):
  def special_move(self, obs_loc):
    #Special move is created that accelerates the car 
    if self.energy < 15:
            self._location += 1
            return f"{self.name} did not have enough energy for nitro and moved 1 space."

    #Deducts energy
    self._energy -= 15

    #Calculates distance
    distance = int(1.5 * self.speed) + random.randint(-1, 1)
    target = self.location + distance

    #If there is an obstacle, car crashes
    if obs_loc is not None and obs_loc <= target:
      self._location = obs_loc
      return (
            f"{self.name} used nitro for {distance} spaces but CRASHED at obstacle "
            f"at {obs_loc}!"
      )

    #If the nitro boost is successful
    self._location = target
    return f"{self.name} used nitro and moved {distance} spaces."
