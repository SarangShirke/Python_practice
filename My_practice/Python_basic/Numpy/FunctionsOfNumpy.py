import numpy as np

#Properties of Numpy
range =np.arange(1,10,2)  #start-Included in Output,stop- Never included,step - telling how many numbers to skip

# print(range)

arr=np.linspace(0,1,10)  #start,stop,number of elements to be generated

# print(arr)


arr1=np.logspace(1,3,3)  #start,stop,number of elements to be generated in log scale
#logerithemic scale arry from 10^1 to 10^3 with 3 elements
#np.logspece(start,ending - powers of 10,number of elements)
#print(arr1)



arr2=np.zeros((4,3))  #3 rows and 4 columns
# print(arr2)

arr3=np.ones((3,4),type(int))   #3 Array full of 1 
#print(arr3)

arr4=np.full([2,3],5)  #2 rows and 3 columns full of 5
#print(arr4)

arr5 = np.empty([2,3]) # Uninitialized array
#print(arr5)

arr6=np.random.rand(3,4)  #this function creates random floats thay are 0 to 1 between 0 and 1
#print(arr6)     

arr7=np.random.randn(3,4)  #this function creates random floats thay are -1 to 1 between -1 and 1 floats
#print(arr7)

arr8=np.random.randint(100,1000,size=(3,4))  #this function creates random integers between 1 to 10
print(arr8)
