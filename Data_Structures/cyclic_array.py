"""

1: modulus operator
print arr[next_idx % len(arr)]

2: object method
class CustomList(list):
    def __getitem__(self, index):
        return super(CustomList, self).\
        __getitem__(index % len(self))

3: numpy
import numpy as np

class CustomArray(np.ndarray):
    def __new__(cls, *args, **kwargs):
        return np.asarray(args[0]).view(cls)

    def __getitem__(self, index):
        return np.ndarray.__getitem__(self, index % len(self))

"""