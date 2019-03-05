# compute the are of a triangle
def triangle_area(base, height):
  area = (1/2)*base*height
  return area

triangle_area(4,8)

# convert F to C
def F2C(f):
  c = (5/9)*(f-32)
  return c
  
f1 =F2C(32)
print(f1)

#####-----------------
# Data conversion operations

# convert an integer into string - str
# convert an hour into 24-hour format "03:00", always print

hour = 3
ones = hour % 10
tens = hour // 10
print(tens, ones, ":00")
print(str(tens) + str(ones) + ":00")

# convert a string into numbers using int and float
import math
import random

print(math.pi)

# Compute and print powerball numbers.

###################################################
# Powerball function
# Student should enter function on the next lines.

def powerball():
  print("Today’s numbers are " + str(random.randrange(1,60)) + 
  ", " + 
  str(random.randrange(1,60)) + 
  ", " + 
  str(random.randrange(1,60)) + 
  ", "+
  str(random.randrange(1,60)) +
  " and " +
  str(random.randrange(1,60)) +
  ". The Powerball number is " +
  str(random.randrange(1,36)) +
  ".")
  
	

