# Udacity CS101 Unit 3'

### LISTS 

##>>> p = [1,2]
##>>> p
##[1, 2]
##>>> p.append(3)
##>>> p
##[1, 2, 3]
##>>> p = p+[4,5]
##>>> p
##[1, 2, 3, 4, 5]
##>>> len(p)
##5
##>>> 

##p= [1,2]
##q= [3,4]
##p.append(q)
##print len(p)
##>>>3
##>>> print p
##[1, 2, [3, 4]]
##>>>

### Loops on Lists

'''
while <test>:
    <block>
'''

##def printAllElements(p):
##    i = 0
##    while i < len(p):
##        print p[i]
##        i += 1
##p = [1,2,3,4]
##printAllElements(p)

### For Loops on Lists

'''
for <name> in <list>:
    <block>
'''

##def print_all_elements(p):
##    for e in p:
##        print e
##p = [1,2,3,4,5]
##print_all_elements(p)
##
##def sum_list(p):
##    tot = 0
##    for e in p:
##        tot += e
##    return tot

##def find_element(l,t):
##    '''njh answer'''
##    result = 0
##    for e in l:
##        if e != t:
##            result += 1
##        if e == t:
##            return result
##    if result == len(l):
##        return -1

##def find_element(p,t):
##    '''while loop answer'''
##    i = 0
##    while i<len(p):
##        if p[i] == t:
##            return i
##        i = i+1
##    return -1


# index method
'''<list>.index(<value>)

p = [0,1,2]
print p.index(2)
>>> 2
print p.index(3)
>>> ERROR
'''

### in
''' <value> in <list> 
>>> p
[0, 1, 2]
>>> 3 in p
False
>>> 2 in p
True
>>> 
'''
##def find_element(l,t):
##    '''index method'''
##    if t in l:
##        return l.index(t)
##    return -1
##
##print find_element([1,2,3],3)
###>>> 2
##
##print find_element(['alpha','beta'],'gamma')
###>>> -1
##
##p = [1,2,3,4,5,7]
##print "p = ", p
##print "Find Element p, 1: ", find_element(p, 1)
##print "Find Element p, 1: ", find_element(p, 6)


### Quiz

# Define a procedure, union,
# that takes as inputs two lists.
# It should modify the first input
# list to be the set union of the two
# lists. You may assume the first list
# is a set, that is, it contains no 
# repeated elements.

##def union(list1,list2):
##    '''njh ans'''
##    for e in list2:
##        if not e in list1:
##            list1.append(e)

##def union(p,q):
##    '''Udacity ans'''
##    for e in q:
##        if e not in p:
##            p.append(e)

# To test, uncomment all lines 
# below except those beginning with >>>.

##a = [1,2,3]
##b = [2,4,6]
##union(a,b)
##print a 
###>>> [1,2,3,4,6]
##print b
###>>> [2,4,6]


### pop
'''
<list>.pop() --> element
mutates the list by removing and returning its
last element'''

##a = [1,2,3]
##b = a
##x = a.pop()
##
##print a,b,x
###>>> 
###[1, 2] [1, 2] 3

##p = [1,2]
##
##p.append(3)
##p.pop()


