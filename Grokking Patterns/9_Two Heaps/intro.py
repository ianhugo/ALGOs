"""
When: 
- given set of elements
- divide into two parts
- want smallest element in one
- want largest element in other
- esp: finding medians

- or have two values
- they can both be max heaps
- closest interval

Use:
- a min heap for bigger numbers
- a max heap for smaller numbesr

----------------------------------------------
Approaches
1. Median 1 (stream/iterate)
- min heap of biggest numbers
- max heap of smallest numbers
- with each new value, compare to top of each
- if bigger, append to min heap, vice versa
- do balancing, by comparing size, popping top


-----------------------
2. Constraint Optimization (502)
- push all into max/min heap based on one attribute, with constraint
- continuously pop, put into max/min heap sorted on another attribute
- select optimized option (the top)
- update constraints, redo


-----------------------
3. Closest Intervals (436)
- idea: want max end to be matched with a smallest max start
- push all into max heap based on ending
- push all into max heap based on starting
- pop first off end, pop off start until find greater than or equal to
- repeat


"""