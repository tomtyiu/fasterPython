#Use numpy vs range for faster execution time https://www.kdnuggets.com/speeding-up-your-python-code-with-numpy
import numpy as np
import time

import math
import time

sample = 1_000_000
list_1 = range(sample)

start_time = time.time()
result = [math.sin(x) for x in list_1]
print("Time using Python lists:", time.time() - start_time)


import numpy as np
import time

array_1 = np.arange(sample)

start_time = time.time()
result = np.sin(array_1)
print("Time using NumPy arrays:", time.time() - start_time)

#Time using Python lists: 0.08826088905334473
#Time using NumPy arrays: 0.015142440795898438
