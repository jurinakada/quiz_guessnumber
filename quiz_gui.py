import pygame

 #initialize game

pygame.init()

screen = pygame.display.set_mode((1280,780))

clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #screen color
    screen.fill("pink")

    # add welcome message
    font.render()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

