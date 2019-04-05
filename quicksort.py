#!/usr/bin/env python

def quicksort(mylist):
    """ Sort a mylist
    using mylist comprehensions
    """
    if not mylist:
        return mylist

    pivot = mylist[0]

    left = [x for x in mylist[1:] if x <= pivot]
    right = [x for x in mylist[1:] if x > pivot]

    return quicksort(left) + [pivot] + quicksort(right)

def quicksort2(mylist):
    """ Alternative quicksort
    using lambda and filter
    !filter() does not return a list (but iterable), 
    thus use list()
    """
    if not mylist:
        return mylist

    pivot = mylist[0]

    lesserOrEqual = list(filter(lambda x: x <= pivot, mylist[1:]))
    greaterThan = list(filter(lambda x: x > pivot, mylist[1:]))

    return quicksort2(lesserOrEqual) + [pivot] + quicksort2(greaterThan)
    

mymylist = [5,1,9,7,6,3,2]
myemptymylist = []
print("{} -> {}".format(mymylist, quicksort(mymylist)))
print("empty: {}".format(quicksort(myemptymylist)))

print("{} -> {}".format(mymylist, quicksort2(mymylist)))
print("empty: {}".format(quicksort2(myemptymylist)))
