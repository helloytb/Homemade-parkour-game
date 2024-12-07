# import pygame
# from roll_back import run_game
# from palyer_show import*
#
# pygame.init()
# screen = pygame.display.set_mode((1980,1080))
#
# def choose():
#     '''角色选择页面'''
#     screen.fill((0,206,250))
#     choosepalyer = pygame.font.SysFont('Arial',30)
#     choosepalyer = choosepalyer.render('plese choose palyer',True,(255,0,0))
#     screen.blit(choosepalyer,[830,50])
#     zhangenxi_1 = pygame.image.load('palyer/zhangenxi_1.jpg')  # 1
#     zhangenxi_2 = pygame.image.load('palyer/zhangenxi_2.jpg')  # 2
#     nieyuxin_1 = pygame.image.load('palyer/nieyuxin_1.jpg')    # 3
#     nieyuxin_2 = pygame.image.load('palyer/nieyuxin_2.jpg')    # 4
#     yangshirui = pygame.image.load('palyer/yangshirui.jpg')    # 5
#     yangzicheng = pygame.image.load('palyer/yangzicheng.jpg')  # 6
#     weishao = pygame.image.load('palyer/weishao.jpg')          # 7
#     liyutong = pygame.image.load('palyer/liyutong.jpg')        # 8
#     sunquankun = pygame.image.load('palyer/sunquankun.png')    # 9
#     yushengyun = pygame.image.load('palyer/yushengyun.jpg')    # 10
#     # 修改图像分辨率
#     zhangenxi_1 = pygame.transform.scale(zhangenxi_1,(200,300))
#     zhangenxi_2 = pygame.transform.scale(zhangenxi_2,(200,300))
#     nieyuxin_1 = pygame.transform.scale(nieyuxin_1,(200,300))
#     nieyuxin_2 = pygame.transform.scale(nieyuxin_2,(200,300))
#     yangshirui = pygame.transform.scale(yangshirui,(200,300))
#     yangzicheng = pygame.transform.scale(yangzicheng,(200,300))
#     weishao  = pygame.transform.scale(weishao,(200,300))
#     liyutong = pygame.transform.scale(liyutong,(200,300))
#     sunquankun = pygame.transform.scale(sunquankun,(200,300))
#     yushengyun = pygame.transform.scale(yushengyun,(200,300))
#
#     # 绘制角色
#     # 第一排
#     screen.blit(zhangenxi_1, [98,150])
#     screen.blit(weishao, [494, 150])
#     screen.blit(nieyuxin_1, [890, 150])
#     screen.blit(yangzicheng, [1286, 150])
#     screen.blit(yangshirui, [1682, 150])
#
#     # 第二排
#     screen.blit(nieyuxin_2, [98, 630])
#     screen.blit(liyutong, [494, 630])
#     screen.blit(sunquankun, [890, 630])
#     screen.blit(yushengyun, [1286, 630])
#     screen.blit(zhangenxi_2, [1682, 630])
#
#     pygame.display.update()
#
#     # 事件检测
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 mouse_x , mouse_y = pygame.mouse.get_pos()
#                 # 角色1
#                 if mouse_x in range(98,298) and mouse_y in range(150,450):
#                     run_game()
#                 # 角色2
#                 if mouse_x in range(494,694) and mouse_y in range(150,450):
#                     run_game()
#                 # 角色3
#                 if mouse_x in range(890,1090) and mouse_y in range(150,450):
#                     run_game()
#                 # 角色4
#                 if mouse_x in range(1286,1486) and mouse_y in range(150,450):
#                     run_game()
#                 # 角色5
#                 if mouse_x in range(1682,1882) and mouse_y in range(150,450):
#                     run_game()
#                 # 角色6
#                 if mouse_x in range(98,298) and mouse_y in range(630,930):
#                     run_game()
#                 # 角色7
#                 if mouse_x in range(494,694) and mouse_y in range(630,930):
#                     run_game()
#                 # 角色8
#                 if mouse_x in range(890,1090) and mouse_y in range(630,930):
#                     run_game()
#                 # 角色9
#                 if mouse_x in range(1286,1486) and mouse_y in range(630,930):
#                     run_game()
#                 # 角色10
#                 if mouse_x in range(1682,1882) and mouse_y in range(630,930):
#                     run_game()
#
#
import pygame
import math
import random
import time
pygame.init()
colock = pygame.time.Clock()

