"""
The program should contain a random function which randomizes from 1-6 and shows the input as dice
1= *
2 = **
3= ***
"""
import random
c=(random.randint(1,6))
print(c)
a={1:"*",2:"*   *",3:"*   *\n  *",4:"*   *\n*   *",5:"*   *\n  *\n*   *",6:"*   *\n*   *\n*   *"}
print(a[c])



