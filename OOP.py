class Cat:

    def __init__(self, age):
        self.age = age
        self.saturation_level = 50
        self.average_speed = self._set_average_speed()

    def _increase_saturation_level(self, value):
        self.saturation_level += value
        if self.saturation_level < 0:
            self.saturation_level = 0

    def _reduce_saturation_level(self, value):
        self.saturation_level -= value
        if self.saturation_level > 100:
            self.saturation_level = 100

    products = {'fodder': 10, 'apple': 5, 'milk': 2}

    def eat(self, product):
        if product in self.products.keys():
            self._increase_saturation_level(self.products.get(product))

    def _set_average_speed(self):
        if self.age in range (0, 8):
            return 12
        elif self.age in range(8, 11):
            return 9
        elif self.age > 10:
            return 6
        else:
            raise ValueError

    def run(self, hours):
        ran_km = self.average_speed * hours
        if 25 >= ran_km:
            self._reduce_saturation_level(2)
        elif 25 < ran_km < 50:
            self._reduce_saturation_level(5)
        elif 50 < ran_km < 100:
            self._reduce_saturation_level(15)
        elif 100 < ran_km < 200:
            self._reduce_saturation_level(25)
        elif ran_km > 200:
            self._reduce_saturation_level(50)
        return f"Your cat ran {ran_km} kilometers"

    def get_saturation_level(self):
        if self.saturation_level > 0:
            return self.saturation_level
        else:
            return 'Your cat is died :('

    def get_average_speed(self):
        return self.average_speed

class Cheetah(Cat):

    products = {'gazelle': 30, 'rabbit': 15}

    def eat(self, product):
        if product in self.products.keys():
            self._increase_saturation_level(self.products.get(product))

    def _set_average_speed(self):
        if self.age in range (0,6):
            return 90
        elif self.age in range (6, 16):
            return 75
        elif self.age > 15:
            return 40




class Wall:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def wall_square(self):
        square_wall = self.width * self.height
        return square_wall

    def number_of_rolls_of_wallpaper(self, roll_width_m, roll_length_m):
        lines_in_roll = roll_length_m/self.height
        lines = self.width / roll_width_m
        number = lines / lines_in_roll
        return number


    

      # Example:
      #     count of lines in roll eq roll length in meters divide height of the wall (use rounding down)
      #     count of lines eq width of the wall divide roll width in meters
      #     number of rolls of wallpaper eq count of lines divide  count of lines in roll


    # def __init__(self, width, height):
    #     pass
    #
    # def wall_square(self):
    #     pass
    #
    # def number_of_rolls_of_wallpaper(self, roll_width_m, roll_length_m):
    #     pass


class Roof:
    """
        * Implement class Roof which receives such parameters: width, height and roof_type

        * Implement method roof_square that returns square of the roof
          if roof_type eq "gable" the roof square if simple rectangle square formula multiplied 2
          if roof_type eq "single-pitch" the roof square if simple rectangle square formula
          if other roof_type raise ValueError like this "Sorry there is only two types of roofs"

    """

    def __init__(self):
        pass

    def roof_square(self):
        pass


class Window:
    """
       * Implement class Window which receives such parameters: width and height

       * Implement method window_square which return result of simple square formula of rectangle

    """

    def __init__(self):
        pass

    def window_square(self):
        pass


class Door:
    """
     * Implement class Door which receives such parameters: width and height
      add variables wood_price eq 10, metal_price eq 3

     * Implement method door_square which return result of simple square formula of rectangle

     * Implement method door_square which receives material value as a parameter
       if material eq wood return door_square multiplied on wood_price
       if material eq metal return door_square multiplied on metal_price
       if material value is another one (not metal or wood) raise ValueError "Sorry we don't have such material"

     *  Implement method update_wood_price which receives new_price value and updates your old price

     *  Implement method update_metal_price which receives new_price value and updates your old price

    """

    def __init__(self):
        pass

    def door_square(self):
        pass

    def door_price(self):
        pass

    def update_wood_price(self):
        pass

    def update_metal_price(self):
        pass


class House:
    """
    !!!! DON'T WRITE NEW METHODS TO THIS CLASS EXCEPT FOR THOSE LISTED BELOW !!!

    * Add super private variable __walls and its value will be empty list
    * Add super private variable __windows and its value will be empty list
    * Add super private variable __roof and its value will be None
    * Add super private variable __door and its value will be None

    * Implement method create_wall which will create new wall using class Wall and add it to the __walls list
      it receives parameters width and height
      if width or height eq 0 raise ValueError "Value must be not 0"
      if user have more than 4 walls raise ValueError "Our house can not have more than 4 walls"

    * Implement method create_roof which will create new roof using class Roof and assign it to the __roof variable
      it receives parameters width, height and roof_type
      if width or height eq 0 raise ValueError "Value must be not 0"
      Check that we won't have another roof if we already have another one,
              otherwise raise ValueError "The house can not have two roofs"

    * Implement method create_window which will create new window using class Window and add it to the __windows list
      it receives parameters width and height
      if width or height eq 0 raise ValueError "Value must be not 0"

    * Implement method create_door which will create new door using class Door and assign it to the __door variable
      it receives parameters width and height
      if width or height eq 0 raise ValueError "Value must be not 0"
      Check that we won't have another door if we already have another one,
              otherwise raise ValueError "The house can not have two doors"

    * Implement method get_count_of_walls that returns count of walls

    * Implement method get_count_of_windows that returns count of windows

    * Implement method get_door_price that receives material value and returns price of the door

    * Implement method update_wood_price that receives new_wood_price and updates old one

    * Implement method update_metal_price that receives new_metal_price and updates old one

    * Implement method get_roof_square that returns the roof square

    * Implement method get_walls_square that returns sum of all walls square that we have

    * Implement method get_windows_square that returns sum of all windows square that we have

    * Implement method get_door_square that returns the square of the door

    * Implement method get_number_of_rolls_of_wallpapers that returns sum of the number of rolls of wallpapers
      needed for all our walls
      it receives roll_width_m, roll_length_m parameters
      Check if roll_width_m or roll_length_m eq 0 raise ValueError "Sorry length must be not 0"

    * Implement method get_room_square that returns the square of our room
      (from walls_square divide windows and door square)

    """

    def __init__(self):
        pass

    def create_wall(self):
        pass

    def create_roof(self):
        pass

    def create_window(self):
        pass

    def create_door(self):
        pass

    def get_count_of_walls(self):
        pass

    def get_count_of_windows(self):
        pass

    def get_door_price(self):
        pass

    def update_wood_price(self):
        pass

    def update_metal_price(self):
        pass

    def get_roof_square(self):
        pass

    def get_walls_square(self):
        pass

    def get_windows_square(self):
        pass

    def get_door_square(self):
        pass

    def get_number_of_rolls_of_wallpapers(self):
        pass

    def get_room_square(self):
        pass




