import pgzrun
WIDTH=470

HEIGHT=470 
web=[]
venoms=[]
spider=Actor("spiderman")
spider.pos=235,400

for i in range(5):
    venom=Actor("venom")
    venom.x = 100+70*i
    venom.y = 80
    venoms.append(venom)
def on_key_down(key):
    if key == keys.SPACE:
        we=Actor("web")
        we.x = spider.x
        we.y = spider.y-30
        web.append(we)


def update():
    if(keyboard.left):
        spider.x-=10
        if(spider.x<0):
            spider.x=0
    if(keyboard.right):
        spider.x+=10
        if(spider.x>470):
            spider.x=420

    for b in web:
        b.y-=5
def draw():
    screen.blit("newyork",(0,0))
    spider.draw()
    for i in web:
        i.draw()
    for b in venoms:
        b.draw()
    screen.draw.text("0",(0,0))


pgzrun.go()