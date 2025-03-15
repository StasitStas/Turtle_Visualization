import turtle, math, random

GROUND_LEVEL, UNDERGROUND_LEVEL = -200, -350
VERTICAL_LEVEL = 700
PIXEL_SIZE, PIXEL_NUMBER = 25, 50
ART_X, ART_Y = -450, GROUND_LEVEL + 10
ART_ANGLE_MIN, ART_ANGLE_MAX = 9, 89
V_0 = 40
TEXT_X, TEXT_Y = -500, 150
BLOCK = False

def create_ground():
    t.hideturtle()
    t.fillcolor('#8C6F3E')
    t.begin_fill()
    t.penup()
    t.goto(-VERTICAL_LEVEL, GROUND_LEVEL)
    t.pendown()
    t.setposition(VERTICAL_LEVEL, GROUND_LEVEL)
    t.setposition(VERTICAL_LEVEL, UNDERGROUND_LEVEL)
    t.setposition(-VERTICAL_LEVEL, UNDERGROUND_LEVEL)
    t.setposition(-VERTICAL_LEVEL, GROUND_LEVEL)
    t.end_fill()

def create_artillery():
    t.penup()
    t.goto(TEXT_X, TEXT_Y)
    t.pendown()
    t.color('black', 'black')
    t.write('"Стрілка вгору" - підняти ствол\n"Стрілка вниз" - опустити ствол\n"Прогалина" - постріл')
    t.penup()
    t.goto(ART_X, ART_Y)
    t.pendown()
    t.setheading(ART_ANGLE_MIN)
    t.showturtle()

def create_pixels(number):
    t.pencolor('#8C6F3E')
    i_max = int(2 * VERTICAL_LEVEL / PIXEL_SIZE) - 1
    j_max = int((GROUND_LEVEL - UNDERGROUND_LEVEL) / PIXEL_SIZE) - 1
    color_list = ['#D9BB83', '#FACDA1', '#B49A83']
    for _ in range(number):
        i_rnd = random.randint(0, i_max)
        j_rnd = random.randint(0, j_max)
        color_rnd = random.choice(color_list)
        t.fillcolor(color_rnd)
        t.begin_fill()
        x_left = -VERTICAL_LEVEL + i_rnd * PIXEL_SIZE
        x_right = -VERTICAL_LEVEL + (i_rnd + 1) * PIXEL_SIZE
        y_up = GROUND_LEVEL - j_rnd * PIXEL_SIZE
        y_down = GROUND_LEVEL - (j_rnd + 1) * PIXEL_SIZE
        t.penup()
        t.goto(x_left, y_up)
        t.pendown()
        t.setposition(x_right, y_up)
        t.setposition(x_right, y_down)
        t.setposition(x_left, y_down)
        t.setposition(x_left, y_up)
        t.end_fill()

def move_up():
    angle = t.heading()
    angle += 1
    if angle > ART_ANGLE_MAX:
        angle = ART_ANGLE_MAX
    t.setheading(angle)

def move_down():
    angle = t.heading()
    angle -= 1
    if angle < ART_ANGLE_MIN:
        angle = ART_ANGLE_MIN
    t.setheading(angle)

def fire():
    global BLOCK
    if BLOCK is True:
        return
    else:
        BLOCK = True
    x, y = t.position()
    ax, ay = 0, -0.98
    angle = math.radians(t.heading())
    vx, vy = V_0 * math.cos(angle), V_0 * math.sin(angle)

    t_fire = turtle.Turtle(shape='circle', visible=False)
    t_fire.shapesize(0.2, 0.2)
    t_fire.color('black', 'black')
    t_fire.penup()
    t_fire.goto(x, y)
    t_fire.pendown()
    t_fire.showturtle()
    while True:
        vx += ax
        vy += ay
        x += vx
        y += vy
        t_fire.setposition(x, y)
        if y <= GROUND_LEVEL:
            BLOCK = False
            break

def main():
    global t
    s = turtle.Screen()
    s.title('Артилерія')
    s.setup(width=0.75, height=0.75)
    s.bgcolor('#729EFF')
    try:
        s.bgpic('sky.png')
    except:
        pass
    t = turtle.Turtle()
    s.delay(0)
    create_ground()
    create_pixels(PIXEL_NUMBER)
    create_artillery()
    s.delay(5)
    s.listen()
    s.onkeypress(move_up, 'Up')
    s.onkeypress(move_down, 'Down')
    s.onkeypress(fire, 'space')
    s.mainloop()

if __name__ == '__main__':
    main()