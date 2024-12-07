import pygame
import sys
pygame.init()


a = 0
b = 396
c = 792
d = 1188
e = 1584

palyer_x = 50
palyer_y = 630
screen = pygame.display.set_mode((1980,1080))

# back_1 = pygame.image.load('beijing/1.png')
# back_1 = pygame.transform.scale(back_1,[396,1080])
# screen.blit(back_1,(a,0))
#
# back_2 = pygame.image.load('beijing/2.png')
# back_2 = pygame.transform.scale(back_2,[396,1080])
# screen.blit(back_2,(b,0))
#
# back_3 = pygame.image.load('beijing/3.png')
# back_3 = pygame.transform.scale(back_3,[396,1080])
# screen.blit(back_3,(c,0))
#
# back_4 = pygame.image.load('beijing/4.png')
# back_4= pygame.transform.scale(back_4,[396,1080])
# screen.blit(back_4,(d,0))
#
# back_5 = pygame.image.load('beijing/5.png')
# back_5= pygame.transform.scale(back_5,[396,1080])
# screen.blit(back_5,(e,0))
#

pygame.display.update()


image = pygame.image.load('图像.png')  # 加载图片
tick = pygame.time.Clock()
frameNumber = 9  # 设置帧数，示例图片有6帧
frameRect = image.get_rect()  # 获取全图的框体数据，以此计算单帧框体
frameRect.width //= frameNumber  # 获取每一帧的边框数据
fps = 60 # 设置刷新率，数字越大刷新率越高
fcclock = pygame.time.Clock()
n = 0




while True:
    back_1 = pygame.image.load('beijing/1.png')
    back_1 = pygame.transform.scale(back_1, [396, 1080])
    screen.blit(back_1, (a, 0))

    back_2 = pygame.image.load('beijing/2.png')
    back_2 = pygame.transform.scale(back_2, [396, 1080])
    screen.blit(back_2, (a+b, 0))

    back_3 = pygame.image.load('beijing/3.png')
    back_3 = pygame.transform.scale(back_3, [396, 1080])
    screen.blit(back_3, (a+c, 0))

    back_4 = pygame.image.load('beijing/4.png')
    back_4 = pygame.transform.scale(back_4, [396, 1080])
    screen.blit(back_4, (a+d, 0))

    back_5 = pygame.image.load('beijing/5.png')
    back_5 = pygame.transform.scale(back_5, [396, 1080])
    screen.blit(back_5, (a + e, 0))

    back_6 = pygame.image.load('beijing/5.png')
    back_6 = pygame.transform.scale(back_5, [396, 1080])
    screen.blit(back_6, (a+1980, 0))



    pygame.display.update()

    a -= 10

    if abs(a) >396:
        a = 0


    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:  # 键盘事件
            if event.type == 768:
                palyer_y -= 200
            print(event.type)





    if n < frameNumber:
        frameRect.x = frameRect.width * n
        n += 1
    else:
        n = 0
    screen.blit(image, (palyer_x,palyer_y ), frameRect)
    fcclock.tick(fps)
    pygame.display.flip()  # 刷新窗口

