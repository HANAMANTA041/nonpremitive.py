"""
##To check all keywords in python
import keyword
keywords = keyword.kwlist
print(keywords)

#Non premitive Data types:List,Tuple,Dictionary,Set
#list is mutable data structure,can contain heterogeneous data structure
If we want to represent group of objects as a single entity, where insertion 
order is preserved and duplicate objects are allowed, objects are separated by 
comma (,) then we use list data structure.
List elements we can access using index same as string.
Negative indexing is also applicable to list.
List elements we can access using slicing same as string concept.
We can iterate over list using loops.

 

number_list = []
a = list(range(0,9))#range(): is a function which returns
#a = [1,2,"Tony",(4,5),3.4,[1,4]]
#a = list(sequence) => here sequence can a list, tuple, set, dictionary, string
l = list ("Bengaluru")
print(l)

l1 = [1, 2, [3, 5, ,333, 222], 4, 999]
for i in l1:
    print(i)

#Methods
l = [11, 22, 33]
      
l
      
[11, 22, 33]
len(l)
      
3
a.count(11)
      
0
l1 = [1,2,3,4,5,3,4]
      
l1
      
[1, 2, 3, 4, 5, 3, 4]
a.count(3)
      
1
l2 = [1,1,1,]
      
l2
      
[1, 1, 1]
l2.count(1)
      
3
l2.append(2)
      
l2
      
[1, 1, 1, 2]
l2.extend([1,2,3])
      
l2
      
[1, 1, 1, 2, 1, 2, 3]
l2.pop(0)
      
1
l2
      
[1, 1, 2, 1, 2, 3]
l2.remove(2)
      
l2
      
[1, 1, 1, 2, 3]
l2.reverse()
      
l2
      
[3, 2, 1, 1, 1]
l2.sort()
      
l2
      
[1, 1, 1, 2, 3]
l_1 = l2.copy()
      
l_1
      
[1, 1, 1, 2, 3]

remove(): to remove specified element from the list, if element is not 
present it gives error

l.clear():removes all elements from the list and list becomes empty
del : you can delete your list
del l
List does not exist


#We can use clear() method to delete all elements in the list, we can use del 
#list_name to delete the list
#Ordering Element of list
#reverse(): This method reverses the elements of the list. This method does 
#not return anything, it updates the existing list. This is list specific method. 
prime_numbers = [2, 3, 5, 7]
prime_numbers.reverse()
print("Reversed List :",prime_numbers)

#sort():
l = [12, 45, 6, 7,43, 3, 134, 6, 8, 768]

l.sort()

print(l)

l = ["Abc", "B", "Zebra", "R", "XYS"]

l.sort()

print(l)

l = [12, 45, 6, 7, 43, 12, 8, 7, 6, 6, 3]

l.sort(reverse = True)

print(l)

#sorted()
l = [12, 45, 6, 7, 43, 3, 134, 6, 8, 768]

sorted(l)

print(l)

#reversed: It returns reversed object iterator, not recommended to use
l = [12, 45, 6, 7, 43, 3, 134, 6, 8, 768]

reverse_object = reversed (l)

for r in reverse_object:

    print(r)

#Aliasing and Cloning of list objects:takes list backup

l = [12, 45, 6, 7, 43, 3, 134, 6, 8, 768]

l1 = l

print(id(l))

print(id(l1))

l.append(101)

print(l)

print(l1)

l = [12, 45, 6, 7, 43, 3, 134, 6, 8, 768]

l1 = l.copy()

print(l, l1)

print(id(l), id(l1))

l.append(441)

print(l, l1)

print(id(l), id(l1))

#slice operator
print(l)

l2 = l[:]

print(l2)

l.append(1111)

print(l)

print(l2)

print(id(l))

print(id(l2))

l = [1, 2, 3, [4, 5]]

l2 = l

l2 = l.copy()

print(l2)

l[3][0] = 199

print(l)

print(l2)

print(id(l))

print(id(l2))

print(id(l[3]))

print(id(l2[3]))

#Deep cloning (copying) and shallow cloning
#Shallow copy is not complete copy, we will face issues as we face in 
#aliasing (nested objects have same references)In order to make these copy, we use copy module.
# nested objects in aliasing problem
import copy

li1 = [1, 2, [3, 5], 4]

li2 = copy.copy(li1)

print(li1)

print(li2)

li1.append(999)

print(li1)

print(li2)

li1[2].append(333)

print(li1)

print(li2)

#Deep copy

print(li1)

li3 = copy.deepcopy(li1)

print(li3)

li1[2] .append(222)

print(li1)

print(li3)



#tuple: are immutable as same as list,object remain same throughout the life of application
t = (10,20,30,40)#() optional t= 10,20,30,40

for i in t:
    
    print(i*2)

t = 2

print(type(t))

t = (2,)

print(type(t))

t = ()

print(t)

t = (1, 2, 3)#(1, 2, 3)

t = (10,)

print(t)

t = 44,

print(t)

l = [11, 22, 33]

t = tuple(l)#takes sequences as input,accesses using index,positive and negative index and slice operator

print(l)

#As tuples are immutable, there are no any methods available those manipulate tuple elements.

#methods:len(),count(),index(),sorted(),min(),max()

t = tuple([1, 24, 4, 5, 6, 7, 45, 2, 36, 4, 8, 9, 7, 4, 3, 23, 7])

print(t)

print(len(t))

print(t.count(7))

print(t.index(24))

t_sorted = sorted(t)#Sorted function returns new list, it does not change original tuple.

print(t_sorted)

print(min(t))

print(max(t))

#1)Packing and 2)unpacking of tuple
#1
a = 10

b = 20

c = 30

d = 40

t = a, b, c, d

print(t)
#2)Unpacking:LHS should be equal to number of values in given tuple
q, x, y, z = t

print(q)

print(x)

print(y, z)

#Dictionary:data in key-value pair,duplicate keys are not allowed if true last added key value considered, previously added key will get ignored
#Heterogeneous objects are used for both keys and values.
# Mutable, dynamically we can change. Indexing and slicing is not applicable.
#creation of dictionary
d = {}

print(d)

d[100] = "Tony"

print(d)

print(d[100])#print(d[102]) Accesssing data:leads to key error:102

#Add data to dictionary: d[key] = value

d[102] = "Odkar"

print(d)

#print(d.clear())#delete whole dictionary : del d

for key,value in d.items():

    print(key,value)

print(d.clear())

print(d)

del d #completely removes dictionary

#Important functions/methods

d = dict()

print(d)

d = dict([(100,"a"), (200,"b"), (300,"c"), (400,"d"), (500,"e")])

print(d)#We can take list of lists ,set, tuples also.

d = dict([[1,2], [3,4], [5,6], [7,8]])#using list of list

print(d)

d = dict([(1,2), (3,4), (5,6), (7,8)])#using list of tuples

print(d)

d = dict(((1,2), (3,4), (5,6), (7,8)))#using tuple of tuples

print(d)

#d = dict({{1,2}, {3,4}, {5,6}, {7,8}})#using set of sets

print(d)Traceback (most recent call last):
  File "D:\pythoncodes\nonpre.py", line 392, in <module>
    d = dict({{1,2}, {3,4}, {5,6}, {7,8}})#using set of sets
TypeError: unhashable type: 'set


d = dict([{1,2}, {3,4}, {5,6}, {7,8}])#using list of sets

print(len(d))

print(d.get(8))#if key is not present then return default value instead None.


print(d.get(100,90))

#print(12):keyError:12

#Functions or methods on dictionary
d = {1:34, 2:45, 3:56, 4:78, 5:90, 6:76, 7:87, 8:56, 9:55}

print(d)

print(d.pop(5))

print(d)

print(d.pop(100,88))

print(d)

print(d.popitem())

print(d)

print(d.keys())

print(d.values())

print(d.items())

for key,value in d.items():
    print("Key is: {} and value is :{}".format(key,value))

d1 = d.copy()

print(d1)

print(d.setdefault(2,90))

print(d.setdefault(100,90))

print(d)

d2 = {111:1,222:2}

d.update(d2)

print(d)

dict_val_sum = sum(d.values())

print(dict_val_sum)

print(d)

print(sorted(d))#displays only keys

#Set:don't support indexing and slicing,dynamic,iterable,insertion order is not preserved,Duplicate data elements are not allowed
s = set()

print(s)

s = {1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 4, 5, 6, 7, 9, 5, 4, 3, 8}

print(s)

s = set([1, 2, 3, 4, 5,9, 6, 74, 3, 2, 3, 34, 19, 5, 6, 4])

print(s)

#s = set(sequence) eg.lis t, tuple,string,dictionary

d = {1:55, 2:77, 3:78, 4:88, 5:99, 6:66}

s = set(d)

print(s)

#Set functons/methods
#adding element to set :add(): takes only one arguement
s = {1, 2, 3, 4, 5, 6, 7, 8, 9}

s.add(111)

print(s)

#update(): takes multiple sequences,it does not take single element. update always expecting iterable
l = [1, 2, 3]

t = [111, 222, 333]

s = {888, 999, 777}

s1 = set()

s1.update(l, t, s)

print(s1)

#copy function:used to create copy of set

s = {1, 2, 3, 4, 5, 6, 7}

s1 = s.copy()

print(s1)

print(s)

#pop():To remove and return some random element from the set
#pop() from empty set gives key errror
#remove elements
s.pop()#by default removes  1st index elemnet of the sequence

print(s)

#remove(): To remove specified element, if it is not present then it gives key error
s.remove(7)

print(s)

#s.remove(100)

#print(s) keyerror

#discard():To remove specified element,if specified element is not present it won't give error
print(s)

s.discard(100)

print(s)

s.discard(4)

print(s)

#clear(): To remove all element,its output is empty set
s.clear()

print(s)

del s

#Set concepts:
#union():behaves same as update() function
#Syntax: set3 = set1.union(set2) or s1|s2
s = {1, 2, 3}

s1 = {4, 5, 6}

s.union(s1)

print(s)

print(s1)

#insertion():only contains the items that ae preset in both sets
s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15}

s2 = {11, 12, 1, 2, 3, 13, 14, 8, 9, 15, 16,17}

print(s1.intersection(s2))

print(s1&s2)

#intersection_update():This method will keep only the items that are present in both sets
#Syntax: x.intersection_update(y)
print(s1)

print(s2)

s1.intersection_update(s2)#if number of elelments of s1>s2 only similsr values are displayed

print(s1)#if number of elements of s1<s2 similar  values of s1 and s2 displayead for s1 
#and for s2 intersected values and ramaining values of sets also displayed

print(s2)

#difference function:Syntax:x.difference(y) or x-y
s1 = {1, 2, 3, 4, 5, 6, 7, 9, 8, 11, 43, 67}

s2  = {12, 13, 1, 3, 4, 5, 21, 78, 54}

print(s1)

print(s2)

print(s1.difference(s2))

print(s1-s2)

print(s2-s1)
"""
#symmetric_difference:returns a set except the elements that are present in both sets
#Syntax:x.symmetric_difference(y) or x^y
s1 = {1, 2, 3, 4, 5, 6, 7, 9, 8, 11, 43, 67}

s2  = {12, 13, 1, 3, 4, 5, 21, 78, 54}

print(s1.symmetric_difference(s2))

print(s1)

print(s2)


















































