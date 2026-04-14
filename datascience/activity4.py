import matplotlib.pyplot as pt
phy=[57,58,69,76,57]
che=[63,47,87,67,65]
math=[73,48,58,69,59]
bio=[39,57,87,90,75]
eng=[59,79,98,68,70]
exam=['E1','E2','E3','E4','E5']
pt.plot(exam,phy,marker='1',markersize=7,markeredgecolor='b',ls='dotted',linewidth=3,color='r',label='phy')
pt.plot(exam,che,marker='X',markersize=3,markeredgecolor='g',ls='dashed',linewidth=3,color='b',label='che')
pt.plot(exam,math,marker='*',markersize=10,markeredgecolor='m',ls='dashdot',linewidth=3,color='g',label='math')
pt.plot(exam,bio,marker='+',markersize=5,markeredgecolor='y',ls='dotted',linewidth=3,color='k',label='bio')
pt.plot(exam,eng,marker='p',markersize=1,markeredgecolor='c',ls='dashed',linewidth=3,color='y',label='eng')
pt.xlabel('name of examination')
pt.ylabel('Marks')
pt.title('result')
pt.legend(loc=0)
pt.grid()
pt.show()