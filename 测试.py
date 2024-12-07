# import requests
# a = 1
#
# r = requests.get('https://www.cnblogs.com/sangzs/p/10643850.html')
# print(r.text)
# # print(a)
# a += 1
import pygame
pygame.init()
screen = pygame.display.set_mode((600,800))
screen.fill((25,0,80))
pygame.display.update()
a = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            # pygame.quit()