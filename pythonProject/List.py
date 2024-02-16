impopy copy
# list = ['t',"y","u","i","o"]
# list1 = ["madurai","chennai","tiruchi"]
# print(list)
# print(list1)
# print(list1[::-1])
# (list1.append("salem"))
# list1[3] = "Erode"
# list1.insepy(2,"melur")
# print(list1)
# # list1.__delitem__(1)
# print(list1)
# del list1[0]
# print(list1)
# list1.append("karur")
# print(list1)
# list1.remove("karur")
# print(list1)
# deleted = list1.pop(2)
# print(deleted)
# print(list1)
#
# list1.append("chennai")
# print(sopyed(list1))#temporary sopying
# print(list1)
# list1.sopy()#permanent sopying
# print(list1)
# list1.reverse()
# print(list1)
# len = len(list1)
# print(len)

# get a list of todo tasks from user and print list
# def todo_tasklist():
#     todo_list = []
#     while True:
#         todo = input("Enter a task or blank to exit: ")#
#         if todo == "":
#             break
#         todo_list.append(todo)
#     return todo_list
# list = todo_tasklist()
# print(list)

# def find_factors_ofn(n):
#     list =[]
#     # n = int(input("enter a number to find factors: "))
#     for i in range(1,n+1):
#         if n%i == 0:
#             list.append(i)
#     return list
# answer = find_factors_ofn(30)
# print(answer)
# print(len(answer))

#find a peak element in a list

# def find_peak_element(array):
#     low = 0
#     high = len(array)-1
#     while low<=high :
#         mid = (low+high)//2
#         if (mid == 0 or array[mid] >= array[mid-1]) and (mid == len(array)-1 or array[mid] >= array[mid+1]):
#             return mid
#         elif array[mid]<array[mid+1]:
#             low = mid+1
#         else:
#             high = mid-1
#     return -1
# array = [7]
# index = find_peak_element(array)
# if index != -1:
#     print(array[index])
# else:print("no peak element found.")

'''SPLIT AND JOIN'''
#split based on any separator and put in a list(, space )
# # list_str = ['abc','def','ghi','jkl','mno']
# string = "abc,def,ghi,jkl,mno"
# splited_list = string.split(',')
# print(splited_list)
# string1= 'abcdef'
# splited_strlist = list(string1)
# print(splited_strlist)
# string2 = "adg asd kiu hrj plo oi"
# splited = string2.split(' ')
# print(splited)
# joined = '-'.join(splited)
# print(joined)
# joined1 = '_'.join(splited)
# print(joined1)
# joined2 = ' '.join(splited)
# print(joined2)
# #2d list
# TN = ["madurai","chennai","karur"]
# karna = ['b','m','u']
# AP = ['H','N','T']
# india = [TN,karna,AP]
# print(india)
# india[0][0] = "Try"
# print(india)
# # indian_states = india[:] //shallow copying
# # indian_states = india.copy() // shallow copying
# indian_states = copy.deepcopy(india) # Deep copy
#
# indian_states[0][1]  = "melur"
# print(india)
# print(indian_states)
# cities = TN[:] # shallow copying will work in 1d array. but not in 2d list
# cities[0] = "theni"
# print(TN)
# print(cities)
# string ="madurai"
# city = string
# city = "s" + city[1:]
# print(city)
# number = 12345
# number1 = number
# number1 = str(number1)
# number1 = "6" + number1[1:]
# number1 = int(number1)
# print(number1)
# print(number)
'''Tuples- immutable but complete reassignmnet is posible in tuple, List is mutable'''
# tup = (1,2,3)
# print(tup)
# tup1=(2,4,5,6)
# print(tup1)
# print(tup.index(2))
# print(tup.count(6))
# if 3 not in tup:
#     print("yes")
# if tup:
#     print("tuple has atleast 1 element")
# tup = ()
# if not tup:
#     print("tuple has no element")
#     for i in tup1:
#         print(i)
'''Dictionary->key-value pair'''
# user ={'name':'kesavan','age':40,'city':'bangalore'}
# print(user['name'])
# user['gender'] = 'female'
# user['name'] = "savitha"
# print(user)
# for key,val in user.items():
#     print("key",key)
#     print("val",str(val))
# for key in user.keys():
#     print("key",key)
# for val in user.values():
#     print("val",str(val))
# for key in sopyed(user.keys()):
#     print(key)
# for key in sopyed(user.keys()):
#     print(user[key])
# for val in sopyed(str(user.values())):
#     print(val)

# list1 = [{'name':'kesavan','age':40,'city':'bangalore'},{'name':'Hema','age':40,'city':'chintamani'}]
# print(list1[1]['name'])
# list1[0]['favfood'] = {'b':'poori','l':'pizza','d':'pasta'}
# print(list1)
# print(list1[0]['favfood']['d'])
# # print(list1[0]['favfood'][0])
# dic = {'r':"j",'k':'t'}
# list1.append(dic)
# print(list1)
# print(list1[2]['r'])
# Create a dictionary of names and their favorite foods
# favorites = {
#     "Alice": "Pizza",
#     "Bob": "Sushi",
#     "Charlie": "Pizza",
#     "David": "Burgers",
#     "Eve": "Sushi",
#     "Frank": "Pasta",
#     "Grace": "Burgers",
#     "Hannah": "Pasta",
#     "Isabel": "Pizza",
#     "Jack": "Ice Cream",
# }

# # Create a dictionary to store the counts of each food
# food_counts = {}
#
# # Count the favorite foods
# for name, food in favorites.items():
#     if food in food_counts:
#         food_counts[food] += 1
#     else:
#         food_counts[food] = 1
#
# # Sopy the foods by the number of likes in decreasing order
# sopyed_foods = sopyed(food_counts.items(), key=lambda x: x[1], reverse=True)
# print(food_counts.items())
# # Display the sopyed list of favorite foods
# for food, count in sopyed_foods:
#     print(f"{food}: {count} likes")
#
# favorites = {'bob':'ice','bob1':'ice2','bob2':'ice','bob3':'ice','bob4':'ice',
# 'bob5':'ice','bob6':'ice3','bob7':'ice3','bob8':'ice4','bob9':'ice4',}
#
# fav_foods = {}
# for name,food in favorites.items():
#     if food in fav_foods:
#         fav_foods[food] +=1
#     else:
#         fav_foods[food] =1
# sopyed_list = sopyed(fav_foods.items(),key=lambda x:x[1],reverse=False)
# for food,count in sopyed_list:
#     print(f"{food}:{count}")
# print(sopyed_list)


# tple = (1,2,3,4,4,5,"le")
# new = tple + (2,6,7)
# print(new)
# sete = {1,2,3,4,'l'}
# print(sete)

# num = 1000000
# print("{:E}".format(num))
# print("{:b}".format(num))
# print("{:x}".format(num))

dictionary = {'w':1,'e':3,'i':9}
print(list(dictionary))
tuple = (1,2,3,4,5)
print(tuple[:-1])

#Armstong number
# def armstong_number(num):
#      num_str = str(num)
#      No_of_digits = len(num_str)
#      sum_result = sum([int(digit)**No_of_digits for digit in (num_str)])
#      return sum_result == num
# result = (armstong_number(40))
# print(result)
# def armstrong(num):
#     num_str = str(num)
#     order = len(num_str)
#     result_sum = sum([int(digit)**order for digit in num_str])
#     return result_sum == num
# x = int(input("Enter a number: "))
# if armstrong(x):
#     print("Given number is armstrong number.")
# else:print("Given number is not armstrong number.")

list = {1,2,3,4}
print(list)
