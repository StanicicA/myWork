#calculating Body Mass Index
#Author:Andrea Stanicic

height = int (input ('Enter your Height(cm):'))
newHight = height / 100  

print ('Your Height is {} m²'.format(newHight))

HeightM = newHight * newHight
weight = int (input ('Enter your Weight(kg)'))
BMI = weight / HeightM

print ('Your BMI is {}'.format(BMI))