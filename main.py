import pygame,sys

WIDTH = 950
HEIGHT = 950

board = []
for i in range(19):
    board.append([0 for i in range(19)])

class Piece:
    def __init__(self,screen):
        self.screen = screen

    def draw(self,color,pos):
        pygame.draw.circle(self.screen,color,pos,23)

def draw(screen,piece):
    screen.fill("#DEB887")

    for i in range(19):
        pygame.draw.line(screen,"#8B5A2B",(25+i*50,25),(25+i*50,HEIGHT-25),3)
    for j in range(19):
        pygame.draw.line(screen,"#8B5A2B",(25,25+j*50),(WIDTH-25,25+j*50),3)

    for i in range(19):
        for j in range(19):
            if board[i][j] == 1:
                pos = (i*50+25,j*50+25)
                piece.draw("black",pos)
            elif board[i][j] == 2:
                pos = (i*50+25,j*50+25)
                piece.draw("white",pos)

def main():
    COLOR = 1

    pygame.init()

    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Connect6")

    clock = pygame.time.Clock()

    piece = Piece(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                gx = round((pos[0] - 25) / 50)
                gy = round((pos[1] - 25) / 50)

                if COLOR == 1 and board[gx][gy] == 0:
                    board[gx][gy] = 1
                    COLOR = 2
                elif COLOR == 2 and board[gx][gy] == 0:
                    board[gx][gy] = 2
                    COLOR = 1

        draw(screen,piece)

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()