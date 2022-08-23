#----------------------------------------------------------
#PASSO 8: Adicionar contadores para os pontos feito pelo jogador
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

#altera a direção da bola e retorna ela
def moveBola(bola, bolaDirX, bolaDirY):
    bola.x += bolaDirX 
    bola.y += bolaDirY
    return bola

# Verifica por colisão com as bordas
# Retorna uma nova posição caso exista colisão
def verificaColisao(bola, bolaDirX, bolaDirY):
    if bola.top == (LARGURA_LINHA) or bola.bottom == (ALTURA_TELA - LARGURA_LINHA):
        bolaDirY = bolaDirY * -1
    if bola.left == (LARGURA_LINHA) or bola.right == (LARGURA_TELA - LARGURA_LINHA):
        bolaDirX = bolaDirX * -1
    return bolaDirX, bolaDirY


def inteligenciaArtificial(bola, bolaDirX, paleta2):
    # Movimentar a paleta2 (jogador do computador) quando a bola vem em sua direção
    if bolaDirX == 1:
        if paleta2.centery < bola.centery:
            paleta2.y += 1
        else:
            paleta2.y -=1
    return paleta2


#Verifica a colisão da bola com a paleta1 ou paleta2    
def verificaColisaoBola(bola, paleta1, paleta2, bolaDirX):
    if bolaDirX == -1 and paleta1.right == bola.left and paleta1.top < bola.top and paleta1.bottom > bola.bottom:
        return -1
    elif bolaDirX == 1 and paleta2.left == bola.right and paleta2.top < bola.top and paleta2.bottom > bola.bottom:
        return -1
    else: return 1


# ** --------------------------------------------------------
#Verifica se um jogador fez ponto e retorna o novo valor do placar
def verificaPlacar(paleta1, bola, placar, bolaDirX):
    #zera a contagem se a bola acerta a borda do jogador
    if bola.left == LARGURA_LINHA: 
        return 0
    
    #dá 10 pontos para o jogador se computador não rebater
    elif bola.right == LARGURA_TELA - LARGURA_LINHA:
        placar += 10
        return placar
    
    #dá 1 ponto para o jogador, se ele rebater
    elif bolaDirX == 1 and paleta1.right == bola.left and paleta1.top < bola.top and paleta1.bottom > bola.bottom:
        placar += 1
        return placar
    
    #senão, placar fica o mesmo...
    return placar

def desenhaPlacar(placar):
    resultadoSurf = BASICFONT.render('placar = %s' %(placar), True, BRANCO)
    resultadoRect = resultadoSurf.get_rect()
    resultadoRect.topleft = (LARGURA_TELA - 150, 25)
    DISPLAYSURF.blit(resultadoSurf, resultadoRect)

# ** --------------------------------------------------------
    
    
# Função principal
def main():
    pygame.init()
    
    # ** --------------------------------------------------------
    global BASICFONT, BASICFONTSIZE
    BASICFONTSIZE = 20
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTSIZE)
    # ** --------------------------------------------------------
    
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
    placar = 0
    # ** --------------------------------------------------------
    
    #altera a posição da bola
    bolaDirX = -1
    bolaDirY = -1
    
    #Criando os retangulos para a bola e paletas e os coloca na posição inicial
    paleta1 = pygame.Rect(PALETAOFFSET, jogadorUm_posicao, LARGURA_LINHA, PALETA_TAMANHO)
    paleta2 = pygame.Rect(LARGURA_TELA - PALETAOFFSET - LARGURA_LINHA, jogadorDois_posicao, LARGURA_LINHA,PALETA_TAMANHO)
    bola = pygame.Rect(bolaX, bolaY, LARGURA_LINHA, LARGURA_LINHA)
 
    #Desenhando as posições iniciais da arena
    desenhaArena()
    desenhaPaleta(paleta1)
    desenhaPaleta(paleta2)
    desenhaBola(bola)
    
    #pygame.mouse.set_visible(0) #descomente para tornar o cursor do Mouse invisível

    #2-seção "game loop" ----------------------------
    terminou = False
    while not terminou: #Loop principal do jogo
        #3-seção de tratamento de eventos 
        for event in pygame.event.get():
            if event.type == QUIT:
                terminou = True

            elif event.type == MOUSEMOTION:
                mouseX, mouseY = event.pos
                paleta1.y = mouseY

        desenhaArena()
        desenhaPaleta(paleta1)
        desenhaPaleta(paleta2)
        desenhaBola(bola)
        
        bola = moveBola(bola, bolaDirX, bolaDirY)
        
        bolaDirX, bolaDirY = verificaColisao(bola, bolaDirX, bolaDirY)
        
        bolaDirX = bolaDirX * verificaColisaoBola(bola, paleta1, paleta2, bolaDirX)

        paleta2 = inteligenciaArtificial (bola, bolaDirX, paleta2)

        # ** --------------------------------------------------------
        placar = verificaPlacar(paleta1, bola, placar, bolaDirX)
        #print(placar) #descomente para debugar
        desenhaPlacar(placar)
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







