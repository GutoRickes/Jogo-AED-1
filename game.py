import pygame
import random
import sys

#Início
pygame.init()
LARGURA, ALTURA = 200, 300
TGRID = 20
CORES = [
    (0, 0, 0),
    (120, 37, 179),
    (100, 179, 179),
    (80, 34, 22),
    (80, 134, 22),
    (180, 34, 22),
    (180, 34, 122),
    ]
    
class Peca:
    formatos = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[4, 5, 9, 10], [2, 6, 4, 9]],
    ]
    def _init_(self, x, y):
        self.x = x
        self.y = y
        self.tipo = random.randint(0, len(self. formatos) - 1)
        self.cor = random.randint(1, len(CORES) - 1)
        self.rotacao = 0
    
    def imagem(self):
        return self.formatos[self.tipo][self.rotacao]
