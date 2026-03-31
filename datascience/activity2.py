#series and dataframe
#series : 1d,homogeneous | dataframe :2d,hetrogeneous
import pandas as pd
import numpy as np
L=[5,1,9,3,7]
s1=pd.Series(L,['a','b','c','d','e'])
print(s1)
print(s1['b'])

ar=np.array(L)
s1=pd.Series(ar,['a','b','c','d','e'])
print(s1)

di={'cricket':19,'football':26,'swimming':41,'basketball':8}
s1=pd.Series(di)
print(s1)

L=[[3,9,1,-4,5],[30,90,10,-40,50],[13,19,11,-14,15]]
df=pd.DataFrame(L)
print(df)

print(df.info())

L=[[3,9,1,np.nan,5],[30,np.nan,10,-40,50],[13,19,11,-14,np.nan]]
df=pd.DataFrame(L)
print(df)

df=df.fillna('***')
print(df)

df=df.dropna(axis=1)#drop the records which contain nan
print(df)