import pgzrun
WIDTH=470

HEIGHT=470 
score=0
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
    if key == key .SPACE:
        we=Actor("web")
        we.x = spider.x
        we.y = spider.y-30
        web.append(we)


def update():
    global score
    if(keyboard.left):
        spider.x-=10
        if(spider.x<0):
            spider.x=0
    if(keyboard.right):
        spider.x+=10
        if(spider.x>470):
            spider.x=420

    for c in web:
        c.y-=15
        for i in venoms:
                if i.colliderect(c):
                    venoms.remove(i)
                    web.remove(c)
                    score+=10
def draw():
    screen.fill("sky blue")
    spider.draw()
    for i in web:
        i.draw()
    for b in venoms:
        b.draw()
    screen.draw.text(str(score),(0,0))


pgzrun.go()