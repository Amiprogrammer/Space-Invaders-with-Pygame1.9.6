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

# background of screen
background = pygame.image.load("background.png")

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
EnemyX_change = random.choice([-4,4])
EnemyY_change = 40

# bullet for shooting
BulletImg = pygame.image.load("bullet.png")
# bullet position
BulletX = 0
BulletY = PlayerY
BulletY_change = 30
"""
bullet_state value
    if "Ready!" you can't see the bullet!
    "Fire!" currectly the bullet is shooting!
"""
bullet_state = "Ready!"

# function to include player
def player(x,y):
    global PlayerImg
    screen.blit(PlayerImg,(x,y))

# function to include enemy
def enemy(x,y):
    global EnemyImg
    screen.blit(EnemyImg,(x,y))

# function to include bullet
def bullet(x,y):
    global BulletImg,bullet_state
    bullet_state = "Fire!"
    screen.blit(BulletImg,(x + 16,y + 10))

# game looping
running = True
while running:

    # change the background color
    screen.fill((19,95,107)) # RGB color = Red, Green, Blue

    # set a background
    screen.blit(background,(0,0))

    # to get event in pygame
    for event in pygame.event.get():
        # when user click on close window
        if( event.type == pygame.QUIT ):
            # override this value of variable
            running = False

        # when user press on keyboard
        if( event.type == pygame.KEYDOWN ):
            if( event.key == pygame.K_LEFT ):
                PlayerX_change = -5
            elif( event.key == pygame.K_RIGHT ):
                PlayerX_change = 5
            elif( event.key == pygame.K_SPACE ):
                if( bullet_state == "Ready!"):
                    # call bullet function
                    BulletX = PlayerX
                    bullet(BulletX,BulletY)
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
        EnemyX_change = 4
        EnemyY += EnemyY_change
    elif( EnemyX >= 736 ):
        EnemyX_change = -4
        EnemyY += EnemyY_change

    # check of bullet state
    if( bullet_state == "Fire!" ):
        BulletY -= BulletY_change
        bullet(BulletX,BulletY)

    if( BulletY <= 0 ):
        BulletY = PlayerY
        bullet_state = "Ready!"

    # movenment of player
    PlayerX += PlayerX_change
    # call player function
    player(PlayerX,PlayerY)

    # call enemy function
    EnemyX += EnemyX_change
    enemy(EnemyX,EnemyY)

    pygame.display.update() # to update anything in pygame

pygame.quit() # to quit the program
