
def add(a,b):
    c=a+b
    return c
print(add(5,6))

c='Shiva '
d='Gopi'
print(add(c,d))
a,b=map(str,input('enter the values').split(','))

def sample(*a): #(*)--> takes n-number of dynamic input
    print(a)
    print(type(a))
sample(2,3,4,5)
sample('codegnan',[2,4,56],2+5j,'shiva')
        
a,*b,c=23,45,76,4354,876
print(a)
print(b)

def add(*a):
    print(a)
    result=0
    for i in a:
        if type(i) in [int,float]:
            result=result+i
    return result
print(add(2,3,4))
print(add(2,'codegnan',3,4,234.54,[23,45]))
----------------------------------------------------
def batch(name,place,age): #march argument position
    print(f'{name} is in {place} and age is {age}')
batch('shiva','vizag',21)

----------------------------------------------------

def batch(name,place=HYD,age): #march argument position and we can declare the arguments by default.but not first arg(syntax error)
    print(f'{name} is in {place} and age is {age}')
batch('shiva','vizag',21)
---------------------------------------------------
def batch(**a): #(**)--> to display output as dict type(keys:values)
    print(a)
    print(type(a))
batch()
batch(name='sanjay',age=22,place='hyd',branch='cse')

data = {'name':['rocky','prem'],
        'place':['hyd','viz']}

data.update({'batch':'PFS-VSP-004'})
batch(**data)
