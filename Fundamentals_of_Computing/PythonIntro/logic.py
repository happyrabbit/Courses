a = True
b = False

print(not a)
print(a and b)

# Comparison operators

a = 7 > 3 
print(a)

def greet(friend, money):
  if friend and (money > 20):
    print("Hi!")
    money = money - 20
  elif friend:
    print("Hello")
  else:
    print("Ha ha")
    money = money + 10
  return money
  
money = 15

money = greet(True, money)

money = greet(False, money)

money = greet(True, money)

# Return True if year is a leap year, false otherwise
def is_leap_year(year):
  if (year % 400) == 0:
    return True
  elif (year % 100) == 0:
    return False
  elif (year % 4) == 0:
    return True
  else:
    return False


year = 2100
leap_year = is_leap_year(year)

if leap_year:
  print(year, "is a leap year")
else:
  print(year, "is not a leap year")
