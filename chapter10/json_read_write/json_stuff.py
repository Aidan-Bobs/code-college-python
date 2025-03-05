from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]

numbers_json_path = Path("numbers.json")
content_numbers_json = json.dumps(numbers)

numbers_json_path.write_text(content_numbers_json)

