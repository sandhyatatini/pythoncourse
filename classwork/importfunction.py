import sys
import math
import random
import collections
print(math.sqrt(25))
print(math.pow(3,2))
print(math.floor(23.8))
print(math.ceil(24.08))
print(math.fabs(-93))
print(math.tan(90))
print(math.sin(60))
print(math.cos(23))
print(math.degrees(23))
print(math.pi)

print(random.random())
print(random.randint(1,6))
print(random.uniform(2,7))
l=["Sandhya","Sandeep","Bhavani","Hari","Hemu"]
print(random.choice(l))
print(random.choices(l,k=3))
random.shuffle(l)
print(l)

names=["Sandhya","sandeep","Bhavani","Hari","Hemu","sandhya","sandeep","Sivadevi","Rambabu"]
c=collections.Counter(names)
print(c)

names="python programming"
d={}
for i in names:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
#-----------------------
def word_count(sentence):
    words=sentence.split()
    freq={}
    for word in words:
        freq[word]=freq.get(word,0)+1
    return freq
sentence=input()
print(word_count(sentence))