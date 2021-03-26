dict1 = {101:"Gulzar", 102:"Paveen", 103:"Sabreen"}
dict2 = {101:21.5, "Gulzar":True, 102:"Ahmad"}
dict3 = {101:"Gulzar", 102:"Ahmad", 103:"Shaik", 101:"Parveen"}

print(dict1)
print(dict2)
print(type(dict1))
print(type(dict2))

print("Dictonery is mutable:")
print(dict1[101])
print(dict2["Gulzar"])

print("Duplicates keys not allowed", dict3)

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict["colors"])
print(thisdict["colors"][1])

x = thisdict.get("year")
print(x)

y = thisdict.keys()
print(y)

thisdict["brand"] = True
print(thisdict)
print(y)

z = thisdict.values()
print(z)

x = thisdict.items()
print(x)

for i,j in thisdict.items():
    print(i, '---------',j)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")