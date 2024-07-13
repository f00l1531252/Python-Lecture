class Car:
    def __init__(self, model_name, mileage, manufacturer):
        self.model_name = model_name
        self.mileage = mileage
        self.manufacturer = manufacturer

    def gas(self):
        print('{0.model_name} アクセル全開 （燃費{0.mileage}/l)'.format(self))

    def brakes(self):
        print(f'{self.model_name} ブレーキ')

class Truck(Car):
    def __init__(self, model_name, mileage, manufacturer, max_payload, payload):
        self.max_payload = max_payload
        self.payload = payload
        super().__init__(model_name=model_name, mileage=mileage, manufacturer=manufacturer)
        self.show_payload()

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
            if self.payload + weight < 0:
                self.payload = 0
                print(f'{self.payload}tの荷物を降ろしました。')
                self.show_payload()
            else:
                self.payload += weight
                print(f'{-weight}tの荷物を降ろしました')
                self.show_payload()

    def show_payload(self):
        print(f'現在の積載料は{self.payload}tです。')


if __name__ == '__main__':
    prius = Car('プリウス', 30, 'TOYOTA')
    prius.gas()
    prius.brakes()

