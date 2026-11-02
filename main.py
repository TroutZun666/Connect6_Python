import pygame,sys

WIDTH = 950
HEIGHT = 950
color = 1
game = True

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
                pos = (j*50+25,i*50+25)
                piece.draw("black",pos)
            elif board[i][j] == 2:
                pos = (j*50+25,i*50+25)
                piece.draw("white",pos)

    if not game:
        font1 = pygame.font.Font("fonts/SourceHanSerifSC-Bold.otf",150)
        font2 = pygame.font.Font("fonts/SourceHanSerifSC-Bold.otf",25)

        text1 = font1.render("游戏结束",True,"red")
        text_rect1 = text1.get_rect()
        text_rect1.center = (WIDTH/2,HEIGHT/2)

        text2 = font2.render("点击空格重新开始",True,"red")
        text_rect2 = text2.get_rect()
        text_rect2.center = (WIDTH/2,HEIGHT/2+120)

        screen.blit(text1,text_rect1)
        screen.blit(text2,text_rect2)

def check():
    global game
    for i in range(19):
        for j in range(19):
            if board[i][j]:
                if j + 5 < 19: 
                    # 判断横向是否连成一线
                    if board[i][j] == board[i][j+1] == board[i][j+2] == board[i][j+3] == board[i][j+4] == board[i][j+5]:
                        game = False
                        break
                if i + 5 < 19:
                    # 判断竖向是否连成一线
                    if board[i][j] == board[i+1][j] == board[i+2][j] == board[i+3][j] == board[i+4][j] == board[i+5][j]:
                        game = False
                        break
                if i + 5 < 19 and j + 5 < 19:
                    # 判断斜向是否连成一线
                    if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i+3][j+3] == board[i+4][j+4] == board[i+5][j+5]:
                        game = False
                        break
                if i + 5 < 19 and j - 5 >= 0:
                    # 判断斜向是否连成一线
                    if board[i][j] == board[i+1][j-1] == board[i+2][j-2] == board[i+3][j-3] == board[i+4][j-4] == board[i+5][j-5]:
                        game = False
                        break

def main():
    global game,color,board

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
            if event.type == pygame.MOUSEBUTTONDOWN and game:
                pos = pygame.mouse.get_pos()
                gx = round((pos[0] - 25) / 50)
                gy = round((pos[1] - 25) / 50)

                if 0 <= gx <= 19 and 0 <= gy <= 19: 
                    if color == 1 and board[gy][gx] == 0:
                        board[gy][gx] = 1
                        color = 2
                    elif color == 2 and board[gy][gx] == 0:
                        board[gy][gx] = 2
                        color = 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game = True
                    color = 1
                    board = []
                    for i in range(19):
                        board.append([0 for i in range(19)])

        draw(screen,piece)
        if game:
            check()

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()