import pygame
import math
from scripts.projetil import Projetil

class Jogador:
    def __init__(self, x, y, image_path, speed=1):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (50, 50))  # Ajusta o tamanho do tanque
        self.position = [x, y]
        self.angle = 0
        self.speed = speed
        self.projeteis = []  # Lista para armazenar projéteis

    def atualizar(self, keys):
        # Movimentação e rotação do tanque
        if keys[pygame.K_w]:  # Para cima
            self.angle = 90
            self.position[1] -= self.speed
        if keys[pygame.K_s]:  # Para baixo
            self.angle = -90
            self.position[1] += self.speed
        if keys[pygame.K_a]:  # Para a esquerda
            self.angle = 180
            self.position[0] -= self.speed
        if keys[pygame.K_d]:  # Para a direita
            self.angle = 0
            self.position[0] += self.speed

    def atirar(self):
        # Calcula a posição inicial do projétil com base no centro do tanque
        tanque_centro = [
            self.position[0],  # Coordenada x do centro
            self.position[1]   # Coordenada y do centro
        ]
        # Adiciona um novo projétil
        novo_projetil = Projetil(tanque_centro[0], tanque_centro[1], self.angle, "assets/projetil.png")
        self.projeteis.append(novo_projetil)

    def atualizar_projeteis(self, tela):
        for projetil in self.projeteis[:]:
            projetil.atualizar()
            projetil.desenhar(tela)
            # Remove o projetil se sair da tela
            if projetil.fora_da_tela(tela.get_width(), tela.get_height()):
                self.projeteis.remove(projetil)

    def desenhar(self, tela):
        # Rotacionar a imagem do tanque
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        rotated_rect = rotated_image.get_rect(center=self.position)

        # Desenhar o tanque
        tela.blit(rotated_image, rotated_rect.topleft)
