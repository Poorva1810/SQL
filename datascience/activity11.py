import matplotlib.pyplot as plt
class_A=[63,47,57,48,57,96,68,60,59,44,54,93]
class_B=[54,58,69,78,69,89,57,70,45,35,92,83]
class_C=[53,57,86,96,85,46,58,68,59,36,58,64]
plt.hist([class_A,class_B,class_C],bins=10,label=['class_A','class_B','class_C'])
plt.xlabel('exam scores')
plt.ylabel('number of students')
plt.title('distribution of exam scores across classes')
plt.legend()
plt.xticks(range(45,96,5))
plt.yticks([1,2,3,4])
plt.grid()
plt.show()