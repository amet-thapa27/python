import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
blue = (0,0,255)
red = (255,0,0)

dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption("snake game")
#name the screen

snake_block = 10

clock = pygame.time.Clock()
snake_speed = 30

font_style = pygame.font.SysFont(None, 50)


def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [int(dis_width/2),int(dis_height/2)])


def gameloop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    foodx = int(random.randrange(0, dis_width - snake_block) / 10) * 10
    foody = int(random.randrange(0, dis_width - snake_block) / 10) * 10

    while not game_over:
        while game_close:
            dis.fill(white)
            message("You lost ! press Q-Quit or C-Play Again",red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over == True
                        game_close == False
                    if event.key == pygame.K_c:
                        gameloop()

        for event in pygame.event.get():
            #event.get() returns all the action that takes place over it

            if event.type == pygame.QUIT:
                #exit screen when close button is clicked
                game_over = True
            #print(event)
            #prints out all the action that takes place on the screen
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        pygame.draw.rect(dis , blue, [foodx,foody,snake_block,snake_block])
        pygame.draw.rect(dis, black,[int(x1), int(y1), snake_block, snake_block])
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            print("Yummy!!")
        clock.tick(snake_speed)

    pygame.display.update()
    message("you lost",red)
    pygame.quit()
    quit()


gameloop()