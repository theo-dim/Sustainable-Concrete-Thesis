import pandas as pd
import numpy as np
for i in range (1,61):
    iterable = pd.read_csv('/Users/Theo/Google Drive/College/Senior Thesis/Materials Science/data/laham/100Meta0SlagGP_OH_'+str(i)+'-00000.csv', sep=',',names = ['r','G'])
    area1 = iterable[3000:5000]
    print area1.r[np.argmax(area1.G, axis = 0)]

final = pd.read_csv('/Users/Theo/Google Drive/College/Senior Thesis/Materials Science/data/laham/100Meta0SlagGP_OH_final-00000.csv', sep=',',names = ['r','G'])
area2 = final[3000:5000]
print area2.r[np.argmax(area2.G, axis = 0)]

longterm = pd.read_csv('/Users/Theo/Google Drive/College/Senior Thesis/Materials Science/data/laham/100Meta0SlagGP_OH_90day.csv', sep=',',names = ['r','G'])
area3 = longterm[3000:5000]
print area3.r[np.argmax(area3.G, axis = 0)]
