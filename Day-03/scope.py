import random

print(random.randrange(1,100))


a = "Python"
print(a[0])
print(a[-1])
print(len(a))

for i in a:
    print(i)

txt = "The best things in life are free!"
print("free" in txt)


print(txt[0:3])

print(txt[3:-1])
print(txt[0:])

# Comparision
== 

# Assignment
=


a +=  6;
a = a+6

b -= 7
b = b -7
"""

# global keyword

def greeting():
    global name
    name  = "Sadeed"
    print(f"{name}, welcome to CBC!")

greeting()

def greetingmessage():
    print(f"{name} is learning Python")

greetingmessage()
"""


"""
# local
def greeting():
    name  = "Sadeed"
    print(f"{name}, welcome to CBC!")

greeting()

name = "Sara"
print(name)

def greetingmessage():
    print(f"{name} is learning Python")

greetingmessage()

"""


"""
# Global
name  = "Sadeed"

def greeting():
    print(f"{name}, welcome to CBC!")

greeting()

"""
