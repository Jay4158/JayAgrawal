import math

def are(x,y,z):
    sm=x+y+z;sm/=2
    area=math.sqrt(sm*((sm-x)*(sm-y)*(sm-z)))
    return area

l = int(input("Enter 1st:").strip())
b = int(input("Enter 2nd:").strip())
h = int(input("Enter 3rd:").strip())

print("Area of Tringle:"+"{:.2f}".format(are(l,b,h)))

