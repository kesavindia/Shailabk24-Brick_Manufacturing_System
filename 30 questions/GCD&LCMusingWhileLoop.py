'''Create a  program to find the Greatest Common Divisor (GCD) and
Least Common Multiple (LCM) of two numbers using a while loop.'''

def GCD(x,y):
    while y:
        x,y = y,x%y
    return abs(x)
def LCM(x,y):
    gcd = GCD(x,y)
    return abs(x*y)//gcd
Input1 = int(input("enter a num: "))
Input2 = int(input("enter another num: "))
gcd = GCD(Input1,Input2)
lcm = LCM(Input1,Input2)
print(f"LCM of {Input1} and {Input2} = {lcm}")
print(f"GCD of {Input1} and {Input2} = {gcd}")
