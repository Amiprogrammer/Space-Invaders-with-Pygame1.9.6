import random
import math
import pygame
from pygame import mixer

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

# background music
mixer.music.load("background.wav")
mixer.music.play(-1)

# set a player
PlayerImg = pygame.image.load("player.png")
# player position
PlayerX = 370
PlayerY = 480
PlayerX_change = 0

# set a multiple enemy
EnemyImg = []
EnemyX = []
EnemyY = []
EnemyX_change = []
EnemyY_change = []
num_of_enemyes = random.randint(6,8)
for i in range(num_of_enemyes):
    EnemyImg.append(pygame.image.load("enemy.png"))
    # enemy position
    EnemyX.append(random.randint(0,736))
    EnemyY.append(random.randint(50,150))
    EnemyX_change.append(random.choice([-4,4]))
    EnemyY_change.append(40)

# bullet for shooting
BulletImg = pygame.image.load("bullet.png")
# bullet position
BulletX = 0
BulletY = PlayerY
BulletY_change = 38
"""
bullet_state value
    if "Ready!" you can't see the bullet!
    "Fire!" currectly the bullet is shooting!
"""
bullet_state = "Ready!"

# player score
p_score = 0
# postion text
TextX,TextY = 10,10
font_score = pygame.font.Font("Roboto-Bold.ttf",32)

font_copyright = pygame.font.Font("Roboto-Bold.ttf",20)

def show_score(x,y):
    score = font_score.render(f"Score : {p_score}", True, (250,250,250))
    screen.blit(score,(x,y))

gameover_img = pygame.image.load("game-over.png")
def game_over():
    global gameover_img
    screen.blit(gameover_img,(260,140))

def copyright():
    copyright = font_copyright.render("(C) 2020. built by Juliao Martins", True, (180,180,200))
    screen.blit(copyright,(500,560))

# function to include player
def player(x,y):
    global PlayerImg
    screen.blit(PlayerImg,(x,y))

# function to include enemy
def enemy(x,y,i):
    global EnemyImg
    screen.blit(EnemyImg[i],(x,y))

# function to include bullet
def bullet(x,y):
    global BulletImg,bullet_state
    bullet_state = "Fire!"
    screen.blit(BulletImg,(x + 16,y + 10))

# collision and detectod two points is equal
def ColliSion(EnemyX,EnemyY,BulletX,BulletY):
    distance = math.sqrt((math.pow(EnemyX-BulletX,2)) + (math.pow(EnemyY-BulletY,2)))
    if( distance < 27 ):
        return True
    else:
        return False

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
                    lasser = mixer.Sound("laser-shot.wav")
                    lasser.play()
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

    # check of bullet state
    if( bullet_state == "Fire!" ):
        BulletY -= BulletY_change
        bullet(BulletX,BulletY)

    if( BulletY <= 0 ):
        BulletY = PlayerY
        bullet_state = "Ready!"

    for i in range(num_of_enemyes):

        if( EnemyY[i] > 426 ):
            for j in range(num_of_enemyes):
                EnemyY[j] = 5000
            game_over()
            break

        collision = ColliSion(EnemyX[i],EnemyY[i],BulletX,BulletY)
        if( collision ):
            explosion = mixer.Sound("explosion.wav")
            explosion.play()
            BulletY = PlayerY
            bullet_state = "Ready!"
            EnemyX[i] = random.randint(0,736)
            EnemyY[i] = random.randint(50,150)
            EnemyX_change[i] = random.choice([-4,4])
            p_score += 1

        # boundaries of enemy
        if( EnemyX[i] <= 0 ):
            EnemyX_change[i] = 4
            EnemyY[i] += EnemyY_change[i]
        elif( EnemyX[i] >= 736 ):
            EnemyX_change[i] = -4
            EnemyY[i] += EnemyY_change[i]

        # call enemy function
        EnemyX[i] += EnemyX_change[i]
        enemy(EnemyX[i],EnemyY[i], i)

    # movenment of player
    PlayerX += PlayerX_change
    # call player function
    player(PlayerX,PlayerY)

    # call show_score function
    show_score(TextX,TextY)

    # call copyright function
    copyright()

    pygame.display.update() # to update anything in pygame

pygame.quit() # to quit the program