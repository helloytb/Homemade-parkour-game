import pygame
import time
pygame.init()

screen = pygame.display.set_mode((1980,1080))
screen.fill((0,206,250))
pygame.display.update()
your_palyer = pygame.image.load('image/your_palyer.png')

zhangenxi_1 = pygame.image.load('palyer/zhangenxi_1.jpg')  # 1
zhangenxi_2 = pygame.image.load('palyer/zhangenxi_2.jpg')  # 2
nieyuxin_1 = pygame.image.load('palyer/nieyuxin_1.jpg')    # 3
nieyuxin_2 = pygame.image.load('palyer/nieyuxin_2.jpg')    # 4
yangshirui = pygame.image.load('palyer/yangshirui.jpg')    # 5
yangzicheng = pygame.image.load('palyer/yangzicheng.jpg')  # 6
weishao = pygame.image.load('palyer/weishao.jpg')          # 7
liyutong = pygame.image.load('palyer/liyutong.jpg')        # 8
sunquankun = pygame.image.load('palyer/sunquankun.png')    # 9
yushengyun = pygame.image.load('palyer/yushengyun.jpg')    # 10
# 修改图像分辨率
zhangenxi_1 = pygame.transform.scale(zhangenxi_1,(400,500))
zhangenxi_2 = pygame.transform.scale(zhangenxi_2,(400,500))
nieyuxin_1 = pygame.transform.scale(nieyuxin_1,(400,500))
nieyuxin_2 = pygame.transform.scale(nieyuxin_2,(400,500))
yangshirui = pygame.transform.scale(yangshirui,(400,500))
yangzicheng = pygame.transform.scale(yangzicheng,(400,500))
weishao  = pygame.transform.scale(weishao,(400,500))
liyutong = pygame.transform.scale(liyutong,(400,500))
sunquankun = pygame.transform.scale(sunquankun,(400,500))
yushengyun = pygame.transform.scale(yushengyun,(400,500))

def show_1():
    screen.blit(your_palyer,(730,80))
    screen.blit(zhangenxi_1,(760,280))
    pygame.display.update()
    time.sleep(2)
def show_2():
    screen.blit(your_palyer, (730, 80))
    screen.blit(weishao, (760, 280))
    pygame.display.update()
    time.sleep(2)
def show_3():
    screen.blit(your_palyer,(730,80))
    screen.blit(nieyuxin_1,(760,280))
    pygame.display.update()
    time.sleep(2)
def show_4():
    screen.blit(your_palyer,(730,80))
    screen.blit(yangzicheng,(760,280))
    pygame.display.update()
    time.sleep(2)
def show_5():
    screen.blit(your_palyer,(730,80))
    screen.blit(yangshirui,(760,280))
    pygame.display.update()
    time.sleep(2)
def show_6():
    screen.blit(your_palyer,(730,80))
    screen.blit(nieyuxin_2,(760,280))
    pygame.display.update()
    time.sleep(2)
def show_7():
    screen.blit(your_palyer,(730,80))
    screen.blit(liyutong,(760,280))
    pygame.display.update()
    time.sleep(2)
def show_8():
    screen.blit(your_palyer,(730,80))
    screen.blit(sunquankun,(760,280))
    pygame.display.update()
    time.sleep(2)
def show_9():
    screen.blit(your_palyer,(730,80))
    screen.blit(yushengyun,(760,280))
    pygame.display.update()
    time.sleep(2)
def show_10():
    screen.blit(your_palyer,(730,80))
    screen.blit(zhangenxi_2,(760,280))
    pygame.display.update()
    time.sleep(2)

