from pathlib import Path


""" path = Path('my_name.txt')
contents = path.read_text()

line_no = 1
lines = contents.splitlines()
for line in lines:
    
    print(f"Line {line_no}: {line}")
    line_no = line_no + 1 """


new_path = Path("new_file.txt")

file_text = "Today was a day that was being a day.\n"

file_text += "We learnt how to open .txt files in python"

file_text += "I am learning coding at a bootcamp. \nToday was a very long day \nthe weekend was super short \nits been raining all day"

file_text += "Coding is not for the weak.\n"


input_text = input("what you gotta say?")

file_text += input_text

new_path.write_text(f"{file_text}\ncoding can make you go nuts!\n")

print(f"Go check the {new_path.name}")
