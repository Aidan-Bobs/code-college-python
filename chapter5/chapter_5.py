cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())



#gets an input from the user by askin them their name
my_name= input("whats your name? ")

#checks if name is Aidan
if my_name == "Aidan":
    #if the name is aidan the it prints the bellow sentence
    print("hello, awesomest guy")
elif my_name == "David":
    print("hello, Mr. David")
else:
    print(f"Hello, {my_name}")

