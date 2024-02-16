#walrus operator (:=) To simplify the number of lines of codes

print(name :="kesavan")
# num_list = []
# print("enter a list of numbers or z to exit")
# while True:
#      inp = input()
#      if inp == 'z' :
#          break
#      num_list.append(int(inp))
#
# print(num_list)
num_list = list()
print("enter a list of numbers or z to exit")
while (inp := input()) != 'z':
    num_list.append(int(inp))
print(num_list)


