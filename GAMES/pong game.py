import turtle #Inside_Out
wn = turtle.Screen()
wn.bgcolor("light green")
skk = turtle.Turtle()
skk.color("red")
# clock = turtle.time.Clock()
def sqrfunc(size):
	for i in range(4):
		skk.fd(size)
		skk.left(90)
		size = size + 5


sqrfunc(6)
while True:
    wn.update()

# sqrfunc(26)
# sqrfunc(46)
# sqrfunc(66)
# sqrfunc(86)
# sqrfunc(106)
# sqrfunc(126)
# sqrfunc(146)
