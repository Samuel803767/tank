import pygame
from scripts.tijolo import Tijolo

# Função para criar o mapa de tijolos a partir da matriz
def criar_labirinto():
    # Matriz do labirinto (1 para tijolos, 0 para espaço vazio)
    labirinto_matriz = [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1],
        [1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1],
        [1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1],
        [1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    tijolos = []
    tijolo_image = "assets/tijolo.png"
    espacamento = 60  # Distância entre os tijolos

    # Para centralizar, vamos adicionar um deslocamento para o centro da tela
    deslocamento_x = 0
    deslocamento_y = 0

    for i, linha in enumerate(labirinto_matriz):
        for j, valor in enumerate(linha):
            if valor == 1:  # Se o valor for 1, cria um tijolo
                # Calculando a posição centralizada do tijolo
                tijolos.append(Tijolo(j * espacamento + deslocamento_x, i * espacamento + deslocamento_y, tijolo_image, tijolo_image))

    return tijolos
