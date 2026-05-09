from pygame import *
import random
from time import time as timer
from time import sleep
clock = time.Clock()
backx = 700
backy = 500
back = (200, 255, 255)
window = display.set_mode((backx, backy))
display.set_caption('Ping Pong')
game = True
finish = False
FPS = 60
class GameSprite(sprite.Sprite):
    def __init__(self, pimage, x, y, speed, ysize, xsize):
        super().__init__()
        self.image = transform.scale(image.load(pimage), (xsize, ysize))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 630:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_i] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_k] and self.rect.y < 630:
            self.rect.y += self.speed

racket_l = Player('racket.png', 5, 5, 4, 100, 20)
racket_r = Player('racket.png', 650, 5, 4, 100, 20)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish == False:
        window.fill(back)
        racket_l.reset()
        racket_r.reset()
        racket_l.update_l()
        racket_r.update_r()
    display.update()
    clock.tick(FPS)
