string
------
string is a sequence of character that are enclosed in ' '," ",""" """
str is immutable

concatination
-------------
-->Here, the (+) operator acts as concatination more than 2 strings
eg:
    so="python"
    any="is a language"
    print(so+any)
O/P:pythonis a language

INDEXING:
--------
-->This is used to access the particular char in the string by pass index position value..
-->Index start from 0..
-->we have negative indexing to count from last to first
eg:
so="python"
any="is a language"
print(so[5])
print(so[-4])
O/P:
    n
    t

METHODS
-------
1.replace()
-->we can replace the old str with new str
syntax:
    variable.replace("old str",new str)

    eg:print(so.replace("python","java"))
    O/P:java

2.JOIN()
-->it is used to add sub string to the string

SYNTAX: "sub str".join(string)
eg:
    so="python is a language"
    print("-".join(so))
O/P:p-y-t-h-o-n- -i-s- -a- -l-a-n-g-u-a-g-e

3.split()
-->it is used to separate the string as substrings
eg:
    so="python is a language"
    print(so.split())
o/p:['python', 'is', 'a', 'language']

4.count
-------
used to count the characters in the string based on indexing

eg;
so="python is a language"
print(so.count())

BUILT IN FUNCTION IN STR:
1.Len()
used to count length of str

2.max()
used to count maximum characters in string

3.min()
used to count minimum characters in string















              
