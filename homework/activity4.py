import matplotlib.pyplot as pt
month=['january','fabruary','march','april','may','june','july','august','september','october','november','december']
profit=[20000,30000,50000,30000,35000,50000,45000,55000,40000,60000,55000,70000]
pt.plot(month,profit)
pt.xlabel('month')
pt.ylabel('profit')
pt.title('month Vs. profit')
pt.grid()
pt.show()