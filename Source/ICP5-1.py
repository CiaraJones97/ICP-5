import matplotlib.pyplot as plt
import numpy as np

#inputing data as an array
arr1 = np.array([[0,1],[1,3],[2,2],[3,5],[4,7],[5,8],[6,8],[7,9],[8,10],[9,12]])

# List for the x and y values
x_values = []
y_values = []

# to check if the data input is correct
print (arr1)
x_sum = 0
for i in  arr1 [:,0]:
    x_sum += i
    x_values.append(i)
x_mean = x_sum / len(arr1)
y_sum = 0
for i in arr1 [:,1]:
    y_sum += i
    y_values.append(i)
y_mean = y_sum/len(arr1)

lis2 = []
lis3 = []

# Add the number minues the mean for the x and y values
for i in range (len(arr1)):

    lis2.append( arr1[i][0]- x_mean)
    lis3.append( arr1[i][1]- y_mean)

# Change the list into arrays
arr2 = np.array(lis2)
arr3 = np.array(lis3)

# Find (x - x_mean) * (y - y_mean)
arr4 = arr2 * arr3

# Find (x - x_mean) * (x- x_mean)
arr5 = arr2 * arr2

Numerator = 0
Dumnetor = 0

# Find the sum of the numerator and the denominator
for i in range (0, 10):
    Numerator += arr4[i]
    Dumnetor += arr5[i]

# Calculate B1 and B0
B1 = Numerator/Dumnetor
B0 = y_mean - B1*x_mean
print ("The value of the means are x_mean : {} and y_mean : {}".format (x_mean,y_mean))
print ( "The vale of B0 is : {} and the value of B1 is : {}".format (B0,B1))

x = np.linspace (0,15,1000)
y = B0 + B1 *x
plt.plot (x,y)
plt.scatter(x_values, y_values, color = 'yellow')
plt.show ()

