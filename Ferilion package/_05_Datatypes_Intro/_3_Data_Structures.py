# '''
# Data types: Numbers : int float
#             Boolean : True False
#             String  : 'H' '1' "a"
#
# char   : to store single character : = 'A'   'b'
# string : to store multiple character :
# '''
#
# '''
# int        : 1 function : int()
# float      : 1 function : float()
# bool       : 1 function : bool()
#
# Data Structures:
# -----------------
# String*     - 1 hour    : 1  str()  + 40 Functions
# List*       - 45 hour   : 1  list() + 10 Functions
# Tuple       - 15M       : 1  tuple()+ 3 Functions
# Dictionary* - 45M       : 1  dict() + 10 Functions
# Set         - 15M       : 1  set()  +  3 Functions
# '''
#
# print("----------String--------------")
# # STRING  --> Collection of characters
# x = 'Hello World'   # left  to right indexing
#     #0123456789 10
# print("Value of x: ", x, id(x), type(x))
#
# name = "Madhu"
#        #01234
# print("Name is : ", name, type(name))
#
# passw = '#@$#@$32424SDFDSFfdsfsdf'
# print("Name is : ", passw, type(passw))
#
# print("-----------CRUD Operations------------")
# x = 10    # CREATE
# print(x)  # RETRIEVE
# x = 20    # UPDATE
# del x     # DELETE
#
#
#
# # CRUD
# # 1. CREATE
#    #    1234567891011  Position
# str1 = 'Hello World'
#     #   012345678910   Indexing
#
# # 2. RETRIEVE
# print("Message : ", str1)
# print("Message : ", str1[0])    # Indexing
# print("Message : ", str1[4])    # Indexing           index pos   diff
# print("Message : ", str1[0:5])  # Slicing       str1[stapy:stop:step]
# print("Message : ", str1[2:7])  # Slicing
#
#
#
# #UPDATE
# str2 = str1 + ' Welcome'
# print("Message : ", str1)
# print("Message : ", str2)
#
#
# str1 = 'Hello'
# print("String1 : ", str1)
# str1 = 'World'
# print("String1 : ", str1)
#
#
#
# # DELETE
# del str1
#
#
# # LIST
# print("----------List--------------")
#      #   1   2   3   4   5   Position
# list1 = [13, 22, 43, 24, 55]
#      #   0    1   2   3   4  Indexing
# '''
# List<Integer> li = new ArrayList<Integer>();
# li.add(13)
# li.add(22)
# '''
# print("List1 : ", list1)
# print("List1 : ", list1[0])   # indexing
# # print("List1 : ", list1[2])
# print("List1 : ", list1[1:3])  # slicing   ds[ind:ind+1]   ds[ind:pos]
#
# print("Before update : ", list1)
# # UPDATE
# list1[2] = 44
# print("After update : ", list1)
# del list1[4]
# del list1
# print("List1 : ", list1)
#
# list1 = [1.3, 2.2, 3.6, 4.7, 5]
# print("List1 : ", list1)
#
# list1 = [True, False, True, False, True]
# print("List1 : ", list1)
#
# list1 = ['hello', 'world', 'madhu']
# print("List1 : ", list1)
#
# list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matrix concept
#        #  0  1  2    0  1  2    0  1  2
#        #    0           1         2
# print("List1 : ", list1)
# print("List1 : ", list1[1])
# print("List1 : ", list1[1][2])     # list1 of 1 of 2
#
# list1 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]



# list1 = [{1, 2, 3}, {4, 5, 6}]

# print(list1[0][1])
# Convepy the first set to a list
# list1[0] = list(list1[0])
# Access the second element of the list
# print(list1[0][1])
#Accessing elements by iterating the set
# count = 0
# for element in list1[0]:
    # if count == 0:
        # print(element)
    #     break
    # count += 1

# list1 = [{'id': 100}, {'name': 'Madhu'}]
# print(list1[1]['name'])
#
# list1 = [10, 3, 4.2, True, False, 0, None, 'Hello', [1, 2, 3]]
#      #                                       01234    0  1 2
#      #    0   1   2     3     4    5   6      7           8
#
# print("List1 : ", list1)
# print("List1 : ", list1[7][4])
# print("List1 : ", list1[8][1])
#
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# print("Adding lists : ", list1+list2)
#
# print(list1 := [1, "Hello", 20.4, True]) # Heterogeneous
#
# print("----------Tuple--------------")
# tup1 = (1, 2, 3, 4, 5)
# print("Tuple1 : ", tup1)
# tup1 = (1.3, 2.2, 3.6, 4.7, 5.4)
# print("Tuple1 : ", tup1)
# tup1 = (True, False, True, False, True)
# print("Tuple1 : ", tup1)
# tup1 = ('hello', 'world', 'madhu')
# print("Tuple1 : ", tup1)
# tup1 = (1.1, 3, 4.2, True, False, 0, None, 'Hello', [1, 2, 3])
# print("Tuple1 : ", tup1)
tup1 = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
tup2 = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
# print("Tuple1 : ", tup1)
# print("Tuple1 : ", tup1[1])
# print("Tuple1 : ", tup1[1][2])
# print("Tuple1 : ", tup1[2][1])
# # del tup1[1]
#
# # del tup1
# print("Tuple1 : ", tup1+tup2)

#
# print("----------Dictionary--------------")
#
# emp_details = [100, 'Madhu Nettem', 200000, 'Bangalore', 'ORACLE', 'M']
#
# order_details = [12345, 534324, 432, 43, 3, 'Samsung S13', 'Bangalore']
#
# # int age = 20
# # key value pair association
emp_details = {'eid': 100,
               'name': 'Madhu Nettem',
               'sal': 200000,
               'loc': 'Bangalore',
               'office': 'ORACLE',
               'gender': 'M'
               }

st_marks = {1001: 33, 1002: 56, 10003: 90}

# # key value pair association
# # dict key : # int,float,bool,string,tuple

ord_details = {'order_no': 12345,
               'ref_no': 534324,
               'price': 432,
               'tax': 43,
               'quantity': 3,
               'prod_desc': 'Samsung S13',
               'del_loc': 'Bangalore'
               }
# '''
# key = eid
# value = 100
# 'eid':100 --> Item  i.e, key:value
# '''
# print("Dictionary :", emp_details)
# print("Dictionary keys :", emp_details.keys())
# print("Dictionary keys :", list(emp_details.keys()))
# print("Dictionary values: ", emp_details.values())
# print("Dictionary values :", list(emp_details.values()))
# print("Dictionary values :", list(emp_details.items()))  # list of tuples
print("Value of eid :", emp_details['eid'])
print("Value of eid :", emp_details.get('eid'))

# list = tuple(emp_details.items())
'''The items() method of a dictionary returns a view object of key-value pairs, 
not a list. View objects are not subscriptable, which means that you cannot use indexing or slicing to access their 
elements. To fix the error, you need to convepy the view object to a list before accessing its elements'''
# print(list[0][0])

# print("-------------Set---------------")  # int,float,bool,string,tuple
# set1 = set({})
# print("Set1   : ", set1)
set1 = {1, 2, 3, 4, 5, 6, '6'}
print("Set1   : ", set1)
print('1' in set1)
for i in set1:
    print (i)
for key,val in emp_details.items():
    print(key,":",val)
# # print("Set1 : ", set1[2]) Indexing is not allowed in set and dict
# # Inside set, dict,set, list are not allowed
string = "hello"
