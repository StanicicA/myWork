# This program prints out a random fruit
# Andrea Stanicic

import random
fruits = ['Apple','Orange','Banana','Pear']

# random number required between 0 and lenght-1
index = random.randint (0,len(fruits)-1)
fruit = fruits [index]
print ("A random Fruit:{}".format(fruit))