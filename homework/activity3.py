import pandas as pd
import numpy as np
exam_data={'name':['Anastasia','Dima','Katherine','James','Emily','Michael','Matthew','Laura','kevin'],
           'score':[12,5,16.5,np.nan,18,20,19.5,np.nan,7],
           'attempts':[1,2,3,2,1,2,2,1,1],
           'qualify':['yes','yes','no','no','yes','no','yes','yes','yes']}
labels=['a','b','c','d','e','f','g','h','i']
df=pd.DataFrame(exam_data,index=labels)
print('summery of the basic information about this dataframe and its data:')
print(df.info())


