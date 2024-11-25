import pygame
import math

class Projetil:
    def __init__(self, x, y, angle, image_path, speed=3):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (20, 20))  # Ajusta o tamanho do projétil
        self.angle = angle
        self.speed = speed

        # Centralizar o projétil no centro do tanque e ajustá-lo à direção
        offset_x = math.cos(math.radians(self.angle)) * 25  # Distância inicial
        offset_y = -math.sin(math.radians(self.angle)) * 25
        self.position = [x + offset_x, y + offset_y]

    def atualizar(self):
        # Movimenta o projétil na direção do ângulo
        self.position[0] += self.speed * math.cos(math.radians(self.angle))
        self.position[1] -= self.speed * math.sin(math.radians(self.angle))

    def desenhar(self, tela):
        # Rotacionar a imagem do projétil
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        rotated_rect = rotated_image.get_rect(center=self.position)

        # Desenhar o projétil
        tela.blit(rotated_image, rotated_rect.topleft)

    def fora_da_tela(self, largura, altura):
        # Verifica se o projétil saiu da tela
        return (
            self.position[0] < 0 or
            self.position[0] > largura or
            self.position[1] < 0 or
            self.position[1] > altura
        )
