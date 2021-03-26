myset = {"apple", "orange", "bannana","orange", "apple"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print("Set Example:", myset)
print("Data Type:", type(myset))


print("Duplicates not allowed:", myset)
print("Length count will be with out duplicate:", len(myset))

a = set(("apple", "cherry", "grapes"))
print("Set Constructor:", a)

print("Access Set ")
for x in a :
    print(x)

print("apple" in a)

a.add("orange")
print("After Set adding:",a)

b = {"pineapple", "mango", "pappaya"}
a.update(b)
print(a)

thisset = {"Test1", "Test2", "Test3"}
mylist = ["List1", "List2", "List3"]

thisset.update(mylist)
print("updating List and set:", thisset)

#Note: If the item to remove does not exist, remove() will raise an error.
thisset.remove("Test1")

#Note: If the item to remove does not exist, discard() will NOT raise an error.
thisset.discard("New1")

#Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.
x = thisset.pop()
print("Deleted iteam of pop method:",x)

print("After pop deletion", thisset)

# clear will clear the set
thisset.clear()
print("After clear function:", thisset)

#The del keyword will delete the set completely:
del thisset


#Join two sets 
#The union() method returns a new set with all items from both sets:
set1 = {"a", "b","c"}
set2 = {1,2,3}
set3 = set1.union(set2)

print("Union Set:", set3)

#The update() method inserts the items in set2 into set1:
set1.update(set2)
print("After update set:", set1)

#The intersection() method will return a new set, that only contains the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print("Intersection:", z)

#The intersection_update() method will keep only the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

#The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print("Symmetric_defference_update:", x)

#The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z= x.symmetric_difference(y)