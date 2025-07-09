my_dict={"name":"sandhya","branch":"ece","cource":"python"}
copied=my_dict.copy
print(f"returns ashallow copy: {copied}")
print(my_dict.get("keys"))
for key, value in my_dict.items():
    print(key, value)
print(list(my_dict.keys()))
print(list(my_dict.values()))
value=my_dict.pop("name")
print(value)
pair=my_dict.popitem()
print(pair)
my_dict.update({"b":4,"rf":4})
print(my_dict)
my_dict.setdefault("b",9)
print(my_dict)