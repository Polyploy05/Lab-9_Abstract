'''
Name: Daniel Puerto & Jacob Miranda
Date: 3/17/26
Group: 13
Description:

'''

import vehicle
import random


class Motorcycle(Vehicle):

  def slow(self, obs_loc):
    base = int(self.speed * 0.75)
    distance = base + random.randint(-1,1)
    if distance < 1:
      distance = 

    target = self._location + distance 

    if obs_loc <= target:
      moved = obs_loc - self._location - 1
      if moved < 1:
        moved = 1
      self._location += moved
      return f"{self.name} moved slowly around an obstacle for {moved} spaces."
    
    #No obstacle
    self._location = target
    return f"{self.name} moved slowly for {distance} spaces."

  def special_move(self, obs_loc):

    if self.energy < 15:
      self._location += 1
      return f"{self.name} did not have enough energy and moved 1 space."

    self._energy -= 15

    if random.random() >= 0.75:

      self._location += 1
      return f"{self.name} attempted a stunt but FELL OVER and moved only 1 space!"


    distance = (2 * self.speed) + random.randint(-1, 1)
    if distance < 1:
      distance = 1
      
    target = self.location + distance


    if obs_loc <= target:
      self._location = obs_loc
      return(
          f"{self.name} preformed a stunt for {distance} spaces but CRASHED " 
          f"into an obstacle at {obs_loc}!"
      )

    self._location = target
    return f"{self.name} preformed a stunt and moved {distance} spaces."
