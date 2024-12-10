'''#dice code
import random
while True:
    int(input("enter the roll of dice:"))
    a=random.randint(1,6)
    print(a)
    option=input("roll again?(y/n)")
    if option=='y':
        continue
    elif option=='n':
        break
    else:
        print("invalid option")'''
'''import time
import random
for i in range(10):
    a=random.randint(2000,6000)
    print(a)
    time.sleep(2)'''

#regex(regular expressions)
'''Regular expressions are powerful tools(modules) embedded in python which is mainly used to find a pattern within a given string
or statements or files will mainly use it for text manipulation'''

'''a="codegnan is in vja"
print(a)'''

'''b="codegnan\nis\tin\nvja"
print(b)'''

'''c=r"codegnan\nis\tin\tvja"
print(c)'''

'''#compile(),search(),findall(),split(),sub()
#sequene characters
b\w->alphanumeric
\W->non alphanumeric
\d->matches any digit
\D->matches non digit
\s->it represents white spaces
\S->It represents non white spaces'''
#compile
import re
a="mat cat cap maths code cash money map codegnan"
b=re.compile(r"m\w\w\w\w")
print(b)

#search()
c=b.search(a)
print(c)

b=re.search(r"m\w+",a)
print(b)

#findall
c=re.findall(r"m\w+",a)
print(c)
print(*c)