FPS = 120           # 帧数
SCREEN_WIDTH = 1980  # 屏幕宽
SCREEN_HIGHT = 1080  # 屏幕高


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
pygame.display.set_caption('滚动背景')
sign = int(time.strftime("%M%S"))
def run_game():

    x = 20
    y = 550
    player_x = 320
    player_y = 620
    player_di = player_y + 256
    diff =30
    jumping = False


    luzhang = pygame.image.load('image/luzhang.png')
    luzhang = pygame.transform.scale(luzhang,[300,200])
    luzhang_x = 1980
    luzhang_y = 680
    image = pygame.image.load('图像.png')  # 加载图片
    tick = pygame.time.Clock()
    frameNumber = 9  # 设置帧数，示例图片有6帧
    frameRect = image.get_rect()  # 获取全图的框体数据，以此计算单帧框体
    frameRect.width //= frameNumber  # 获取每一帧的边框数据
    fps = 30  # 设置刷新率，数字越大刷新率越高
    fcclock = pygame.time.Clock()
    n = 0

    # 加入背景
    bg = pygame.image.load('background/5.png').convert_alpha()
    # 调整背景大小
    bg = pygame.transform.scale(bg, [300, 1080])

    bg_width = bg.get_width()
    bg_rect = bg.get_rect()
    scroll = 0
    tiles = math.ceil(SCREEN_WIDTH / bg_width) + 1
    run = True

    while run:
        score = int(pygame.time.get_ticks()) / 100

        if fps <= 90:       # 速度增加
            fps += 0.01

        colock.tick(FPS)


        if jumping :       # 跳跃判断
            player_y -= diff
            diff -= 2
            if player_y == 620:
                jumping = False
                diff = 30
                # player_y = 620

        for i in range(0, tiles):   # 背景滚动
            screen.blit(bg, (i * bg_width + scroll, 0))
            bg_rect.x = i * bg_width + scroll


        # 背景速度
        scroll -= 30
        if abs((scroll)) > bg_width:
            scroll = 0

        if n < frameNumber:
            frameRect.x = frameRect.width * n
            n += 1
        else:
            n = 0


        screen.blit(image, (player_x, player_y), frameRect)
        fcclock.tick(fps)
        pygame.display.flip()  # 刷新窗口

        shuzi = random.randint(1, 1000)
        # if shuzi % 3 ==0:
        screen.blit(luzhang,(luzhang_x,luzhang_y))  # 绘制路障
        pygame.display.flip()

        if luzhang_x >= -300:
            luzhang_x -= 20
        if luzhang_x <= -300:
            luzhang_x = 1980

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:  # 键盘事件
                if event.key == pygame.K_SPACE: # 空格按键
                    jumping = True  # 跳跃开启
        if luzhang_x in range(270,376): # 386
            # if player_di - 195 > 680:
            print(player_y)
            if player_y > 422:
                break
            # geme_over = pygame.image.load('image/game_over.png')
            # screen.blit(geme_over, (100, 100))
            # pygame.display.update()

        print(score)
        score_back = pygame.font.Font('font/AlimamaShuHeiTi-Bold.ttf', 30)
        score_back = score_back.render(f'得分：{score}', True, (0, 0, 0))
        screen.blit(score_back, (1720, 100))
        pygame.display.update()

    geme_over = pygame.image.load('image/game_over.png')
    screen.blit(geme_over, (750, 300))
    pygame.display.update()
    #
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()


        # screen.blit(score_back, (1720, 100))



run_game()
