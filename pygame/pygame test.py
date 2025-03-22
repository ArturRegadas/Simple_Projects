import pygame
from pygame.locals import *
from sys import exit
from random import randint

pontos=0
x=23
y=23
pygame.init()



x1=randint(40, 400)
y1=randint(40, 400)
janela = pygame.display.set_mode((640, 480))
pygame.display.set_caption(' teste pygame')
fps=pygame.time.Clock()
#                       fonte/tamanho/Negrito/letra_meio_de_lado
fonte=pygame.font.SysFont('arial', 45, True, False)

while True:
    fps.tick(75)
    #            R G  B
    janela.fill((0,0,255))
    msg=f'teste em numeros: {pontos}'
    #                       variavel /nao pixelado/ cor
    msg_formatado = fonte.render(msg, True, (255, 255, 255) )
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        '''if event.type == KEYDOWN:
            if event.key == K_a:
                x=x-1
            if event.key == K_d:
                x=x+1
            if event.key == K_w:
                y=y-1
            if event.key == K_s:
                y=y+1'''
        if pygame.key.get_pressed()[K_a]:
            x=x-1
        if pygame.key.get_pressed()[K_d]:
            x=x+1
        if pygame.key.get_pressed()[K_w]:
            y=y-1
        if pygame.key.get_pressed()[K_s]:
            y=y+1

    quadrado = pygame.draw.rect(janela, (0, 255, 0), (x, y, 20, 30))
    circulo = pygame.draw.circle(janela, (255, 255, 255), (x1, y1), 40)
    pygame.draw.line(janela, (255, 0, 0), (10, 233), (600, 40 ), 10)
    if quadrado.colliderect(circulo):
        x1=randint(40, 400)
        y1=randint(40, 400)
        print('BOOM')
        pontos=pontos+1
    janela.blit(msg_formatado, (100, 40))
    pygame.display.update()
