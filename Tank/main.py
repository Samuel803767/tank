import pygame
from scripts.jogador import Jogador
from scripts.tijolo import Tijolo
from scripts.mapa import criar_labirinto

# Inicializar o Pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 1200, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo de Tanque - Colisão e Explosão")

# Cores
BLACK = (0, 0, 0)

# Criar o jogador 1 com controles WASD
controles_jogador1 = {
    'cima': pygame.K_w,
    'baixo': pygame.K_s,
    'esquerda': pygame.K_a,
    'direita': pygame.K_d
}
jogador1 = Jogador(WIDTH // 4, HEIGHT // 2, "assets/player1.png", speed=5, controles=controles_jogador1)

# Criar o jogador 2 com controles de setas
controles_jogador2 = {
    'cima': pygame.K_UP,
    'baixo': pygame.K_DOWN,
    'esquerda': pygame.K_LEFT,
    'direita': pygame.K_RIGHT
}
jogador2 = Jogador(3 * WIDTH // 4, HEIGHT // 2, "assets/player2.png", speed=5, controles=controles_jogador2)

# Criar o mapa de tijolos
tijolos = criar_labirinto()

# Loop principal
running = True
clock = pygame.time.Clock()

while running:
    # Processar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Atirar para o jogador 1
                jogador1.atirar()
            if event.key == pygame.K_RETURN:  # Atirar para o jogador 2
                jogador2.atirar()

    # Capturar teclas pressionadas para o movimento
    keys = pygame.key.get_pressed()
    
    # Atualiza os jogadores com suas respectivas teclas de movimento
    jogador1.atualizar(keys)  # Jogador 1 controla com WASD
    jogador2.atualizar(keys)  # Jogador 2 controla com setas do teclado

    # Atualizar tijolos e remover os que foram destruídos
    tijolos_remover = []
    for tijolo in tijolos:
        if tijolo.atualizar():  # Se o tijolo foi destruído
            tijolos_remover.append(tijolo)  # Marca o tijolo para remoção
        for projetil in jogador1.projeteis[:]:  # Verifica colisões do jogador 1
            if tijolo.verificar_colisao(projetil):
                jogador1.projeteis.remove(projetil)
                tijolo.destruir()
                break
        for projetil in jogador2.projeteis[:]:  # Verifica colisões do jogador 2
            if tijolo.verificar_colisao(projetil):
                jogador2.projeteis.remove(projetil)
                tijolo.destruir()
                break

    # Remove tijolos destruídos da lista
    for tijolo in tijolos_remover:
        tijolos.remove(tijolo)

    # Atualizar a tela
    screen.fill(BLACK)  # Limpa a tela com a cor preta
    jogador1.desenhar(screen)  # Desenha o jogador 1
    jogador1.atualizar_projeteis(screen)  # Desenha os projéteis do jogador 1
    jogador2.desenhar(screen)  # Desenha o jogador 2
    jogador2.atualizar_projeteis(screen)  # Desenha os projéteis do jogador 2
    for tijolo in tijolos:  # Desenha os tijolos
        tijolo.desenhar(screen)

    # Atualizar a exibição
    pygame.display.flip()
    clock.tick(60)  # Controla o FPS do jogo

pygame.quit()
