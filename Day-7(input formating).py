'''         Input formatinng from user
input()
---------
The input() function is used to take input from the user..

1.int()
-------
it only takes interger values
eg:
num=int(input("Enter a number: "))
num2=int(input("Enter a number: "))
print(num + num2)
o/p:
Enter a number: 5
Enter a number: 4
9

2.char()
--------
eg:
num=input("Enter a char: ")
num2=input("Enter a char: ")
print(num + num2)
o/p:
Enter a char: shiva
Enter a char: 3
shiva3

3.float()
---------
eg:
num=input("Enter a number: ")
num2=input("Enter a number: ")
print(num + num2)
o/p:
Enter a number:2.0
Enter a number:3.1
5.1

4.list()
--------
group=list(map(int,input().split()))
print(group)
o/p:
23 45 67
[23, 45, 67]

5.Tuple()
---------
group=tuple(map(int,input().split()))
print(group)
some=tuple(map(int,input().split()))
print(group)
o/p:
1,2
(1,2)

EVAL()
------
num=eval(input("Enter: "))
print(type(num))
o/p:
->Enter: 56
<class 'int'>
->'shiva'
'shiva'
->Enter: 6.22
<class 'float'>
{"mani" : 3,
 "ramu" : 5}
 
{'mani': 3, 'ramu': 5}

F-String:
---------
name=input("Enter your name: ")
age=int(input("enter your age: "))
print(name,"and my age is: ",age)
print(f"{name} your age is: {age}")

Modulus()
--------
name=input("Enter your name: ")
age=int(input("enter your age: "))
print("your name is %s your age is %d" %(name,age))
o/p:
Enter your name: shiva
enter your age: 22
your name is shiva your age is 22'''










