""" def my_function(user, game):
    user.strip().lower().title()
    game.strip().lower().title()
    print(f"Welcome back to {game}, hope you have fun, {user}")

my_function("aidan", "game")



def true_title(name, gender = "male"):
    if gender == "male":
        print(F"Good afternoon, Duke {name.strip().lower().title()}")
    else:
        print(F"Good afternoon, Dutchess {name.strip().lower().title()}")

true_title(name = "Aidan")

my_list = [1, 2, 3, 4, 5]
second = [2,4,6,8,10]


def my_test_function(f_list):
    f_list[::-1]
    for i in f_list:
        print(i)


def what_name(first, last = None):
    if last == None:
        print(f"your name is {first}")
    else:
        print(f"your full name is {first, last}") """

from pizza import pizza_oven as pizza_store

pizza_store()

