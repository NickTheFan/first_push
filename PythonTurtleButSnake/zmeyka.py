# Импорт
import random
import turtle
import time

delay = 0.1
score = 0
high_score = 1
bosshp = 150
speed = 3.5
# Создаем черепашку
t = turtle.Turtle()
colorst = random.choice(['white', 'green', 'yellow'])
t.shape("arrow")
t.color(colorst)
t.speed(speed)


# Создаем босса
boss = turtle.Turtle()
boss.shape("turtle")
boss.color("red")
boss.penup()
boss.speed(1009000000)
boss.goto(300, 0)
boss.setheading(180)
boss.shapesize(stretch_wid=5, stretch_len=5, outline=0)

bosstext = turtle.Turtle()
bosstext.color("white")
bosstext.penup()
bosstext.speed(1009000000)
bosstext.goto(300, 25)



def bossdie():
    global bosshp

    if bosshp == 0:
        boss.hideturtle()
        timerr.goto(0,0)
        timerr.write(f"Вы победили!", font=("Candara", 32, "normal"))
        time.sleep(5)
        window.bye()

    elif timer <= 0 and bosshp > 0:


        timerr.goto(-200, 0)
        timerr.write(f"Вы проиграли, ведь у босса осталось {100 - bosshp} здоровья!", font=("Candara", 32, "normal"))


# Создание яблок
colors = random.choice(['yellow', 'green', 'pink'])
shapes = random.choice(['square', 'circle'])
apple = turtle.Turtle()
apple.goto(50, 50)
apple.up()
apple.shape(shapes)
apple.color(colors)

timer = 30
timerr = turtle.Turtle()
timerr.color("white")
timerr.hideturtle()
timerr.penup()
timerr.goto(250, 400)
timerr.write(f"Время : {timer}", font=("Candara", 32, "normal"))


def update_timer():
    global timer
    if timer > 0:
        timer -= 1
        timerr.clear()
        timerr.write(f"Время : {timer}", font=("Candara", 32, "normal"))
        window.ontimer(update_timer, 1000)



# Создание текста
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(-420, 400)


def tpapple(x, y):
    apple.speed(1000)
    apple.up()
    apple.hideturtle()
    apple.goto(x, y)
    apple.showturtle()


def bounce():
    global speed
    t.setheading(180)
    speed += 1.5


x = random.randint(-450, 450)
y = random.randint(-450, 450)

# Настраиваем экран
window = turtle.Screen()
window.setup(900, 900)
window.title("Туртле")
window.bgcolor("black")


# window.onkeypress(t.forward(90), key: "w")

# Функции управления

def goleft():
    t.left(90)
    check_dist()


def goright():
    t.right(90)
    check_dist()


def move():
    t.forward(3.5)
    check_dist()


def update_score():
    global score
    global high_score
    global timer
    global bosshp
    score += 1
    bosshp -= 10
    timer += 5
    pen.clear()
    pen.write(f"Score : {score} High score : {high_score}", font=("Candara", 32, "normal"))
    bosstext.clear()
    bosstext.write(f"{bosshp} hp", font=("Candara", 32, "normal"))

    if score >= high_score:
        high_score = score
        high_score += 1
    bossdie()


bossdie()
update_timer()


def clear_w():
    t.clear()


def home():
    t.goto(0, 0)


window.listen()
window.onkeypress(move, "w")
window.onkeypress(goleft, "a")
window.onkeypress(goright, "d")
window.onkeypress(clear_w, "c")
window.onkeypress(home, "h")


def check_dist():
    if t.distance(apple) < 20:
        xx = random.randint(-430, 430)
        yy = random.randint(-430, 430)
        t.up()
        t.goto(0, 0)
        t.down()
        apple.up()
        update_score()
        tpapple(xx, yy)

    if t.xcor() >= 450 or t.xcor() <= -450 or t.ycor() >= 450 or t.ycor() <= -450:
        global score
        score = 0
        t.up()
        t.clear()
        t.goto(0, 0)
        t.down()
        pen.clear()
        pen.write(f"Score : {score} High score : {high_score}", font=("Candara", 32, "normal"))
        t.goto(0, 0)


while timer > 0:
    move()

# Связываем клавиши с действиями

window.listen()
xx = random.randint(-450, 450)
yy = random.randint(-450, 450)

check_dist()

window.mainloop()
