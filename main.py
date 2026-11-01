import pygame,sys

WIDTH = 600
HEIGHT = 800

def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH,HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    main()