#The built-in reversed function returns an iterator.
#Python’s iterators can do two things:
#Return the next item using a for loop or calling the built-in next function.
#Signal that the iterator is exhausted and that there are no more items by raising StopIteration .
#The first call to sorted(rev) consumes everything from the iterator. When we call sorted(rev) the second time, the iterator will immediately raise StopIteration and the function sorted will assume an empty iterator. The result of the first sorted(rev) is [1, 2, 3, 4]. The result of the second sorted(rev) is [] (the empty list). This is why the comparison returns False.

nums = [4,3,7,1,3,6,2]
#nums.reverse()
print(nums)

rev = reversed(nums)
print(list(rev))
print(sorted(rev) == sorted(rev))

nums2 = [4, 1, 3, 2]
print(nums2)
rev2 = reversed(nums2)
print(sorted(rev2) == sorted(rev2))
a = sorted(rev2)
print(a)
