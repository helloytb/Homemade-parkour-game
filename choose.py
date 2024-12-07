import pygame
from roll_back import run_game
from palyer_show import*

pygame.init()
screen = pygame.display.set_mode((1980,1080))

def choose():
    '''角色选择页面'''
    screen.fill((0,206,250))
    choosepalyer = pygame.font.SysFont('Arial',30)
    choosepalyer = choosepalyer.render('plese choose palyer',True,(255,0,0))
    screen.blit(choosepalyer,[830,50])
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
    zhangenxi_1 = pygame.transform.scale(zhangenxi_1,(200,300))
    zhangenxi_2 = pygame.transform.scale(zhangenxi_2,(200,300))
    nieyuxin_1 = pygame.transform.scale(nieyuxin_1,(200,300))
    nieyuxin_2 = pygame.transform.scale(nieyuxin_2,(200,300))
    yangshirui = pygame.transform.scale(yangshirui,(200,300))
    yangzicheng = pygame.transform.scale(yangzicheng,(200,300))
    weishao  = pygame.transform.scale(weishao,(200,300))
    liyutong = pygame.transform.scale(liyutong,(200,300))
    sunquankun = pygame.transform.scale(sunquankun,(200,300))
    yushengyun = pygame.transform.scale(yushengyun,(200,300))

    # 绘制角色
    # 第一排
    screen.blit(zhangenxi_1, [98,150])
    screen.blit(weishao, [494, 150])
    screen.blit(nieyuxin_1, [890, 150])
    screen.blit(yangzicheng, [1286, 150])
    screen.blit(yangshirui, [1682, 150])

    # 第二排
    screen.blit(nieyuxin_2, [98, 630])
    screen.blit(liyutong, [494, 630])
    screen.blit(sunquankun, [890, 630])
    screen.blit(yushengyun, [1286, 630])
    screen.blit(zhangenxi_2, [1682, 630])

    pygame.display.update()

    # 事件检测
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x , mouse_y = pygame.mouse.get_pos()
                # 角色1
                if mouse_x in range(98,298) and mouse_y in range(150,450):
                    screen.fill((0, 206, 250))
                    show_1()
                    run_game()
                # 角色2
                if mouse_x in range(494,694) and mouse_y in range(150,450):
                    screen.fill((0, 206, 250))
                    show_2()
                    run_game()
                # 角色3
                if mouse_x in range(890,1090) and mouse_y in range(150,450):
                    screen.fill((0, 206, 250))
                    show_3()
                    run_game()
                # 角色4
                if mouse_x in range(1286,1486) and mouse_y in range(150,450):
                    screen.fill((0, 206, 250))
                    show_4()
                    run_game()
                # 角色5
                if mouse_x in range(1682,1882) and mouse_y in range(150,450):
                    screen.fill((0, 206, 250))
                    show_5()
                    run_game()
                # 角色6
                if mouse_x in range(98,298) and mouse_y in range(630,930):
                    screen.fill((0, 206, 250))
                    show_6()
                    run_game()
                # 角色7
                if mouse_x in range(494,694) and mouse_y in range(630,930):
                    screen.fill((0, 206, 250))
                    show_7()
                    run_game()
                # 角色8
                if mouse_x in range(890,1090) and mouse_y in range(630,930):
                    screen.fill((0, 206, 250))
                    show_8()
                    run_game()
                # 角色9
                if mouse_x in range(1286,1486) and mouse_y in range(630,930):
                    screen.fill((0, 206, 250))
                    show_9()
                    run_game()
                # 角色10
                if mouse_x in range(1682,1882) and mouse_y in range(630,930):
                    screen.fill((0, 206, 250))
                    show_10()
                    run_game()


