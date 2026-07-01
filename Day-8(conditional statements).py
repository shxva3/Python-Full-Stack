'''statements:
   -----------
1.conditional satatemnet--->if
                            if-else
                            elif
                            nested if

2.control statement---->break
                        continue
                        pass

3.loop statements--->for
                     while

if:
---
num=7
if num%2 == 0:
    print(f"{num} is even number")
else:
    print(f"{num} is odd number")

eg-2:
-----
sbi_details={"ATM pin" : '2233'}
pin=input("Enter your pin: ")
if pin in sbi_details['ATM pin']:
    print("Welcome to SBI ATM")
else:
    print("you entered wrong pin")


nested if:
----------
sbi_details={"ATM pin" : '2233'}
pin=input("Enter your pin: ")
if len(pin) == 4:
    if pin in sbi_details['ATM pin']:
        print("Welcome to SBI Atm")
    else:
        print(f"{pin} is incorrect")
else:                                                                            
    print("Enter only 4 digits")


Task: print max value in given number
-----'''
a=int(input("Enter a number"))
b=int(input("Enter a number"))
c=int(input("Enter a number"))
if a>=b and a>=c:
    print('a is max value')
elif b<=a and b>=c:
    print('b is max value')
elif c>=a and c>=b:
    print('c is max value')
else:
    exit


