import pygame
from scripts.jogador import Jogador
from scripts.tijolo import Tijolo

# Inicializar o Pygame
pygame.init()

# Configurações da tela (Aumentando horizontalmente)
WIDTH, HEIGHT = 1200, 600  # Aumentando a largura
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo de Tanque - Colisão e Explosão")

# Cores
BLACK = (0, 0, 0)

# Criar o jogador
jogador = Jogador(WIDTH // 2, HEIGHT // 2, "assets/player1.png", speed=5)

# Função para criar o mapa de tijolos
def criar_mapa():
    tijolos = []
    tijolo_image = "assets/tijolo.png"
    explosao_image = "assets/explosao.png"
    espacamento = 60  # Distância entre os tijolos

    # Criando um mapa de tijolos
    for i in range(5):  # 5 linhas
        for j in range(10):  # 10 colunas
            tijolos.append(Tijolo(j * espacamento + 100, i * espacamento + 100, tijolo_image, explosao_image))

    return tijolos

# Criar tijolos
tijolos = criar_mapa()

# Loop principal
running = True
clock = pygame.time.Clock()

while running:
    # Processar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Dispara o projétil
                jogador.atirar()

    # Capturar teclas pressionadas
    keys = pygame.key.get_pressed()
    jogador.atualizar(keys)

    # Atualizar tijolos e remover os que foram destruídos
    tijolos_remover = []
    for tijolo in tijolos:
        if tijolo.atualizar():
            tijolos_remover.append(tijolo)
        # Detectar colisões entre projéteis e tijolos
        for projetil in jogador.projeteis[:]:
            if tijolo.verificar_colisao(projetil):
                jogador.projeteis.remove(projetil)  # Remove o projétil
                tijolo.destruir()  # Diminui a vida do tijolo
                break

    # Remove tijolos destruídos da lista
    for tijolo in tijolos_remover:
        tijolos.remove(tijolo)

    # Atualizar a tela
    screen.fill(BLACK)
    jogador.desenhar(screen)
    jogador.atualizar_projeteis(screen)

    # Desenhar tijolos
    for tijolo in tijolos:
        tijolo.desenhar(screen)

    # Atualizar a exibição
    pygame.display.flip()

    # Controlar o FPS
    clock.tick(60)

pygame.quit()
