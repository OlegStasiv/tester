# -*- coding: utf-8 -*-
from pygame.sprite import Sprite, collide_rect
import pyganim
from pygame.surface import Surface

SCREEN_COLOR = (80, 80, 80)

MOVE_ANIMATION = [("images/bug/bug.png", 110), ("images/bug/bug1.png", 110), ("images/bug/bug2.png", 110)]


class Bug(Sprite):
    def __init__(self, x=10, y=10, speed=3):
        Sprite.__init__(self)
        self.image = Surface((40, 40))
        self.image.fill(SCREEN_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.animation = pyganim.PygAnimation(MOVE_ANIMATION)
        self.animation.play()

    def move(self, player, bug_army, suriken_move):
        if self.rect.y < 600:
            self.rect.y += self.speed
            self.collision(player, bug_army, suriken_move)
            self.image.fill(SCREEN_COLOR)
            self.animation.blit(self.image, (0, 0))
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
