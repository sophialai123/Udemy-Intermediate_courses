
"""
OOPs : classes and objects:
Attributes(variables ): Means what the object has and it is variable
Methods (functions): what the object does, and it is a function.

                         attributes:  is_holding_plate = True
                                      tables_responsible = [4,5,6]


  Waiter(object,Class)     Methods:   def take_order(table,order):
                                   # takes order to chef

                               def take_payment(amount):
                                   # add money to restaurant

Class(blueprint) :  object
Car = CarBlueprint ()  #  Car is the object and CarBlueprint() is the Class (第一个字母大写)

car.speed
#object.attributes       has(attributes):
                                         speed = 0
                                          fuel = 32





car.stop()
#object.method                  does(methods):
                                def move():
                                    speed = 60
                                def stop():
                                     speed = 0


"""
# from turtle import Turtle, Screen
# timmy = Turtle() # timmy is object and Turtle is attribute
# print(timmy)
# timmy.shape("turtle") # shape is the method.
# timmy.color("blue")
# timmy.forward(100)
# timmy.color("blue")

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["pikachu","squirtle","charmander"])
table.add_column("Type", ["electric","water","fire"])
table.align = "l"
print(table)