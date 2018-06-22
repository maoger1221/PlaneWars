# -*- coding:utf-8 -*-
from BasePlane import BasePlane
from Bullet import Bullet
import pygame


class HeroPlane(BasePlane):
    def __init__(self, screen_temp):
        BasePlane.__init__(self, screen_temp, 210, 700, "./feiji/hero1.png") # super().__init__()
        self.create_images()  # 调用这个方法向bomb_list中添加图片
        self.planeType = 0

    def move_left(self):
        self.x -= 10

    def move_right(self):
        self.x += 10

    def move_up(self):
        self.y -= 10

    def move_down(self):
        self.y += 10

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))

    # 爆炸时轮换图片
    def create_images(self):
        self.bomb_list.append(pygame.image.load("./feiji/hero_blowup_n1.png"))
        self.bomb_list.append(pygame.image.load("./feiji/hero_blowup_n2.png"))
        self.bomb_list.append(pygame.image.load("./feiji/hero_blowup_n3.png"))
        self.bomb_list.append(pygame.image.load("./feiji/hero_blowup_n4.png"))
