class Heart:
    def __init__(self, usage):
        self._usage = usage
    
    @property
    def state(self):
        if self._usage > 70:
            return "high blood pressure"
        return "feeling good"


class Brain:
    def __init__(self, usage):
        self._usage = usage
    
    @property
    def state(self):
        if self._usage > 90:
            return "tired"
        return "rested"
        

class Person:
    def __init__(self, heart_usage, brain_usage):
        self.heart = Heart(heart_usage)
        self.brain = Brain(brain_usage)


class Leg:
    def __init__(self, moving_speed):
        self._moving_speed = moving_speed
        
    @property
    def state(self):
        if abs(self._moving_speed) > 10:
            return "running"
        elif self._moving_speed == 0:
            return "standing"
        else:
            return "walking"

if __name__ == "__main__":
    person = Person(50, 90)
    print(person.heart.state)
    print(person.brain.state)
    Person.leg = Leg(0)
    print(person.leg.state)
    Person.leg = Leg(5)
    print(person.leg.state)
    Person.leg = Leg(11)
    print(person.leg.state)