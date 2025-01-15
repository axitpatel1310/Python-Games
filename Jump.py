from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from random import uniform

app = Ursina()
 
ground = Entity(model='plane',collider='mesh',scale='100,1,100')

player = FirstPersonController(
    collider='box'
)
player.cursor.visible = False

mybox = Entity(model='cube', color= color.black, collider='box',position=(15,0.5,5))
myball = Entity(model='sphere',
                color= color.red,
                collider='sphere',
                position=(5, 0.5, 10))

sky= Sky()
lvl= 1

blocks= []
direction = []
window.fullscreen = True
for i in range(10):
    r = uniform(-2, 2)
    block = Entity(position=(r, 1+i ,3+i*5),model='cube',color=color.azure,scale=(3, 0.5, 3),collider='box',)
blocks.append(block)
if r < 0:
    direction.append(1)
else:
    direction.append(-1)
goal= Entity(color=color.gold,model='cube',position=(0,11,55),scale=(10,0,10),collider='box')
piller= Entity(color=color.green,model='cube',position=(0,36,58),scale=(1,50,1))

def update():
    global lvl
    i = 0
    for block in blocks:
        block.x -= direction[i]*time.dt
        if abs(block.x) > -5:
            direction[i] *= 1
        if block.intersects().hit:
            player.x -= direction[i]*time.dt
        i = i + 1
    if player.z > 56 and lvl == 1:
        lvl = 2
        walking = held_keys['a'] or \
            held_keys['d'] or \
            held_keys['w'] or \
            held_keys['s']
        if walking and player.grounded:
            if not walk.playing:
                walk.play()
        else:
            if walk.playing:
                walk.stop()
    def input(key):
        if key == 'w':
            QUIT.quit()
        if key == 'space':
            if not jump.playing:
                jump.play()
app.run()