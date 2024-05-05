'''
my first pygame game
100% by me
glitches at around 5 points
'''

#creates all variables and initializes pygame and other functions
import pygame
import random
import time
pygame.init()
screen = pygame.display.set_mode((700, 700))
done = False
x=0
y=0
point_x=random.randrange(0,7)
point_y=random.randrange(0,7)
point_x *= 100
point_y *= 100
score = 0
enemy_x = []
enemy_y = []
enemy = 255,0,0
player = 125,125,125
bgcolor = 0,0,0
point = 0,250,0
#draws the player and the point
pygame.draw.rect(screen, player, pygame.Rect(x, y, 100, 100))
pygame.draw.rect(screen, point, pygame.Rect(point_x, point_y, 100, 100))
pygame.display.flip()
#game loop
while not done:
    #checks if the x button was clicked
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #checks if a key was pressed
        if event.type == pygame.KEYDOWN:
            #checks if the left arrow was pressed
            if event.key == pygame.K_LEFT:
                #checks whether or not the player is touching the edge
                if x > 0:
                    #changes x 
                    x -= 100
                    #draws point and player
                    screen.fill(bgcolor)
                    pygame.draw.rect(screen, player, pygame.Rect(x, y, 100, 100))
                    pygame.draw.rect(screen, point, pygame.Rect(point_x, point_y, 100, 100))
                    #draws enemies
                    repeat = len(enemy_x)
                    while repeat > 0:
                        enemy_x_drawing = enemy_x[repeat-1]
                        enemy_y_drawing = enemy_y[repeat-1]
                        pygame.draw.rect(screen, enemy, pygame.Rect(enemy_x_drawing , enemy_y_drawing , 100, 100))
                        repeat -= 1
                        pygame.display.flip()
                                        
            #same as above(but for different key)
            if event.key == pygame.K_RIGHT:
                if x < 600:
                    x += 100
                    screen.fill(bgcolor)
                    pygame.draw.rect(screen, player, pygame.Rect(x, y, 100, 100))
                    pygame.draw.rect(screen, point, pygame.Rect(point_x, point_y, 100, 100))
                    repeat = len(enemy_x)
                    while repeat > 0:
                        enemy_x_drawing = enemy_x[repeat-1]
                        enemy_y_drawing = enemy_y[repeat-1]
                        pygame.draw.rect(screen, enemy, pygame.Rect(enemy_x_drawing , enemy_y_drawing , 100, 100))
                        repeat -= 1
                        pygame.display.flip()
                                        
            #same as above(but for different key)
            if event.key == pygame.K_UP:
                if y > 0:
                    y -= 100
                    screen.fill(bgcolor)
                    pygame.draw.rect(screen, player, pygame.Rect(x, y, 100, 100))
                    pygame.draw.rect(screen, point, pygame.Rect(point_x, point_y, 100, 100))
                    repeat = len(enemy_x)
                    while repeat > 0:
                        enemy_x_drawing = enemy_x[repeat-1]
                        enemy_y_drawing = enemy_y[repeat-1]
                        pygame.draw.rect(screen, enemy, pygame.Rect(enemy_x_drawing , enemy_y_drawing , 100, 100))
                        repeat -= 1
                        pygame.display.flip()
            #same as above(but for different key)
                if event.key == pygame.K_DOWN:
                    if y < 600:
                        y += 100
                        screen.fill(bgcolor)
                        pygame.draw.rect(screen, player, pygame.Rect(x, y, 100, 100))
                        pygame.draw.rect(screen, point, pygame.Rect(point_x, point_y, 100, 100))
                        repeat = len(enemy_x)
                        while repeat > 0:
                            enemy_x_drawing = enemy_x[repeat-1]
                            enemy_y_drawing = enemy_y[repeat-1]
                            pygame.draw.rect(screen, enemy, pygame.Rect(enemy_x_drawing , enemy_y_drawing , 100, 100))
                            repeat -= 1
                            pygame.display.flip()
            #checks whether or not you are touching the point               
            if point_x == x and point_y == y:
                #changes score
                score += 1
                #new enemy
                random_enemy_x = random.randrange(0,7)
                random_enemy_y = random.randrange(0,7)
                random_enemy_x *= 100
                random_enemy_y *= 100
                #makes sure new enemy is not in the same place as other enemies or the player
                while random_enemy_x == x or random_enemy_x in enemy_x:
                    random_enemy_x = random.randrange(0,7)
                    random_enemy_y = random.randrange(0,7)
                    random_enemy_x *= 100
                    random_enemy_y *= 100
                #adds new enemy to list of enemies
                enemy_x.append(random_enemy_x)
                enemy_y.append(random_enemy_y)
                #generates new point
                point_x=random.randrange(0,7)
                point_y=random.randrange(0,7)
                point_x *= 100
                point_y *= 100
                #makes sure the new point is not in the same location as an enemy
                while point_x in enemy_x:
                    point_x=random.randrange(0,7)
                    point_y=random.randrange(0,7)
                    point_x *= 100
                    point_y *= 100
                screen.fill(bgcolor)
                #figures out how many enemies there are
                repeat = len(enemy_x)
                #draws enemies
                while repeat > 0:
                    enemy_x_drawing = enemy_x[repeat-1]
                    enemy_y_drawing = enemy_y[repeat-1]
                    pygame.draw.rect(screen, enemy, pygame.Rect(enemy_x_drawing , enemy_y_drawing , 100, 100))
                    repeat -= 1
                #draws player and point
                pygame.draw.rect(screen, player, pygame.Rect(x, y, 100, 100))
                pygame.draw.rect(screen, point, pygame.Rect(point_x, point_y, 100, 100))
                pygame.display.flip()
                        
                #checks if the player is touching an enemy
                if x in enemy_x:
                    x_kill = enemy_x.index(x)
                    if y == enemy_y[x_kill]:
                        done = True
                if y in enemy_y:
                    y_kill = enemy_y.index(y)
                    if x == enemy_x[y_kill]:
                        done = True
#closes pygame and prints your score
pygame.quit()
print(score)
