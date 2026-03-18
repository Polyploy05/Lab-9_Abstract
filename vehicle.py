'''Name: Jacob Miranda & Daniel Puerto
Date: 03/16/26
Group: 13
Description:
'''

import random
import abc

class Vehicle:
    def __init__(self, name, initial, speed):
        self._name = name
        self._initial = initial
        self._speed = speed
        self._position = 0
        self._energy = 100

    def fast(self, obs_loc):
        if self._energy >= 5:
            self._energy -= 5
            movement = random.randint(-1, 1) + self._speed
        else:
            return self.slow(obs_loc)
        
        self._position += movement
        if obs_loc is not None and self._position >= obs_loc:
            self._position = obs_loc
            return f"{self._name} sped through {movement} spaces but CRASHED into an obstacle at {obs_loc}!"
        else:
            return f"{self._name} sped through {movement} spaces."

    def slow(self, obs_loc):
        movement = random.randint(-1, 1) + (self._speed // 2)
        self._position += movement
        if movement > obs_loc:
            return f"{self._name} moved forward {movement} spaces and drove around the obstacle at {obs_loc}!"
        else:
            return f"{self._name} moved forward {movement} spaces"
    
    def __str__(self):
        return f"{self.name()} (Energy: {self.energy()}, Position: {self.position()})"
    

    def initial(self):
        return self._initial
    
    def name(self):
        return self._name   
    
    def position(self):
        return self._position
    
    def energy(self):
        return self._energy
    

    @abc.abstractmethod
    def special_move(self):
        pass
