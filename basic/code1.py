
friends = {"a", "b", "c"}
aborad = {"t", "b", "c"}
aborad2 = { "b", "c"}

temp = aborad.difference(friends)
temp2 = aborad2.difference(friends)
print(temp) # {'t'}
print(temp2) # empty set()

friends = ["a", "b"]
friends2 = ["a", "b"]
stranger = ["c"]

print(friends == friends2) # True
print(friends is friends2) # False  check for memory address
