import pygame
from pygame import *
import modulo

pygame.init()

font = pygame.font.SysFont('Times New Roman', 20)
font2= pygame.font.SysFont('Times New Roman',40)


def main_menu():
	pygame.mixer.music.load('overtaken.WAV')
	pygame.mixer.music.set_volume (0.20)
	pygame.mixer.music.play(loops=-1)
	tela_menu = pygame.display.set_mode((500, 500),0,32)
	while True:
		tela_menu.fill((0,0,0))
		tela_menu.blit(pygame.image.load("Fundomenu.png"),(0,0))
		modulo.draw_text('MAIN MENU', (255, 0, 0), tela_menu, 130, 20,font2)
		mx, my = pygame.mouse.get_pos()
		botao1 = pygame.Rect(188, 225, 200, 100)
		botao2= pygame.Rect(170,420,160,50)
		modulo.draw_text('GAME', (255, 0, 0), tela_menu, 188,225,font2)
		modulo.draw_text('REGRAS',(255,0,0),tela_menu, 170,420, font2)
		if botao1.collidepoint((mx, my)):
			modulo.draw_text('GAME', (255,255,255), tela_menu, 188,225,font2)
			if click:
				main()
		if botao2.collidepoint((mx,my)):
			modulo.draw_text('REGRAS',(255,255,255),tela_menu, 170,420, font2)
			if click:
				modulo.regras()
		click = False
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True
		#pygame.draw.rect(tela_menu,(0,0,0),(188,225,120,50))
		
		pygame.display.update()


def main(): 
	
	#Gerar tabuleiro e Fontes Principais
	
	tabuleiro = modulo.gerar_tabuleiro()   
	#print(tabuleiro)
	pontos_player1 = 0
	pontos_player2 = 0

	cor_vez = 255
	cor_prox = 0
	
	jogadas = 1

	matriz = [[' ']*4 for i in range(4)]

	pygame.init()

	tela_jogo = pygame.display.set_mode((800,600))
	tela_jogo.fill((255,255,255))

	fonte = pygame.font.SysFont ("Times New Roman", 40)
	vencedor = fonte.render("GANHOU",False,(255,255,255))
	pontos_jogador_1 = fonte.render(str(pontos_player1),False,(0,0,0))
	pontos_jogador_2 = fonte.render(str(pontos_player2),False,(0,0,0))
	jogador_1 = fonte.render("Alma-Negra:",False,(200,200,200))
	jogador_2 = fonte.render("Chapolin:",False,(255,0,0))
	empate = fonte.render("NINGUEM ",False,(255,255,255))

	tela_jogo.blit(pygame.image.load("Fundojogo.png"),(0,0))
	pygame.display.update()

	#Botões e Musica dentro do jogo 
	
	jogo = True
	pygame.mixer.music.load('MusicaSeaOfThieves.WAV')
	pygame.mixer.music.set_volume (0.20)
	pygame.mixer.music.play(loops=-1)

	while(jogo):
		tela_jogo.blit(pygame.image.load("Fundojogo.png"),(0,0))
		for evento in pygame.event.get():
			if(evento.type == pygame.QUIT):
				jogo = False
			mouse = pygame.mouse.get_pos()
			pygame.draw.rect(tela_jogo,(200,200,200),(685,440,110,40))
			modulo.draw_text('REINICIAR', (0, 0, 0), tela_jogo, 690, 445,font)
			pygame.draw.rect(tela_jogo,(200,200,200),(685,500,110,40))
			modulo.draw_text('MENU', (0, 0, 0), tela_jogo, 710, 505,font)
			if 690+90> mouse[0] > 690 and 440+40 > mouse[1]> 440:
				pygame.draw.rect(tela_jogo,(200,0,0),(685,440,110,40))
				modulo.draw_text('REINICIAR', (255, 255, 255), tela_jogo, 690, 445,font)
				if(evento.type == pygame.MOUSEBUTTONDOWN):
					main()
			if 690+90> mouse[0] > 690 and 500+40 > mouse[1]> 500:
				pygame.draw.rect(tela_jogo,(200,0,0),(685,500,110,40))
				modulo.draw_text('MENU', (255, 255, 255), tela_jogo, 710, 505,font)
				if(evento.type == pygame.MOUSEBUTTONDOWN):
					pygame.quit
					main_menu()
			
			#Tabuleiro e funcionamento da matriz 
			
			if(evento.type == pygame.MOUSEBUTTONDOWN):
				x , y = pygame.mouse.get_pos()
				if((200 < x < 600) and (100 < y < 500)):
					x = (x//100)-2
					y = (y//100)-1

					if (matriz[x][y] != " "):
						continue
					matriz[x][y] = tabuleiro[x][y]

					#Pontuação
					
					def contador(jogador):
						if (tabuleiro[x][y] == "Tesouro"):
							jogador = jogador + 100
						elif (tabuleiro[x][y] == "Buraco" and jogador > 0):                           
							jogador = jogador - 50
						return jogador    
								
					
					if(jogadas % 2 !=0):
						cor_vez = 0
						cor_prox = 255
						pontos_player1 = contador(pontos_player1) 
					elif(jogadas % 2 ==0):
						cor_vez = 255
						cor_prox = 0
						pontos_player2 = contador(pontos_player2) 
					jogadas = jogadas + 1
					pygame.display.update()
			
			#Imagens, nomes para aparecerem na tela e Pontuação final
			
			for linha in range(4):
				for coluna in range(4):

					if (matriz[linha][coluna] == ' '):
						pygame.draw.rect(tela_jogo,(225,120,0),(linha*100+200,coluna*100+100,100,100),1)
					elif(matriz[linha][coluna] == "Tesouro"):
						tela_jogo.blit(pygame.image.load("tesouro.png"),(linha*100+200,coluna*100+100))
					elif(matriz[linha][coluna] == "Buraco"):
						tela_jogo.blit(pygame.image.load("X.png"),(linha*100+200,coluna*100+100))
					else:
						tela_jogo.blit([pygame.image.load("0.png"),pygame.image.load("1.png"),pygame.image.load("2.png"),pygame.image.load("3.png"),pygame.image.load("4.png")][matriz[linha][coluna]],(linha*100+200,coluna*100+100))
				
				pontos_jogador_1 = fonte.render(str(pontos_player1),False,(cor_prox,255,255))
				pontos_jogador_2 = fonte.render(str(pontos_player2),False,(cor_vez,255,255))
				
				
				tela_jogo.blit(pontos_jogador_1,(360,20))
				tela_jogo.blit(pontos_jogador_2,(610,20))
				
				tela_jogo.blit(jogador_1,(147,20))
				tela_jogo.blit(jogador_2,(450,20))
				

				if(jogadas >= 17):
					
					tela_jogo.blit(vencedor,(410,530))
					
					if(pontos_player1 > pontos_player2):
						
						tela_jogo.blit(jogador_1,(197,528))
						
						tela_jogo.blit(pygame.image.load("Thanos.png"),(200,100))
					
					elif(pontos_player1 < pontos_player2):
						
						tela_jogo.blit(jogador_2,(245,530))
						
						tela_jogo.blit(pygame.image.load("Chapolin.png"),(200,100))
					
					else:
						tela_jogo.blit(empate,(205,530))
			
			pygame.display.update()
	pygame.quit()
main_menu()
