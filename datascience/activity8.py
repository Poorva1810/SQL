import matplotlib.pyplot as pt
phy=[45,76,67,54,87]
chem=[53,64,76,69,97]
bio=[65,69,76,85,59]
math=[43,58,95,85,49]
eng=[59,69,78,76,94]
exam=['E1','E2','E3','E4','E5']
pt.bar(exam,phy,width=0.9)
pt.bar(exam,chem,width=0.7)
pt.bar(exam,bio,width=0.5)
pt.bar(exam,math,width=0.3)
pt.bar(exam,eng,width=0.6)
pt.grid()
pt.xlabel('names of examination')
pt.ylabel('subjectwise percentage')
pt.title('result')
pt.show()