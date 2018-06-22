# -*- coding:utf-8 -*-
from Base import Base
import time


class BasePlane(Base):
    def __init__(self, screen_temp, x, y, image_name):
        Base.__init__(self, screen_temp, x, y, image_name)
        self.bullet_list = []  # 存储子弹
        self.hit = False
        self.bomb_list = []  # 用来存储爆炸时需要的图片
        self.image_num = 0  # 用来记录while True的次数,当次数达到一定值时才显示一张爆炸的图,然后清空,当这个次数再次达到时,再显示下一个爆炸效果的图片
        self.image_index = 0  # 用来记录当前要显示的爆炸效果的图片的序号
        self.planeType = 0  # 用来记录飞机类型，0为我的飞机，1为敌机

    def display(self, plane):

        # 如果被击中,就显示爆炸效果,否则显示普通的飞机效果
        if self.hit == True:
            self.screen.blit(self.bomb_list[self.image_index], (self.x, self.y))
            self.image_num += 1
            if self.image_num == 7:
                self.image_num = 0
                self.image_index += 1
            if self.image_index > 3:
                time.sleep(1)
                exit()  # 调用exit让游戏退出
                # self.image_index = 0
        else:
            self.screen.blit(self.image, (self.x, self.y))

        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():  # 判断子弹是否越界
                self.bullet_list.remove(bullet)
            if self.planeType == 1:
                if bullet.x > plane.x and bullet.x < plane.x + 100 and bullet.y > plane.y and bullet.y < plane.y + 124:
                    plane.bomb()

    def bomb(self):
        self.hit = True

    def reset(self):
        self.hit = False
