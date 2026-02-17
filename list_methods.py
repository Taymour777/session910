a = [1, 2, 3]
a.append(27)
print(a)
b = ["Bob"] * 4
a.extend(b) # adds one list at the end, same as a + b
print(a)

# pop removes by position!
x = a.pop(3)
print(x)
print(a)

a.remove(3)
print(a)
while True:
    try:
        a.remove("Bob")
    except ValueError:
        break
print(a)
