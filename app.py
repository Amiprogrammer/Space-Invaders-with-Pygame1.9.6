import random
import pygame

pygame.init() # to initialize

# to create screen
screen = pygame.display.set_mode((800,600))

# set title of screen
pygame.display.set_caption("Space Invaders")

# set icon
# load image
icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

# set a player
PlayerImg = pygame.image.load("player.png")
# player position
PlayerX = 370
PlayerY = 480
PlayerX_change = 0

# set a enemy
EnemyImg = pygame.image.load("enemy.png")
# enemy position
EnemyX = random.randint(0,736)
EnemyY = random.randint(50,150)
EnemyX_change = random.choice([-1,1])
EnemyY_change = 50

# function to include player
def player(x,y):
    global PlayerImg
    screen.blit(PlayerImg,(x,y))

# function to include enemy
def enemy(x,y):
    global EnemyImg
    screen.blit(EnemyImg,(x,y))

# game looping
running = True
while running:

    # change the background color
    screen.fill((19,95,107)) # RGB color = Red, Green, Blue

    # to get event in pygame
    for event in pygame.event.get():
        # when user click on close window
        if( event.type == pygame.QUIT ):
            # override this value of variable
            running = False

        # when user press on keyboard
        if( event.type == pygame.KEYDOWN ):
            if( event.key == pygame.K_LEFT ):
                PlayerX_change = -1
            elif( event.key == pygame.K_RIGHT ):
                PlayerX_change = 1
        # when user not press an arrow of keyboard
        if( event.type == pygame.KEYUP ):
            if( event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT ):
                PlayerX_change = 0

    # boundaries of player
    if( PlayerX <= 0 ):
        PlayerX = 0
    elif( PlayerX >= 736 ):
        PlayerX = 736

    # boundaries of enemy
    if( EnemyX <= 0 ):
        EnemyX_change = 1
    elif( EnemyX >= 736 ):
        EnemyX_change = -1

    # movenment of player
    PlayerX += PlayerX_change
    # call player function
    player(PlayerX,PlayerY)

    # call enemy function
    EnemyX += EnemyX_change
    enemy(EnemyX,EnemyY)

    pygame.display.update() # to update anything in pygame

pygame.quit() # to quit the program
