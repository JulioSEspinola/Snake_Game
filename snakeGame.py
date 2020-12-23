import pygame
import time
import random
 
#Starts game
pygame.init()
 
#Colos used
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
 
#Window dimensions
dis_width = 500
dis_height = 400
 
#Displays the window
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')
 
clock = pygame.time.Clock()

#Sake block dimensions
snake_block = 10
snake_speed = 10 #Speed of the snake

#fonts used
font_over = pygame.font.SysFont("Helvetica", 20)
score_font = pygame.font.SysFont("Helvetrica", 25)
 
#Displays the score
def score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
 
 
#Displays the snake
def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, red, [x[0], x[1], snake_block, snake_block])
 
#Displays the message after the game is over
def message(msg, color):
    mesg = font_over.render(msg, True, white)
    dis.blit(mesg, [dis_width / 7, dis_height / 2])
 
#Executes snake functionality 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    
    #Runs the program while is game over is not true
    while not game_over:
 
        while game_close == True:
            dis.fill(black)
            message("Game over! Press S-Play Again or Q-Quit", red)
            score(Length_of_snake - 1)
            #updates the window to the new conditions
            pygame.display.update()
 
            #Runs the program when s is pressed and quits when q is pressed
            for i in pygame.event.get():
                if i.type == pygame.KEYDOWN:
                    if i.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if i.key == pygame.K_s:
                        gameLoop()
                        
        #This loop helps the snake move
        for j in pygame.event.get():
            #If the snake touches the wall then the program quits
            if j.type == pygame.QUIT:
                game_over = True
            if j.type == pygame.KEYDOWN:
                if j.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif j.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif j.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif j.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        
        #makes the sanke moke up, down, left and right
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block]) #creates the food
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        
        #Cheks if the snake touches itself then the game ends
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        snake(snake_block, snake_List)
        score(Length_of_snake - 1)
 
        pygame.display.update()
        
        #Food is added randomly and increases the length of the snake
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(snake_speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()
