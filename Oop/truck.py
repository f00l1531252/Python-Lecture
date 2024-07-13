from car import Car


class Truck(Car):
    def __init__(self, model_name, mileage, manufacturer, max_payload):
        self.max_payload = max_payload
        self.payload = 0
        super().__init__(model_name=model_name, mileage=mileage, manufacturer=manufacturer)
        self.show_payload()

    def gas(self):
        if self.payload == self.max_payload:
            print('積載量がMAXです。気をつけて運転してください。')
        else:
            super().gas()

    def load(self, weight):
        if weight > 0: # 積載
            if self.payload + weight > self.max_payload:
                print(f'最大積載量は{self.max_payload}tのため{weight}tの荷物は積めません。'
                      f'{(self.payload+weight) - self.max_payload}tの荷物を降ろしてください。')
            else:
                self.payload += weight
                print(f'{weight}tの荷物を積みました')
                self.show_payload()
        else:
            if self.payload < -weight:
                print(f'{self.payload}t全ての荷物を降ろしました。')
                self.payload = 0
                self.show_payload()
            else:
                self.payload += weight
                print(f'{-weight}tの荷物を降ろしました')
                self.show_payload()

    def show_payload(self):
        print(f'現在の積載料は{self.payload}tです。')


if __name__ == '__main__':
    truck = Truck('Truck', 10, 'いすゞ', 10)
    print('#########')
    truck.load(3)
    print('#########')
    truck.load(8)
    print('#########')
    truck.load(-3)
    print('#########')
    truck.load(8)
    print('#########')
    truck.load(-10)
    print('#########')
    truck.gas()
    print('#########')
    truck.load(10)
    truck.gas()


