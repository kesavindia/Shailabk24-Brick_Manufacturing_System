#Data Validation
print("Check your job eligiblity.")
Height = int(input("enter your height in cm: "))
while True:
    if Height < 150:
        print("You are not eligible for the post.")
        break
    else:
        print("You are eligible for the post.")
        if 150 <= Height <= 165:
            print("But your chance of getting job is less.")
            break
        elif 166 <= Height <= 180:
            print("But your chance of getting job is more.")
            break
        else:
            print("You will surely get this job.")
            break
