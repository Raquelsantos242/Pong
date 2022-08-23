#----------------------------------------------------------
#PASSO 3: Fazer com que a bola se movimente pela tela inteira
#----------------------------------------------------------

#1-seção de configuração e definição de variáveis
import pygame, sys
from pygame.locals import * # ** "pygame.locals": submódulo com as constantes da pygame, como QUIT

# CONSTANTES
# Constantes para o tamanho da tela
LARGURA_TELA = 400; ALTURA_TELA = 300
# Será utilizado para a velocidade do jogo
FPS = 200

# Valores para o desenho das paletas e do fundo
LARGURA_LINHA = 10   #largura das linhas da quadra e da paleta
PALETA_TAMANHO = 50  #altura da paleta
PALETAOFFSET = 20    #distância entre borda da quadra e a paleta
 
# Cores (o jogo é em preto e branco...)
PRETO = (0, 0, 0)       #Cor Preta
BRANCO = (255,255,255)  #Cor Branca
VERMELHO = (255,0,0)  #Cor Vermelha

# Função para desenhar o fundo
def desenhaArena():
    DISPLAYSURF.fill(PRETO)
    # Desenha a quadra
    pygame.draw.rect(DISPLAYSURF, BRANCO, ((0,0),(LARGURA_TELA,ALTURA_TELA)), LARGURA_LINHA*2)
    # Desenha a linha no centro
    pygame.draw.line(DISPLAYSURF, BRANCO, ((LARGURA_TELA//2),0),((LARGURA_TELA//2),ALTURA_TELA), (LARGURA_LINHA//4))


# Função para desenhar a paleta
def desenhaPaleta(paleta):
    #Impede da paleta ir  além da borda do fundo
    if paleta.bottom > ALTURA_TELA - LARGURA_LINHA:
        paleta.bottom = ALTURA_TELA - LARGURA_LINHA
    #Impede da paleta ir  além da borda do topo
    elif paleta.top < LARGURA_LINHA:
        paleta.top = LARGURA_LINHA
    #Desenha a paleta
    pygame.draw.rect(DISPLAYSURF, BRANCO, paleta)
 
 
# Função para desenhar a bola
def desenhaBola(bola):
    pygame.draw.rect(DISPLAYSURF, BRANCO, bola)

# ** --------------------------------------------------------
#altera a direção da bola e retorna ela
def moveBola(bola, bolaDirX, bolaDirY):
    bola.x += bolaDirX
    bola.y += bolaDirY
    return bola
# ** --------------------------------------------------------

# Função principal
def main():
    pygame.init()
    global DISPLAYSURF  # ** para que a janela do jogo será tratada com variável global

    FPSCLOCK = pygame.time.Clock()
    #cria a janela do jogo (nesse jogo, foi chamada de DISPLAYSURF)
    DISPLAYSURF = pygame.display.set_mode((LARGURA_TELA,ALTURA_TELA))
    pygame.display.set_caption('PongNet') # ** põe o título na janela
    
    bolaX = LARGURA_TELA//2 - LARGURA_LINHA//2 #pos. x inicial da bola = 200-5 = 195
    bolaY = ALTURA_TELA//2 - LARGURA_LINHA//2  #pos. y inicial da bola = 150-5 = 145
    jogadorUm_posicao = (ALTURA_TELA - PALETA_TAMANHO) //2   #pos y inicial do jogador1 = (300-50)//2=125
    jogadorDois_posicao = (ALTURA_TELA - PALETA_TAMANHO) //2 #pos y inicial do jogador2 = (300-50)//2=125
    
    # ** --------------------------------------------------------
    #altera a posição da bola
    bolaDirX = -1
    bolaDirY = -1
    # ** --------------------------------------------------------
    
    #Criando os retangulos para a bola e paletas e os coloca na posição inicial
    paleta1 = pygame.Rect(PALETAOFFSET, jogadorUm_posicao, LARGURA_LINHA, PALETA_TAMANHO)
    paleta2 = pygame.Rect(LARGURA_TELA - PALETAOFFSET - LARGURA_LINHA, jogadorDois_posicao, LARGURA_LINHA,PALETA_TAMANHO)
    bola = pygame.Rect(bolaX, bolaY, LARGURA_LINHA, LARGURA_LINHA)
 
    #Desenhando as posições iniciais da arena
    desenhaArena()
    desenhaPaleta(paleta1)
    desenhaPaleta(paleta2)
    desenhaBola(bola)

    #2-seção "game loop" ----------------------------
    terminou = False
    while not terminou: #Loop principal do jogo
        #3-seção de tratamento de eventos 
        for event in pygame.event.get():
            if event.type == QUIT:
                terminou = True

        # ** --------------------------------------------------------
        desenhaArena()
        desenhaPaleta(paleta1)
        desenhaPaleta(paleta2)
        desenhaBola(bola)
        
        bola = moveBola(bola, bolaDirX, bolaDirY)
        # ** --------------------------------------------------------

        #4-atualização da tela do jogo 
        pygame.display.update()
        FPSCLOCK.tick(FPS)

    #---- fim do game loop ---------------------------
    # Finaliza a janela do jogo
    pygame.display.quit()
    # Finaliza o pygame
    pygame.quit()
    sys.exit()


if __name__=='__main__': # ** para chamar a função principal
    main()


