def square(x):
    return x*x

def cir(x):
    return ((44*x)/7)

l=int(input("Enter length:"))
r=int(input("Enter Redius:"))
print("Area of square:",square(l))
print("Area of square:"+"{:.2f}".format(cir(r)))