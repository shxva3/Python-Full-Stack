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

am_str=int(input("Enter a number: "))          # eg:153=1^3+5^3+3^3=153
length=len(str(am_str))
all_sum=0
for j in str(am_str):
    all_sum+=int(j)**length
if all_sum==am_str:
    print(f"{am_str} is an amstrong number")
else:
    print(f"{am_str} is not an amstrong number")

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
 ,,,
*******************
