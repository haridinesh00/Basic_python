import random
def dice():
    c=(random.randint(1,6))
    print(c)
    a={1:"*", 2:"* *", 3:"* *\n *", 4:"* *\n* *", 5:"* *\n*\n* *", 6:"* *\n* *\n* *"}
    print(a[c])
