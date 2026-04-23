import matplotlib.pyplot as pt
ac=[200,400,430,450]
fridge=[400,450,300,500]
tv=[500,650,754,734]
oven=[100,139,354,384]
year=[2022,2023,2024,2025]
pt.plot(year,ac,marker='*',markersize=5,markeredgecolor='r',ls='dotted',color='b')
pt.plot(year,fridge,marker='x',markersize=10,markeredgecolor='g',ls='dashed',color='m')
pt.plot(year,tv,marker='>',markersize=5,markeredgecolor='k',ls='dotted',color='c')
pt.plot(year,oven,marker='+',markersize=5,markeredgecolor='y',ls='dotted',color='b')
pt.xlabel(' selling year')
pt.ylabel('no. of selling')
pt.title('selling per year')
pt.legend(loc=0)
pt.grid()
pt.show()