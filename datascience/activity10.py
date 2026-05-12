import pandas as pd
import matplotlib.pyplot as pt
males=[72,80,91,105,100,62,90,120,83]
females=[70,84,93,100,101,72,152,140,81]
pt.hist([males,females],bins=6)
pt.xticks([62,77,92,107,122,137,152])
pt.yticks([1,2,3,4])
pt.grid()
pt.show()