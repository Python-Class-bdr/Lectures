from animal import Animal


class Fish(Animal):
    def __init__(self, color, swim_speed=0):
        super().__init__(color, "fish")
        self.swim_speed = swim_speed

    # def __str__(self):
    #     return f'{self.color} {self.animal_type}'

    # ! This is the same as the __str__ method above.
    # ? This is the same as the __str__ method above.
    # Todo: Try to understand why this is the same as the __str__ method above.
    # -> The __str__ method is a special method that is called when you call the str() function on an object.
    
    
# Nilgun says:sdfasdfasdf


a_fish = Fish("blue")
string_representation = str(a_fish)  # 'blue fish'
print(string_representation)
