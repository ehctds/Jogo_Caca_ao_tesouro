from random import randint
import pygame

def regras():
	sair = False
	while not sair:
		for evento in pygame.event.get():
			if evento.type == pygame.QUIT:
				sair = True
				pygame.quit()
				quit()
			if evento.type == pygame.KEYDOWN or evento.type == pygame.MOUSEBUTTONDOWN:
				sair = True
		tela_regras = pygame.display.set_mode((500, 500),0,32)
		fonte = pygame.font.SysFont('Times New Roman', 20)
		regras1 = fonte.render('Os tesouros e buracos são distribuídos aleatoriamente no', False, (255,255,255))
		regras2 = fonte.render('tabuleiro antes de iniciar o jogo. O jogo terá dois', False, (255,255,255))
		regras3 = fonte.render('participantes que jogarão alternadamente escolhendo casas', False, (255,255,255))
		regras4 = fonte.render('no tabuleiro. Caso um jogador encontre um tesouro, ele', False, (255,255,255))
		regras5 = fonte.render('ganha 100 pontos. Se encontrar um buraco, perde 50 pontos', False, (255,255,255))
		regras6 = fonte.render('(a pontuação não pode ficar negativa). Na hipótese de', False, (255,255,255))
		regras7 = fonte.render('escolher uma casa numérica, seu placar não se altera. O', False, (255,255,255))
		regras8 = fonte.render('jogo termina quando todas as casas são reveladas e vence', False, (255,255,255))
		regras9 = fonte.render('o jogo aquele como o maior número de pontos.', False, (255,255,255))
		voltar = fonte.render('Aperte qualquer tecla para voltar ao menu inicial.', False, (255,0,0))   

		tela_regras.blit(regras1, (5, 65))
		tela_regras.blit(regras2, (5, 85))
		tela_regras.blit(regras3, (5, 105))
		tela_regras.blit(regras4, (5, 125))
		tela_regras.blit(regras5, (5, 145))
		tela_regras.blit(regras6, (5, 165))
		tela_regras.blit(regras7, (5, 185))
		tela_regras.blit(regras8, (5, 205))
		tela_regras.blit(regras9, (5, 225))
		tela_regras.blit(voltar,(25,300))
		pygame.display.update()

def gerar_tabuleiro():
    #buracos
    contador1 = 0
    #tesouros
    contador2 = 0
    #nada
    contador3 = 0
    lista=['Tesouro','Buraco',0]

    #Criador de Buracos e Tesouros
    tabuleiro = []
    for i in range(0,4):
        linhas = []
        
        for j in range(0,4):
            linhas.append(lista[randint(0,2)])
        tabuleiro.append(linhas)
    
    #Corretor da quantiade de buracos
    for i in range(4):
        
        for j in range(0,4):
            if (tabuleiro[i][j] == lista[1] ):
                contador1 += 1
            
            if (tabuleiro[i][j] == lista[1] and contador1 == 4):
                tabuleiro[i][j] = lista[2]
                contador1 -= 1
    
    # Corretor da quantidade de 0
    for i in range(0,4):
        
        for j in range(0,4):
            if(tabuleiro[i][j] == lista[2]):
                contador3 += 1
            
            if(contador3 > 7):
                tabuleiro[i][j] = lista[0]
                contador3 -= 1
    
    #Corretor Quantidade de tesouros
    for i in range(0,4):
        
        for j in range(0,4):
            if (tabuleiro[i][j] == lista[0] ):
                contador2 += 1
            
            if (contador2 > 6 ):
                tabuleiro[i][j] = lista[2]
                contador2 -= 1

    #Contador de posição dos tesouros
    for i in range(4):
        
        for j in range(4):
            cont0 = 0
            
            if(tabuleiro[i][j] == 0):
                    if (i + 1 <= 3):
                        if(tabuleiro[i + 1][j] == "Tesouro"):
                            cont0 += 1
                    
                    if (i - 1 >= 0):
                        if(tabuleiro[i - 1][j] == "Tesouro"):
                            cont0 += 1
                    
                    if j + 1 <= 3:
                        if(tabuleiro[i][j + 1] == "Tesouro"):
                            cont0 += 1
                    
                    if j - 1 >= 0:
                        if(tabuleiro[i][j - 1] == "Tesouro"):
                            cont0 += 1
                    tabuleiro[i][j] = cont0
    return tabuleiro

def draw_text(text, color, surface, x, y, fonte):
    textobj = fonte.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)