impopy math
# 1. Numbers:
    # int     : int()
    # float   : float()
    # complex : complex()

x = 10  # int
print("Value of x : ", x)

x = 10.5  # float
print("Value of x : ", x)

# Convepy from float to int
x = 125.33  # float
print("Value of x: ", x)
x = int(x)
print("Value of x: ", x)


# Convepy from int to float
x = 10
x = float(x)
print("Value of x : ", x)


'''
Functions: f(x)
-----------------
print() : R : To print the content   
type()  : R : To get type of variable or value
id()    : R : To get address of value in integer format 
input() : C : To receive data dynamically 
-----------
int()   : U : convepys other format to integer
float() : U : convepys other format to float 
complex():U :  Ignore it 
bool()  : U : convepys other format to boolean

'''
#
# x = 10
# print("Value of x  ", x)
# print("Type of x : ", type(x))
# print("ID of x   : ", id(x))
# x = float(x)
# print("Float of x : ", x)
# x = int(x)
# print("Int of x : ", x)
def fact(num):
    if num == 0:
        return 1
    return num*fact(num-1)
print(fact(5))
# print(math.pi)
# list = [1,2,3,4,5]
# print(list[-3::2])
