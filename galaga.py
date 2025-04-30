import pgzrun
WIDTH=470

HEIGHT=470
ship=Actor("galaga")
ship.pos=235,400
def on_key_down(key):
    if key == keys.SPACE:
        bullet=Actor("bullet")
        bullet.x = ship.x
        bullet.y = ship.y

def update():
    if(keyboard.left):
        ship.x-=10
        if(ship.x<0):
            ship.x=0
    if(keyboard.right):
        ship.x+=10
        if(ship.x>470):
            ship.x=420
def draw():
    screen.fill("blue")
    ship.draw()
    bullet.draw()


pgzrun.go()