import pygame

class Tijolo:
    def __init__(self, x, y, image_path, explosao_path):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (50, 50))  # Ajuste do tamanho do tijolo
        self.position = [x, y]
        self.explosao = pygame.image.load('assets/explosao.png')
        self.explosao = pygame.transform.scale(self.explosao, (60, 60))  # Ajuste da explosão
        self.mostrando_explosao = False
        self.tempo_explosao = 0
        self.vida = 3  # O tijolo precisa levar 3 tiros para ser destruído

    def verificar_colisao(self, projetil):
        # Verifica a colisão entre o projetil e o tijolo
        tijolo_rect = pygame.Rect(self.position[0], self.position[1], 50, 50)
        projetil_rect = pygame.Rect(projetil.position[0] - 10, projetil.position[1] - 10, 20, 20)
        return tijolo_rect.colliderect(projetil_rect)

    def destruir(self):
        # Diminui a vida do tijolo e, quando a vida chega a 0, exibe a explosão
        self.vida -= 1
        if self.vida <= 0:
            self.mostrando_explosao = True
            self.tempo_explosao = pygame.time.get_ticks()

    def atualizar(self):
        # Remove a explosão após 1 segundo
        if self.mostrando_explosao:
            if pygame.time.get_ticks() - self.tempo_explosao > 1000:
                self.mostrando_explosao = False
                return True  # Retorna True para remover o tijolo
        return False

    def desenhar(self, tela):
        if self.mostrando_explosao:
            # Desenha a explosão se o tijolo foi destruído
            tela.blit(self.explosao, self.position)
        else:
            # Caso contrário, desenha a imagem do tijolo
            tela.blit(self.image, self.position)
