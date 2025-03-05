from pathlib import Path
import json

json_numbers_path = Path('numbers.json')
json_numbers_contents = json_numbers_path.read_text()
numbers = json.loads(json_numbers_contents)



print(numbers)