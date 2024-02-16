

import module1

print("Executing module2.py")

if __name__ == '__main__':
    print("module1.py is being imported")
    module1.my_function()
else:
    print("module1.py is running directly")
# module1.my_function()
