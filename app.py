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

# game looping
running = True
while running:

    # change the background color
    screen.fill((250,250,250)) # RGB color = Red, Green, Blue

    # to get event in pygame
    for event in pygame.event.get():
        # when user click on close window
        if( event.type == pygame.QUIT ):
            # override this value of variable
            running = False

    pygame.display.update() # to update anything in pygame

pygame.quit() # to quit the program
