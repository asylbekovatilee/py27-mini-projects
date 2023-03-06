import json

# loads: json -> python kod                         
# dumps: python -> json kod


with open('db.json','r+') as file:
    python_obj = json.load(file)

    python_obj.append({'title':'Samsung', 'price': 1200})

    json.dump(python_obj, file)

# dict_ = {'a': 1, 'b': 2, 'c': 3}
# json_obj = json.dumps(dict_)
# print(json_obj)

# json_obj = '{"a": 1, "b": 2, "c": 3}'
# python_bj = json.loads(json_obj)
# print(python_bj)

