import json
from datetime import datetime as e
# Python dictionary
python_dict = {"name": "John", "age": 30, "city": "New York"}

# Serialize the dictionary to JSON
json_data = json.dumps(python_dict)
print(json_data)

# Deserialize JSON to a Python dictionary
new_python_dict = json.loads(json_data)

# Print the resulting dictionary
print(new_python_dict)


# Example: Working with datetime
now = e.now()
print("Current date and time:", now)

# Format the datetime object as a string
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date:", formatted_date)
