# -*- coding:utf-8 -*-
from Base import Base


class BaseBullet(Base):
    def display(self):
        self.screen.blit(self.image, (self.x, self.y))
