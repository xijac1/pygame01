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
text_surface = test_font.render('My Game', False, 'Green')




# variable to set fps
clock = pygame.time.Clock()




#event loop
while True:
    #quit the game when window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # creating a simple surface


    screen.blit(background_surface,(0,0))
    screen.blit(text_surface,(300,50))



    pygame.display.update() # update everything
    clock.tick(60) #limit frames to 60 fps

