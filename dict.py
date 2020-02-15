mag = "my name is khan"
note = "shahrukh khan"
from collections import defaultdict
dict1  = defaultdict(int)
dict2 = defaultdict(int)
for word in mag.split(" "):
    print(word)
    dict1[word] +=1
for word in note.split(" "):
    dict2[word] +=1
print(dict1)
print(dict2)
