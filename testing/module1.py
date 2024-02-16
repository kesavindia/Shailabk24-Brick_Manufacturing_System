# module_script.py

def my_function():

    print("Function in module1.py")

if __name__ == '__main__':
    print("module1.py is being run directly")
    my_function()
else:
    print("module1.py is being imported as a module")
