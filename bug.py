# -*- coding: utf-8 -*-
from pygame import Surface
from pygame.sprite import Sprite, collide_rect
from pygame.image import load


class Bug(Sprite):
    def __init__(self, x=10, y=10, speed=3):
        Sprite.__init__(self)
        self.image = load("images/bug.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def move(self, player, bug_army, suriken_move):
        if self.rect.y < 600:
            self.rect.y += self.speed
            self.collision(player, bug_army, suriken_move)
        else:
            self.remove(bug_army)
            player.bug_miss += 1

    def collision(self, player, bug_army, suriken_move):
        if collide_rect(self, player):
            self.remove(bug_army)
            player.bug_kill +=1
        for i in suriken_move:
            if collide_rect(self, i):
                self.remove(bug_army)
                i.remove(suriken_move)
                player.bug_kill += 1

    def remove(self, bug_army):
        self.kill()
        bug_army.remove(self)
