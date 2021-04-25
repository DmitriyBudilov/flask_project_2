import os
import json
from data import goals, teachers

# print(teachers)
with open("data.json", "w") as json_file:
    json.dump(teachers, json_file, indent=4, ensure_ascii=False)

