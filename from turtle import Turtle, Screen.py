from turtle import Turtle, Screen
oyna = Screen()
oyna.title('Dastur')
chiziq = Turtle()
chiziq.hideturtle()
chiziq.pensize(3)
chiziq.color('green')
chiziq.speed(0)
chiziq.up()
chiziq.goto(300,300)
chiziq.down()
chiziq.goto(300,-300)
chiziq.goto(-300,-300)
chiziq.goto(-300,300)
chiziq.goto(300,300)

shakl = Turtle()
shakl.hideturtle()
shakl.speed(1)
shakl.goto(200,-200)
shakl.goto(250,-200)
shakl.goto(250,-250)
shakl.goto(200,-250)
shakl.goto(200,-200)


aylana = Turtle()
aylana.shape('circle')
aylana.color('grey')
aylana.up()
aylana.goto(0,0)

step_x=3
step_y=2
while True :
	x, y = aylana.position()
	if x+step_x>=300 or x+step_x<= -300 :
		step_x = -step_x
	if y + step_y >=300 or y+ step_y <= -300 :
		step_y = -step_y
	aylana.goto(x+step_x, y +step_y)
	if x+step_x >= 200 and x+step_x <= 250 and y + step_y <= -200 and y + step_y >= -250 :
		break
print('Dastur tugadi')
	
