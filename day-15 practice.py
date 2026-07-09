       practice using Functions
       ------------------------
nums=[23,4,6,23,7,4]
empty=[]
def removes(nums,empty):
    for j in nums:
        empty.append(j)
    print(empty)
removes(nums,empty)

prime=7
count=0
def prime_not(prime,count):
    for j in range(1,prime+1):
        if prime%j == 0:
            count+=1
    if count == 2:
        print(f"{prime} is a prime")
    else:
        primt(f"{prime} is not a prime")
prime_not(prime,count)

some = "python is a programming Language"
count =0
def counting(some,count):
    so=some.split(' ')
    for j in so:
        count+=1
    print(count)
counting(some,count)

some = 'python is a programming Language'
cap_count=0
small_count=0
space_count=0
def cap_small(some,cap_count,small_count,space_count):
    for j in some:
        if j.isupper():
            cap_count+=1
        elif j.islower():
            small_count+=1
        else:
            space_count+=1
    print(f"{cap_count}")
    print(f"{small_count}")
    print(f"{space_count}")
cap_small(some,cap_count,small_count,space_count)
            
        

