class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return f'Model: {self.__model}'

    def get_horsepower(self):
        return f'Engine power:{self.__engine_power}'

    def get_color(self):
        return f'Color:{self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Owner:{self.owner}')

    def set_color(self, new_color):
        new_color_lower = new_color.lower()
        if new_color_lower in self.__COLOR_VARIANTS:
            self.__color = new_color_lower
        else:
            print(f"You can't change the color to {new_color_lower}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()