from pygame import *
from random import randint

window = display.set_mode((1400,800))
display.set_caption("pingpong")
game = True
background = transform.scale(image.load("table-tennis-back-stop-table-tennis-table-34.jpg"),(1400,800))
finish = False
finish2 = False
font.init()
font = font.Font(None,160)
win = font.render("YOU WIN!",True,(0,171,0))
lose = font.render("YOU LOSE!",True,(171,0,0))

dvig_x =10
dvig_y =10

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y,size_x,size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset (self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player (GameSprite):
    def control1(self):
        kp=key.get_pressed()
        if kp[K_UP]:
            self.rect.y= self.rect.y - self.speed
        if kp[K_DOWN]:
            self.rect.y= self.rect.y + self.speed
    def control2(self):
        kp=key.get_pressed()
        if kp[K_w]:
            self.rect.y= self.rect.y - self.speed
        if kp[K_s]:
            self.rect.y= self.rect.y + self.speed





spirt = GameSprite("Без_названия-removebg-preview.png",670,400,100,100,8)
sprite1 = Player("200x200-removebg-preview.png",50,400,190,240,8)

sprite2 = Player("200x200-removebg-preview.png",1200,400,190,240,8)


while game:
    
    kr=key.get_pressed()
    if finish != True:
        window.blit(background,(0,0))
        sprite2.reset()
        spirt.reset()
        sprite1.reset()
        sprite2.control1()     
        sprite1.control2()
        spirt.rect.x = spirt.rect.x + dvig_x
        spirt.rect.y = spirt.rect.y + dvig_y
        if spirt.rect.y >= 760:
            spirt.rect.x = spirt.rect.x - dvig_x
            spirt.rect.y = spirt.rect.y * -1
        time.delay(1)
        display.update()

    for e in event.get():
        if e.type==QUIT:
            game = False

            

        


