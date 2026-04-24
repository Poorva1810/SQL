import matplotlib.pyplot as pt
names=['Viya','Dwij','Kitty','Sini','Tark','Yom']
per=[68,75,97,85,79,96]
pt.bar(names,per,color=['b','r','k','c','m','g'],width=[0.1,0.2,0.3,0.4,0.5,0.6])
pt.grid()
pt.xlabel('names of student')
pt.ylabel('percentage')
pt.title('result')
pt.show()