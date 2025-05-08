# Name- ANURADHA KUMARI
# Reg no.- 23117107002
# Biomedical and Robotics Engineering

def area_and_perimeter(breadth, height, a,b,c):
  
  area = 1/2*breadth*height
  perimeter = a+b+c
  return area, perimeter

breadth= 8
height = 10
a= 5
b= 7
c= 12

area_of_triangle, perimeter_of_triangle= area_and_perimeter(breadth, height, a,b,c)

print("Area:",area_of_triangle)
print("Perimeter:",perimeter_of_triangle)