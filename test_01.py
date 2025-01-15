from ursina import *

def update():
    global speed

    player.x = player.x + time.dt * speed
    if abs(player.x)>3:
        speed= speed * -1

app=Ursina()
speed = 1
player = Entity(model='cube',color=color.red)

app.run()