import functools
#https://caisbalderas.com/blog/iterating-with-python-lambdas/

lis = [1, 3, 5, 6, 2, ]

#sum it
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a+b, lis))

#with condition
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))

#map
#do function on each element
x = [2, 3, 4, 5, 6]
y = map(lambda v : v * 5, x)

#filter
#if satisfy then put True, if not False
aa = map(lambda v : v * 5, filter(lambda u : u % 2, x))

#list comprehension
[v * 5 for v in x if v % 2] 