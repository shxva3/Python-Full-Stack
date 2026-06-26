                 List Datatypes
                 --------------
-->list is a collection of data type that are enclosed in []separated by,
-->list is muttable

any_datatype=[1,'python',[3,5]]
print(any_datatype)
o/p:
[1, 'python', [3, 5]]

Muttable                                        Immutable
--------                                        ---------
the data type can be modified                   The data type cannot be modified(can only makes changes in string)

eg:list                                         eg:string


METHODS:
--------

1.append()

-->This is only used to add new item,but at the last of the list
eg:
    variable_name.append()
    any=[1,2,3]
    any.append(4)
    
   print(any)
o/p:[1, 2, 3, 4]

2.extend()
-->This is used to add new item at end of list,but it add new item and allocate for each character
eg:
any_=[1,2,3,4]
any_.extend('python')
print(any_)
[1, 2, 3, 4, 'p', 'y', 't', 'h', 'o', 'n']
print(len(any_))
10
any_=[1,2,3,4]
any_.append('python')
print(any_)
[1, 2, 3, 4, 'python']
print(len(any_))
5


3.pop()
-->this used to delete the value in a list based on index position.
any=[2,5,7,45,90]
     
any.pop(1)
     
5
print(any)
     
[2, 7, 45, 90]


4.delete()
-->this is used to delete an item based on direct value.
eg:
    any=[2,5,7,45,90]
     
    any.pop(7)
    7
    print(any)
    [2,5,45,90]
    
