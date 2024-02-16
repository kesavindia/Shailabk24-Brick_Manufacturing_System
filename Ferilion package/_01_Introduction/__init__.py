def x():
    global a
    a = 20
    def y():
        global a
        a = 30
        print("Value  ", a)
    y()
    print(a)

a = 10
x()
print("Value L ", a)