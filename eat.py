class Breakfast():
    def __init__(self, food, person):
        self.food = food
        self.person = person
        self.amount = 10

    def __str__(self):
        return "{}, {}".format(self.food, self.person)


    def eat(self):
        self.amount -= 1
        print(self.amount)

    def reorder(self):
        self.amount = 10
        print('There you go no need to worry!')
    




person1 = Breakfast('Pancakes', 'Angel')


person1.eat()
person1.eat()
person1.eat()
person1.reorder()



print(person1)