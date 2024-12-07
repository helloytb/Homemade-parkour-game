import sys
import pygame
import math
import random
import time

pygame.init()
colock = pygame.time.Clock()

FPS = 220           # 帧数
SCREEN_WIDTH = 1980  # 屏幕宽
SCREEN_HIGHT = 1080  # 屏幕高


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HIGHT))
pygame.display.set_caption('滚动背景')
# sign = int(time.strftime("%M%S"))
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

    first_time = int(time.strftime("%d%H%M%S"))
    while run:
        now_time = int(time.strftime("%d%H%M%S"))
        # score = int(pygame.time.get_ticks()) / 100
        score = now_time-first_time
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
    fainlly_time = int(time.strftime("%d%H%M%S"))- first_time

    score_back = pygame.font.Font('font/AlimamaShuHeiTi-Bold.ttf', 30)
    score_back = score_back.render(f'{fainlly_time}', True, (255, 0, 0))


    screen.blit(geme_over, (730, 300))
    screen.blit(score_back, (950, 467))

    pygame.display.update()
    #
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:  # 鼠标点击事件
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if mouse_x in range(796,910) and mouse_y in range(560,601):
                    with open('score.txt', 'a+', encoding='utf-8') as f:
                        a = time.strftime("%Y-%m-%d %H:%M:%S")
                        f.write(f'{a} 得分：{fainlly_time}\n==============================\n')
                    run_game()
                if mouse_x in range(1040, 1155) and mouse_y in range(560, 601):
                    with open('score.txt','a+',encoding='utf-8') as f:
                        a = time.strftime("%Y-%m-%d %H:%M:%S")
                        f.write(f'{a} 得分：{fainlly_time}\n==============================\n')
                    sys.exit()


        # screen.blit(score_back, (1720, 100))



# run_game()
