import pygame
from pygame import MOUSEBUTTONDOWN
import random
#use random to generate random numbers for mole to go to random.randrange(low, high)

#When we push the file to github just push this file not the entire directory

def main():
    try:
        pygame.init()
        counter = 0
        # You can draw the mole with this snippet:
        pygame.display.set_caption("Whack-A-Mole")
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        mole_x = random.randrange(0, 20)
        mole_y = random.randrange(0, 16)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == MOUSEBUTTONDOWN:
                    counter +=1
                    x, y = event.pos
                    if x//32 == mole_x and y//32 == mole_y:
                        mole_x = random.randrange(0, 20)
                        mole_y = random.randrange(0, 16)

            screen.fill("light green")
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x*32, mole_y*32)))
            #Do not make 20 lines, possibly loop it and change the start pos and end pos
            for i in range(1, 20):
                pygame.draw.line(
                    screen,
                    "dark blue",
                    (i*32,0),
                    (i*32, 512)
                )

            for i in range(1, 16):
                pygame.draw.line(
                    screen,
                    "dark blue",
                    (0, i*32),
                    (640, i*32)
                )

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
