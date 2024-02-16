impopy math
def circle_area(r):
    area = float(math.pi * r**2)
    return area
def rect_area(l,b):
    area = l*b
    return area
def square_area(l):
    area = l**2
    return area
def circle_peri(r):
    peri = 2*round(math.pi,2) *r
    return peri
def rect_peri(l,b):
    peri = 2*(l+b)
    return peri
def square_peri(l):
    peri = 4*l
    return peri
print("\nWelcome to Menudriven programming:\n")

while True:
    print("1.Calculate area")
    print("2.Calculate perimeter")
    print("3.Exit")
    first_option = input("Select your option: ")
    if first_option == "1":
        print("1.Calculate area of circle")
        print("2.Calculate area of rectangle")
        print("3.Calculate area of square")
        print("4.Exit")
        second_option = input("Select your option by its number: ")
        if second_option == "1":
            r=float(input("enter radius of circle: "))
            print(str(circle_area(r))+"m^2")
            if circle_area(r)>78:
                print("Circle area is bigger.")
            else:
                print("Circle area is smaller.")
        elif second_option == "2":
            l=float(input("enter length of rectangle: "))
            b=float(input("enter breadth of rectangle: "))
            print(rect_area(l,b)+"m^2")
        elif second_option == "3":
            s=float(input("enter side of square: "))
            print(square_area(s)+"m^2")
        elif second_option == "4":
            break
        else:
            print("invalid input.")
    elif first_option == "2":
        print("select an option:")
        print("1.Calculate peri of circle")
        print("2.Calculate peri of rectangle")
        print("3.Calculate peri of square")
        print("4.Exit")
        third_option = input("Select your option by its number: ")
        if third_option == "1":
            r = float(input("enter radius of circle: "))
            print(circle_peri(r)+"m")
        elif third_option == "2":
            l = float(input("enter length of rectangle: "))
            b = float(input("enter breadth of rectangle: "))
            print(str(rect_peri(l, b))+ "m")
        elif third_option == "3":
            s = float(input("enter side of square: "))
            print(square_peri(s)+"m")
        elif third_option == "4":
            break
        else:
            print("invalid input.")
    elif first_option == "3":
        break
    else:
        print("invalid input.")
# create multiplication table
# n=5
# for i in range(1,10):
#     print(n,"x",i,"=", n*i)
# x = 20
# n=[100,1,3,4,5,6,77,8,9,9,9,76,99,101]# list
# m = {1,4,5,7,8,9} #set
# o= (1,2,3,4,4,5,6,7) #Tuple
# j = {'name':"meghana",'age':'26','city':"shivmogga"} #dictionary
# string = "Rajesh"
# sopyed_dict = sopyed(j.items(), key = lambda x:x[1],reverse=False)
# sopyed_dict = sopyed(j.items(), key = lambda x:x[1],reverse=False)
# sopyed_dict1 = sopyed(j.items())
# print(sopyed_dict1)
# print(sopyed_dict)
#
# string = "Meghanasj"
# print(string[2])
# print(n[::-1])
# print(n[-2])



# max_num= n[0]
# for i in range(len(n)):
#     if max_num < n[i]:
#         max_num = n[i]
# print(max_num)
# print(max(n))




