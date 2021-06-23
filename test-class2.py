class Transportation:

    def drive(self):
        print('drive method is called.')


class Car(Transportation):
    def accelerate(self):
        print('on the road')


class Airpaln():
    def fly(self):
        print("on the air")


car = Car()
car.accelerate()

airplan = Airpaln()
airplan.fly()
# car1 = car('Toyato', '17')
# car2 = car('藍寶堅尼', '24')

# print(car1.brand+' 輪子是 '+car1.wheel+' 吋')
# print(car2.brand+' 輪子是 '+car2.wheel+' 吋')
