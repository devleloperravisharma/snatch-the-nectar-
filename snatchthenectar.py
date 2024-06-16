import pgzrun

import random

'----------------------------------------------------------------------------------------------------------------------------------------------------------------------'

TITLE = "Snatch The Nectar"

WIDTH = 600

HEIGHT = 500

score = 0

game_over = False
'---------------------------------------------------------------------------------------------------------------------------------------------------------------------'

flower = Actor("flower")

beebee = Actor("bee")

flower.pos = (100, 100)

beebee.pos = (20, 20)

def draw():
    screen.blit("pink_wallpaper", (0,0))
    flower.draw()
    beebee.draw()
    screen.draw.text("Score: "+str(score), color = (255, 255, 255), topleft = (10,10))

    if game_over:
        screen.fill("#ffccd8")
        screen.draw.text("Game Over!", color = "white", midtop = (WIDTH/2, HEIGHT/2-50), fontsize = 40)
        if score<10:
            screen.draw.text("You Lost HAHAHAHAAHA! Your score was: "+str(score), color = "white", midtop = (WIDTH/2, HEIGHT/2), fontsize = 30)
        else:
            screen.draw.text("You won! Good job. You get a cookie. Your score was: "+str(score), color = "white", midtop = (WIDTH/2, HEIGHT/2), fontsize = 30)

def time_up():
    global game_over
    game_over = True

def update():
    global score
    if keyboard.up:
        beebee.y -= 5
    if keyboard.down:
        beebee.y += 5
    if keyboard.left:
        beebee.x -= 5
    if keyboard.right:
        beebee.x += 5
    if beebee.colliderect(flower):
        score += 1
        movefl()


def movefl():
    flower.x = random.randint(70, WIDTH-70)
    flower.y = random.randint(70, WIDTH-70)

clock.schedule(time_up, 60.0)



pgzrun.go()