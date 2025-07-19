import json
import jsonschema

with open("kontakte.json", mode="r", encoding="utf-8") as f:
    json_object = json.load(f)

with open("kontakte_schema.json", mode="r", encoding="utf-8") as f:
    json_schema = json.load(f)

try:
    jsonschema.validate(instance=json_object, schema=json_schema)
except jsonschema.ValidationError as e:
    print(f'Validation Error: {e}')
