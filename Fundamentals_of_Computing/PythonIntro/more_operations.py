# Remainder - modular arithmetic

# systematically restrict computation to a range
# long division - divide by a number, we get a quotient plus a remainder
# quotient is integer division //
# the remainder is % 

# problem - get the ones digit of a number
num = 49
tens = num // 10
ones = num % 10

# application - 24 hour clock
hour = 20
shift = 8
print((hour + shift) % 24)

import math

def area_triangle_sss(side1,side2,side3):
  """
  Return area of a triangle, given the lengths of its three sides.
  """
  
  # Heron's formula
  semi_perim = (side1+side2+side3)/2.0
  return math.sqrt(semi_perim*
  (semi_perim-side1)*
  (semi_perim-side2)*
  (semi_perim-side3))
  
  
def do_stuff():
  print("Hello world")
  return "Is it over yet?"
  print("Goodbye cruel world!")
  
def f(x):
  return  -5*x**5 + 69*x**2 - 47
  
def future_value(present_value, annual_rate, periods_per_year, years):
  rate_per_period = annual_rate / periods_per_year
  periods = periods_per_year * years
  return present_value*(1+rate_per_period)**periods

print("$1000 at 2% compounded daily for 3 years yields $", future_value(500,.04,10,10))


def reg_ploygon_area(sn, sl):
  """
  calculate the area of a regular polygon given
  sn: number of sides
  sl: length of each side
  """
  return (sn*sl**2)/(4*math.tan(math.pi/sn))
  
reg_ploygon_area(7,3)


def project_to_distance(point_x, point_y, distance):
  dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)
  scale = distance / dist_to_origin
  return [point_x * scale, point_y * scale]

project_to_distance(2, 7, 4)
