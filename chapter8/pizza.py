def pizza_oven():
    num_toppings = int(input("How many toppings would you like? "))  
    toppings = choose_toppings(num_toppings)
    print(f"Your pizza has the following toppings: {toppings}")

def choose_toppings(no=1):
    choices = []
    while len(choices) < no:
        topping = input(f"Choose topping {len(choices) + 1}: ")  
        choices.append(topping)  
    return ", ".join(choices)  




def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
 location='princeton',
 field='physics')






def multiply(*numbers):
    x, y = numbers
    z = x*y
    return z



def process_values(*values):
    for value in values:
        print(2*value)

