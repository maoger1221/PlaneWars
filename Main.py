# -*- coding:utf-8 -*-

import pygame
import time
from HeroPlane import HeroPlane
from EnemyPlane import EnemyPlane


def key_control(hero_temp):
    # 按下按键
    for event in pygame.event.get():

        # 退出
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                hero_temp.move_left()
            elif event.key == pygame.K_RIGHT:
                hero_temp.move_right()
            elif event.key == pygame.K_UP:
                hero_temp.move_up()
            elif event.key == pygame.K_DOWN:
                hero_temp.move_down()
            elif event.key == pygame.K_SPACE:
                hero_temp.fire()
            elif event.key == pygame.K_b:  # 自爆
                hero_temp.bomb()


def main():
    # 创建一个窗口
    screen = pygame.display.set_mode((480, 852), 0, 32)

    # 创建背景图片
    background = pygame.image.load("./feiji/background.png")

    # 创建我的飞机
    hero = HeroPlane(screen)

    # 创建敌机
    enemy = EnemyPlane(screen)

    while True:
        screen.blit(background, (0, 0))
        # 传入敌机的位置，用于判断子弹是否击中
        hero.display(enemy)
        enemy.display(hero)
        enemy.move()
        # 开火
        enemy.fire()
        pygame.display.update()
        key_control(hero)
        time.sleep(0.01)


if __name__ == "__main__":
    main()
