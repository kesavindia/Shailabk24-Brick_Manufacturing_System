impopy functools
#THIS is for using reduce function
#map(function,iterable) -2 parameters
#filter(function,iterable) -function should return true or false. if true,
# the item will be added in the list else omitted.
#reduce(function,iterable)-performs function on first two elements and repeats it
# until one value remains on the iterable.
# iterables can be list,tuple,set,dictionary
# items = [(3456,"shoe",780),(3455,"shoe1",450),(3452,"shoe2",75)]
# inr_usd = lambda item:(item[0],item[1],item[2]/80)
# inr_usd = lambda item:(item[0],item[1],"{:.2f}".format(item[2]/80))
# items_usd = map(inr_usd,items)
# items_usd1 = list(map(inr_usd,items))
# print(items_usd1)
# items_usd1.sopy( key = lambda item:item[0], reverse=True)
# print(items_usd1)
# def sQ_num(num):
#     return num**2
# val =(1,2,3,4,3)
# sq_m = map(sQ_num,val)
# print(set(sq_m))
# students =  [("Maths","Mala",780),("English","priya",450),("Science","Vinmayi",900)]
# more_than_900 = filter(lambda x:x[2]<800,students)
# second_V = filter(lambda x:x[1][0]=='V',students)
# print(list(second_V))
# print(list(more_than_900))
# val = [2,4,5,6,7]
# sum = functools.reduce(lambda x,y:x+y,val)
# print((sum))
# char = ("p","y","t","h","o","n")
# join = functools.reduce(lambda x,y:x+y,char)
# print(join)

# students = [("Maths","Mala",780),("English","priya",450),("Science","Vinmayi",900)]
# mappes = lambda student:(student[1],round(student[2]*100/1000))
# result_list = map(mappes,students)
# print(list(result_list))
#
# numbers = [23,56,78,99,44]
# # isEven = lambda x:"even" if x%2 == 0 else "odd"
# isEven = [("even" if number%2==0 else "odd") for number in numbers]
# # result = map(isEven,numbers)
# print(isEven)
# temp = [100,110,50,150,200]
# # temp_in_farenheit = [(num*(9/5)+32) for num in temp]
# temp_in_farenheit = lambda x:((x*(9/5)+32))
# result = map(temp_in_farenheit,temp)
# print(list(result))

# students = [("Maths","Mala",780),("English","priya",450),("Science","Vinmayi",900)]
# filtered = lambda x : 800 > x[2] > 500
# result = filter(filtered,students)
# print(list(result))


