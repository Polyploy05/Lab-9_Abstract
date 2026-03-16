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

    def fast(self):
        if self._energy >= 5:
            self._energy -= 5
            movement = random.randint(-1, 1) + self._speed
            self._position += movement
            return movement
        else:
            self.slow()

    def slow(self):
        movement = random.randint(-1, 1) + (self._speed // 2)
        self._position += movement
        return movement
    
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