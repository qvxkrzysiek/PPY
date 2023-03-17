string1 = "Python 2023"
string2 = "Python 2023"
string3 = string1

print(string1 == string2)  # True
print(string2 == string3)  # True

print(type(string1), hex(id(string1)))  # <class 'str'> id
print(type(string2), hex(id(string2)))  # <class 'str'> id
print(type(string3), hex(id(string3)))  # <class 'str'> id

string3 = "Java 11"

print(string1 == string2)  # True
print(string2 == string3)  # False

print(type(string1), hex(id(string1)))  # <class 'str'> id
print(type(string2), hex(id(string2)))  # <class 'str'> id
print(type(string3), hex(id(string3)))  # <class 'str'> id