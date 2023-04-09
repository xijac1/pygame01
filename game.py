import pygame

# initialize the game
pygame.init()
#size of the window size
size = (400,400)
screen = pygame.display.set_mode(size)
#window heading
pygame.display.set_caption("MAZZE")

#event loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

            

