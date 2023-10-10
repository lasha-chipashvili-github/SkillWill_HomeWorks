class Car:
    
    def __init__(self, brand, model, production_year, color, horse_power, is_sport_car=False):
        self.__brand = brand
        self.__model = model
        self.__production_year = production_year
        self.__color = color
        self.__horse_power = horse_power
        self.__is_sport_car = is_sport_car
        
  
    def get_brand(self):
        return self.__brand
    

    def get_model(self):
        return self.__model
    

    def get_production_year(self):
        return self.__production_year
    

    def get_color(self):
        return self.__color
    

    def get_horse_power(self):
        return self.__horse_power
    

    def get_is_sport_car(self):
        return self.__is_sport_car
    
    
    def change_color(self, new_color):
        self.__new_color = new_color
        if self.__new_color == self.__color:
            return False
        self.__color = self.__new_color
        return True
        
    
    def increase_horse_power(self, hp:int):
        self.__hp = hp
        if self.__hp > 0:
            self.__horse_power += self.__hp
            return True
        return False
    

if __name__ == "__main__":   
    car = Car('Audi', 'TT', 2012, 'red', 211, True)
    print(car.get_brand())
    print(car.get_model())
    print(car.get_production_year())
    print(car.get_color())
    print(car.get_horse_power())
    print(car.get_is_sport_car())
    print(car.change_color('red'))
    print(car.change_color('lylac'))
    print(car.get_color())
    print(car.increase_horse_power(0))
    print(car.increase_horse_power(54))
    print(car.get_horse_power())  