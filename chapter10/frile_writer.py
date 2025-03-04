""" from pathlib import Path


contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"

path = Path('programming.txt')
path.write_text(contents) """

new_text = input("what do you want to write? ")

with open("my_name.txt", "a") as text_file:
    text_file.write