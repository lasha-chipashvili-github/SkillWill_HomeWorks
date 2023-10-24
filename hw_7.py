from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass
    
    
class Car(Vehicle):
    def __init__(self, max_speed, current_speed):
        self._max_speed = max_speed
        self._current_speed = current_speed
        
        
    def start_engine(self):
        return "car started"
    
    def stop_engine(self):
        return "car stopped"
    
class SportCar(Car):
    def __init__(self, max_speed, current_speed):
        super().__init__(max_speed, current_speed)
        
    def start_engine(self):      
        return f"{super().start_engine()} and it's max speed is {self._max_speed}"
    
    def stop_engine(self):
        self._current_speed = 0
        return f"{super().stop_engine()} and it's current speed is {self._current_speed}"
    
    
if __name__ == "__main__":
    lambo = SportCar(100, 45)
    print(lambo.start_engine())
    print(lambo.stop_engine())