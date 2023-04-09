import pygame
from sys import exit

# initialize the game
pygame.init()
#size of the window size
size = (800,400)
#variables
screen = pygame.display.set_mode(size)

test_surface = pygame.image.load('graphics/background01.jpeg')

#set image dimensions
test_surface = pygame.transform.scale(test_surface, (800,400))

#window heading
pygame.display.set_caption("MAZZE")

clock = pygame.time.Clock()

#event loop
while True:
    #quit the game when window is closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # creating a simple surface


    screen.blit(test_surface,(0,0))


    pygame.display.update()     # update everything
    clock.tick(60) #limit frames to 60 fps






