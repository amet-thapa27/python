import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 255)
red = (255, 0, 0)

dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("snake game")
#name the screen

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 10

font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 25)


def Your_score(score):
    value= score_font.render("Your score : " + str(score),True, green)
    dis.blit(value, [0,0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,black,[int(x[0]), int(x[1]), snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [int(dis_width/6),int(dis_height/3)])


def gameloop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = int(random.randrange(0, dis_width - snake_block) / 10) * 10
    foody = int(random.randrange(0, dis_width - snake_block) / 10) * 10

    while not game_over:
        while game_close:
            dis.fill(blue)
            message("You lost ! press Q-Quit or C-Play Again",red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:

                        exit()
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
        pygame.draw.rect(dis , blue, [int(foodx),int(foody),snake_block,snake_block])
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        Your_score(length_of_snake - 1)
        pygame.display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameloop()