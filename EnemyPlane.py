# -*- coding:utf-8 -*-
import pygame
import random
from BasePlane import BasePlane
from EnemyBullet import EnemyBullet


class EnemyPlane(BasePlane):
    def __init__(self, screen_temp):
        BasePlane.__init__(self, screen_temp, 0, 0, "./feiji/enemy0.png")
        self.direction = "right"  # 敌机初始飞行方向
        self.create_images()  # 调用这个方法向bomb_list中添加图片
        self.planeType = 1

    def move(self):

        if self.direction == "right":
            self.x += 5
        elif self.direction == "left":
            self.x -= 5

        if self. x > 480 - 50:
            self.direction = "left"
        elif self. x < 0:
            self.direction = "right"

    def fire(self):
        random_num = random.randint(1, 50)
        if random_num == 8 or random_num == 20:
            self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))

    # 爆炸时轮换图片
    def create_images(self):
        self.bomb_list.append(pygame.image.load("./feiji/enemy0_down1.png"))
        self.bomb_list.append(pygame.image.load("./feiji/enemy0_down2.png"))
        self.bomb_list.append(pygame.image.load("./feiji/enemy0_down3.png"))
        self.bomb_list.append(pygame.image.load("./feiji/enemy0_down4.png"))
