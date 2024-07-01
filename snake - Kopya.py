import turtle
import time
import random

DELAY = 0.1
SCORE = 0
HIGH_SCORE = 0

# Ekran ayarları
wn = turtle.Screen()
wn.title("Yılan Oyunu")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0) # Ekran güncellemelerini kapat

# Yılan nesnesi
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("white")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

# Yemek nesnesi
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Fonksiyonlar
def go_up():
    if snake.direction != "down":
        snake.direction = "up"

def go_down():
    if snake.direction != "up":
        snake.direction = "down"

def go_left():
    if snake.direction != "right":
        snake.direction = "left"

def go_right():
    if snake.direction != "left":
        snake.direction = "right"

def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

# Klavye bağlantıları
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Ana oyun döngüsü
while True:
    wn.update()

    # Sınırlar kontrol
    if snake.xcor()>290 or snake.xcor()<-290 or snake.ycor()>290 or snake.ycor()<-290:
        time.sleep(1)
        snake.goto(0,0)
        snake.direction = "stop"
        SCORE = 0
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

    # Yemek yediğinde
    if snake.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        SCORE += 10

        if SCORE > HIGH_SCORE:
            HIGH_SCORE = SCORE

    # Yılanın vücudu
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x, y)

    move()

    # Çarpışma kontrolü
    for segment in segments:
        if segment.distance(snake) < 20:
            time.sleep(1)
            snake.goto(0,0)
            snake.direction = "stop"
            SCORE = 0
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()

    time.sleep(DELAY)

wn.mainloop()
