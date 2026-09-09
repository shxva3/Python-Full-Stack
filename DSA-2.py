
marks =[]
for i in range(3):
    mark = int(input(f"Enter mark {i + 1}: "))
    marks.append(mark)
print("Marks after append:", marks)

marks.insert(0, 90)
print("After inserting 90:", marks)
marks.extend([75, 85])
print("After extending 75 and 85:", marks)
if 75 in marks:
    marks.remove(75)
    print("75 removed from the list")
removed_value = marks.pop()
print("Removed final mark:", removed_value)
print("Final marks list:", marks)
print("length of marks:", len(marks))



numbers = [20, 10, 30, 20, 40, 20]
print("Original list:", numbers)
numbers.sort()
print("Ascending order:", numbers)

numbers.reverse()
print("Descending order:", numbers)

search_num = int(input("Enter a number to search: "))

if search_num in numbers:
    print(search_num, "is found in the list")
    print("Count:", numbers.count(search_num))
    print("First index:", numbers.index(search_num))
else:
    print(search_num, "is not found in the list")
    print("\nNumerical Summary")
    print("Smallest value:", min(numbers))
    print("Largest value:", max(numbers))
    print("Total:", sum(numbers))


          

