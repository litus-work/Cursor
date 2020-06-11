class Cat:

    def __init__(self, age):
        self.age = age
        self.average_speed = self._set_average_speed()
        self.saturation_level = 50

    products = {
        "fodder": 10,
        "apple": 5,
        "milk": 2
    }

    def eat(self, product):
        product = product.lower()
        if product in self.products.keys():
            self._increase_saturation_level(self.products.get(product))

    def _reduce_saturation_level(self, value):
        self.saturation_level -= value
        if self.saturation_level < 0:
            self.saturation_level = 0

    def _increase_saturation_level(self, value):
        self.saturation_level += value
        if self.saturation_level > 100:
            self.saturation_level = 100

    def _set_average_speed(self):
        if self.age in range(0, 8):
            return 12
        elif self.age in range(8, 11):
            return 9
        elif self.age > 10:
            return 6
        else:
            raise ValueError

    def run(self, run_hours):
        run_km = run_hours * self.average_speed
        if run_km <= 25:
            self._reduce_saturation_level(2)
        elif 25 < run_km <= 50:
            self._reduce_saturation_level(5)
        elif 50 < run_km <= 100:
            self._reduce_saturation_level(15)
        elif 100 < run_km <= 200:
            self._reduce_saturation_level(25)
        else:
            self._reduce_saturation_level(50)
        return run_km

    def get_saturation_level(self):

        if self.saturation_level > 0:
            return self.saturation_level
        else:
            return "Your cat is died :("

    def get_average_speed(self):
        return self.average_speed

