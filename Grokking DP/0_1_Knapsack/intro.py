"""
Given:
- array of things
- want some combination to fulfill some constraint
- choose or not choose
- the basic form is True or False
- but can store more information also
    - for example: if True, then store a value, if not then -1

- two attributes
- constraint on one attribute

Pattern 1:
- array of things
- two attributes
- constraint on one attribute

Pattern 2:
- array
- target attribute
- success, failure, 

Observation:
- divide up responsibilities between minions
- don't pass around res array
- can be implicit in the dp table

"""