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
        if keys_pressed[K_s] and self.rect.y < 390:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_i] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_k] and self.rect.y < 390:
            self.rect.y += self.speed

font.init()
font = font.SysFont('Arial', 30)
bspeedx = 3
bspeedy = 3
racket_l = Player('racket.png', 5, 5, 4, 100, 20)
racket_r = Player('racket.png', 675, 5, 4, 100, 20)
ball = GameSprite('proto_ball.png', 330, 230, 5, 40, 40)
player_l = GameSprite('player_l.png', 300, 200, 0, 100, 100)
player_r = GameSprite('player_r.png', 300, 200, 0, 100, 100)

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
        ball.reset()
        ball.rect.x += bspeedx
        ball.rect.y += bspeedy
        if ball.rect.y > 460 or ball.rect.y < 5:
            bspeedy *= -1
        if sprite.collide_rect(racket_l, ball) or sprite.collide_rect(racket_r, ball):
            bspeedx *= -1
        if ball.rect.x < 0:
            win_r = font.render('Right player win!', True, (0, 0, 0))
            window.blit(win_r, (240, 300))
            player_r.reset()
        if ball.rect.x > 700:
            win_l = font.render('Left player win!', True, (0, 0, 0))
            window.blit(win_l, (250, 300))
            player_l.reset()
    display.update()
    clock.tick(FPS)
