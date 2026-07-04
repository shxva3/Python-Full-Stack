'''num=int(input("Enter a number: "))
count=0
for j in range(1,num+1):
    if num%j==0:
        count+=1
if count==2:
    print(f"{num} is a prime")
else:
    print(f"{num} is not a prime")

o/p:
Enter a number: 7
7 is a prime
----------------------------------    

num=int(input("Enter a number:"))
for j in range(1,num+1):
        for i in range(1,j+1):
            print("*",end=" ")   #end is 
        print()

Enter a number:5
* 
* * 
* * * 
* * * * 
* * * * *
--------------------------------

num=int(input("Enter a number:"))
count=0
for j in range(1,num+1):
        for i in range(1,j+1):
            count+=1
            print(count,end=" ")
        print()

Enter a number:4
1 
2 3 
4 5 6 
7 8 9 10 
------------------------------------

a=int(input("Enter a number: "))          # eg:153=1^3+5^3+3^3=153
b=len(str(am_str))
c=0
for j in str(a):
    c+=int(j)**b
if c==a:
    print(f"{a} is an amstrong number")
else:
    print(f"{a} is not an amstrong number")

o/p:
Enter a number: 153
153 is an amstrong number

----------------------------------------


num=10
for j in range(num):
    print(" "*(num-j-1),end="")
    print("*"*(2*j+1))

o/p:
         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
 ----------------------------------------

a=int(input("Enter a number: "))          # eg:153=1^3+5^3+3^3=153
b=len(str(a))
c=0         #count
for j in str(a):
    c+=int(j)**b
if c==a:
    print(f"{a} is an amstrong number")
else:
    print(f"{a} is not an amstrong number")

---------------------------------------------

num=int(input("Enter a number: "))
for i in range(1,num+1):
    print("* "*(i))

---------------------------------

num=int(input("Enter a number: "))
for j in range(num):
    print(" "*(num-j-1),end="*")
    for i in range(j+1):
        print(i,end="*")
 ------------------------------
 
n=int(input())
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(i):
        print(i-j,end="")
    print()
 -----------------------------
so=input("Enter a word: ")
empty= ""
for j in so:
    empty=j+empty
    print(

-------------------------------
num=0
num_2=1
limit=int(input())
print(num,num_2,end=" ")
for i in range(1,limit+1):
    all=num+num_2
    num=num_2
    num_2=all
    print(all,end=" ")
-------------------------------
calculator 
val=int(input("Enter a number"))
val2=int(input("Enter a number"))
user_in=int(input("enter \n1.add \n2.sub \n3.mul \n4.pow: "))
if user_in ==1:
    print(val+val2)
elif user_in ==2:
    print(val-val2)
elif user_in ==3:
    print(val*val2)
else:
    print(val**val2)

--------------------------------
table=int(input("Enter a number: "))
for val in range(1,13):
    print(f"{table} X {val} = {table*val}")
--------------------------------
'''
num=int(input("Enter a number:"))
sum_=0
for j in range(1,num):
    if num%j==0:
        sum_+=j
if sum_==num:
    print(f"{num} is a perfect num")
else:
    print(f"{num} is not a perfect num")




    

















