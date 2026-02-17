from os import name


def greeting():
    """
    Prints out a bunch of greetings in various languages
    :return: None
    """
    print("Hello")
    print("Ciao")
    print("Hola")
    print("Ni hao")

def greeting2(name):
    """
    Prints out a bunch of greetings in various languages
    :param name: the name of the person to greet
    :return:
    """
    print("Hello", name)
    print("Ciao", name)
    print("Hola", name)
    print("Ni hao", name)

def greeting3(name):
    """
    Prints out a bunch of greetings in various languages
    :param name: 
    :return: 
    """
   message = ""
   message += f"Hello {name}\n"
   message += f"Ciao {name}\n"
   message += f"Hola {name}\n"

for i in range(10):
    greeting()
print("I can take a break")
for i in range(5):
    greeting2("Benjamin")
