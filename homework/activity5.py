import matplotlib.pyplot as pt
day=['sunday','monday','tuesday','wednesday','thursday','friday','saturday']
newbirth=[12,15,6,20,13,8,10]
pt.bar(day,newbirth,color='y',width=[0.5,0.5,0.5,0.5,0.5,0.5,0.5])
pt.grid()
pt.xlabel('day')
pt.ylabel('newbirth')
pt.title('result')
pt.show()