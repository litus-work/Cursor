import uuid


class Restaurant:
    def __init__(self, name, stars, city):
        self.name = name
        self.stars = stars
        self.id_rest = str(uuid.uuid4())
        self.city = city


class Table:
    def __init__(self, number, guest_count, rest_name, user):
        self.number = number
        self.guest_count = guest_count
        self.id_table = str(uuid.uuid4())
        self.rest_name = rest_name
        self.user = user


    # def get_table_id(self, id):
    #     pass


class City:
    def __init__(self, name):
        self.name = name
        # self.id_city = id_city
        self.id_city = str(uuid.uuid4())
