import pygame
from sys import exit

# initialize the game
pygame.init()
#size of the window size
size = (800,400)
#variables
pygame.display.set_caption("ZOOMY")
screen = pygame.display.set_mode(size)
test_font = pygame.font.Font('fonts/speed-rush-font/SpeedRush-JRKVB.ttf', 50)


background_surface = pygame.image.load('graphics/background01.png')
text_surface = test_font.render('ZOOMY', False, 'Black')

sprite_surface = pygame.image.load('graphics/arrow01.png')

#position
arrow_y_pos = 100
arrow_x_pos = 360
vel = 4
direction = "down"




# variable to set fps
clock = pygame.time.Clock()


#event loop
while True:
    #quit the game when window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
             # check for events
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "down":
                direction = "up"
            elif event.key == pygame.K_DOWN and direction != "up":
                direction = "down"
            elif event.key == pygame.K_LEFT and direction != "right":
                direction = "left"
            elif event.key == pygame.K_RIGHT and direction != "left":
                direction = "right"
       

    # move snake
    if direction == "up":
        arrow_y_pos -= vel
    elif direction == "down":
        arrow_y_pos += vel
    elif direction == "left":
        arrow_x_pos -= vel
    elif direction == "right":
        arrow_x_pos += vel




    # creating a simple surface
    screen.blit(background_surface,(0,0))
    screen.blit(text_surface,(300,50))

    

    screen.blit(sprite_surface,(arrow_x_pos,arrow_y_pos))
    pygame.display.update() 
    clock.tick(60) #limit frames to 60 fps