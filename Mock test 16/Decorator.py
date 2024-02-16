# Decorator function
def filter_odd(func):
    def wrapper(*args, **kwargs):
        for _ in range(1):
            func(*args)
    return wrapper


# Applying the decorator using the @ syntax
@filter_odd
def filter(list1):
    list2 = []
    for i in list1:
        if i % 2 == 0:
            list2.append(i)
    return list2

resulT_list = filter([1,2,3,4,5])
print(resulT_list)

