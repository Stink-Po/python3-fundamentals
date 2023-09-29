## what is shallow Copy and Deep Copy

some useful information about copy method and when we must use deepcopy
when we use copy method we use shallow copy every item in new sequence pointing to
the same address in memory that mother sequence point too and if one of these 
items are mutable and if we change that item in one of this mother sequence or copy sequence 
other one is also change and in these situations we must use deepcopy from copy builtin python library

#### Hints :
**if we make a copy from tuple copy and orginal tuple both point to the same memory address**
>
> - a = (1,2,3)
> - b = a.copy()
> - a is b
> - > True
>
**Using deepcopy is costly and we cant use them everytime in our code**

**Swapping values of a and b in python with the help of the unpacking in python**
>
> - a = 10
> - b = 20
> - a, b = b, a
> - LHS is a tuple LHS is  (20, 10)
> 