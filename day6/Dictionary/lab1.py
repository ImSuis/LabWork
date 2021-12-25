#Write a Python script to sort (ascending and descending) a dictionary by value. 
import operator
integer = {"first":1,"third":3,"fifth": 5,"second":2,"ninty":90}
sorted_integer = dict( sorted(integer.items(), key=operator.itemgetter(1)))
print(sorted_integer)