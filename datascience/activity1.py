import numpy as np
a= np.arange(9,dtype=np.float64)
a=a.reshape(3,3)
print('first array:')
print(a)
print('\n')

b=np.array([10,10,10])
print('second array:')
print(b)
print('\n')

print('add the two arrays:')
print(np.add(a,b))
print('\n')

print('subtract the two arrays:')
print(np.subtract(a,b))
print('\n')

print('multiply the two arrays:')
print(np.multiply(a,b))
print('\n')

print('divide the two arrays:')
print(np.divide(a,b))
print('\n')

arr=np.array([1,2,3,4])
print(arr[0])

arr=np.array([1,2,3,4,5,6,7,8])
print(arr[1:5])
print(arr.dtype)
newarr=arr.reshape(2,4)
print(newarr)

arr=np.array([1,2,3,4,5,4,4])
x=np.where(arr==4)
print(x)

data_type = [('name', 'S15'), ('class', int), ('height', float)]
students_details = [('James', 5, 48.5), ('Nail', 6, 52.5),('Paul', 5, 42.10), ('Pit', 5, 40.11)]

students = np.array(students_details, dtype=data_type)
print("Original array:")
print(students)
print("Sort by height")
print(np.sort(students, order='height'))