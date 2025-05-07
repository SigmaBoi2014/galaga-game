import pgzrun
WIDTH=470

HEIGHT=470
bull=[]
bugs=[]
ship=Actor("galaga")
ship.pos=235,400

for i in range(5):
    bug=Actor("bug")
    bug.x = 100+70*i
    bug.y = 80
    bugs.append(bug)
def on_key_down(key):
    if key == keys.SPACE:
        bullet=Actor("bullet")
        bullet.x = ship.x
        bullet.y = ship.y-30
        bull.append(bullet)


def update():
    if(keyboard.left):
        ship.x-=10
        if(ship.x<0):
            ship.x=0
    if(keyboard.right):
        ship.x+=10
        if(ship.x>470):
            ship.x=420

    for b in bull:
        b.y-=5
def draw():
    screen.fill("blue")
    ship.draw()
    for i in bull:
        i.draw()
    for b in bugs:
        b.draw()
    screen.draw.text("0",(0,0))


pgzrun.go()