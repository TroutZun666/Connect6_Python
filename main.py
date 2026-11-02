import pygame,sys

WIDTH = 950
HEIGHT = 950

def draw(screen):
    screen.fill("#DEB887")

    for i in range(19):
        pygame.draw.line(screen,"#8B5A2B",(25+i*50,25),(25+i*50,HEIGHT-25),3)
    for j in range(19):
        pygame.draw.line(screen,"#8B5A2B",(25,25+j*50),(WIDTH-25,25+j*50),3)


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Connect6")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw(screen)

        pygame.display.update()

if __name__ == "__main__":
    main()