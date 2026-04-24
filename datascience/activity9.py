import matplotlib.pyplot as pt
import numpy as np
phy=[45,76,67,54,87]
chem=[53,64,76,69,97]
bio=[65,69,76,85,59]
math=[43,58,95,85,49]
eng=[59,69,78,76,94]
exam=['E1','E2','E3','E4','E5']
x=np.arange(len(exam))#len(exam)=5--> 0 to 4
pt.bar(exam,phy,width=0.15)#0,1,2,3,4
pt.bar(x+0.15,chem,width=0.15)
pt.bar(x+0.3,bio,width=0.15)
pt.bar(x+0.45,math,width=0.15)
pt.bar(x+0.6,eng,width=0.15)
pt.grid()
pt.xlabel('names of examination')
pt.ylabel('subjectwise percentage')
pt.title('result')
pt.show()