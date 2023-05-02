import json

x =  '{ "name":"John", "age":30, "city":"New York"}'

def convert_json():

	y = json.loads(x)

	print(y["name"])
convert_json()

x1 = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

def convert_python():
	z = json.dumps(x1)
	print(z)

convert_python()