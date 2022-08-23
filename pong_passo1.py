#----------------------------------------------------------
#PASSO 1: desenhar a tela do jogo
#----------------------------------------------------------

#1-seção de configuração e definição de variáveis
import pygame, sys
from pygame.locals import * # ** "pygame.locals": submódulo com as constantes da pygame, como QUIT

# CONSTANTES
# Constantes para o tamanho da tela
LARGURA_TELA = 400; ALTURA_TELA = 300
# Será utilizado para a velocidade do jogo
FPS = 200

# Função principal
def main():
    pygame.init()
    global DISPLAYSURF  # ** para que a janela do jogo será tratada com variável global

    FPSCLOCK = pygame.time.Clock()
    #cria a janela do jogo (nesse jogo, foi chamada de DISPLAYSURF)
    DISPLAYSURF = pygame.display.set_mode((LARGURA_TELA,ALTURA_TELA))
    pygame.display.set_caption('PongNet') # ** põe o título na janela
    
    #2-seção "game loop" ----------------------------
    terminou = False
    while not terminou: #Loop principal do jogo
        #3-seção de tratamento de eventos 
        for event in pygame.event.get():
            if event.type == QUIT:
                terminou = True
        
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
