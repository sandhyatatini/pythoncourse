import re
text="Hello world"
result=re.search("world",text)
print(result.group())
text = "cat bat mat rat"
result = re.findall(r"\bbat\b", text)  # \b = word boundary
print(result)  # ['bat']
text = "hello 123 world 456"
result = re.sub(r"\d+", "#", text)  # replace digits with #
print(result)  # hello # world #
text = "apple,banana;cherry orange"
result = re.split(r"[,; ]+", text)
print(result)  # ['apple', 'banana', 'cherry', 'orange']

