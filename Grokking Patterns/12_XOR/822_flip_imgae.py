"""
GIVEN: matrix of 0, 1es
WANT: flip and invert image

Note: python floor division operator //

"""


def flip_an_invert_image(matrix):
    C = len(matrix)
    for row in matrix:
        for i in range((C+1)//2):
            #switch places
            #then XOR with 1 to invert
            #can do -i for second index
            row[i], row[C - i - 1] = row[C - i - 1] ^ 1, row[i] ^ 1
        
    return matrix