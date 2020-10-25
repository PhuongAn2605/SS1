class Car:
    def __init__(self, __year_model, __make, __speed):
        self.__year_model = __year_model
        self.__make = __make
        self.__speed = __speed

    def accelerate(self):
        self.__speed = self.__speed + 5

    def brake(self):
        self.__speed = self.__speed - 5

    def get_speed(self):
        return self.__speed


if __name__ == '__main__':
    car = Car(2010, 'Ford', 80)
    for i in range(5):
        car.accelerate()
        print(car.get_speed(), end=' ')
    print()
    for i in range(5):
        car.brake()
        print(car.get_speed(), end=' ')