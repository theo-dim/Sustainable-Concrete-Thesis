import pandas as pd
import numpy as np
for i in range (1,61):
    iterable = pd.read_csv('/PATHTOFILE', sep=',',names = ['r','G'])
    area1 = iterable[3000:5000]
    print np.max(area1.G)

final = pd.read_csv('/PATHTOFILE', sep=',',names = ['r','G'])
area2 = final[3000:5000]
print np.max(area2.G)

longterm = pd.read_csv('/PATHTOFILE', sep=',',names = ['r','G'])
area3 = longterm[3000:5000]
print np.max(area3.G)
