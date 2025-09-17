import re
# re.match(pattern,string)
text="hello word"
result=re.match("hello",text)
print(result.group())
