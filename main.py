import pygame
from pygame.locals import *
import sys
import defs
# 导入库
pygame.init()  # 初始化 pygame
map = pygame.image.load("map.png")  # 创建地图 （载入图片）
person1 = pygame.image.load("people.png")  # 创建人物 （载入图片）
screen = pygame.display.set_mode([800, 600])  # 设置窗口为(800, 600)

# 主程序
while True:
    for event in pygame.event.get(): # 获取窗口事件
        if event.type == pygame.QUIT: # 判断事件是否关闭窗口事件
            pygame.quit()  # 退出 pygame
            sys.exit()  # 退出程序
    screen.fill((0,0,0))  # 设置背景颜色为黑
    screen.blit(map, (0, 0))  # 填入背景
    screen.blit(person1, (390, 270))  # 填入人物
    pygame.display.update()   # 刷新屏幕
