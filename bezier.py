'''
Universidade Federal de Pernambuco - Campus Recife
Aluna: Paula Crislaine de Oliveira Souza Vaz
Login: pcosv
Matricula: 098.868.804-22
Professor: Silvio Melo
Projeto I - Processamento Grafico
'''

from OpenGL.GL import *
from ponto import Ponto

globVector = []

# Trata todas as chamadas necessarias para realizacao das contas
def bezier(pontos, factor):
    global globVector
    globVector = []

    t = 0
    plus_fator = 1.0 / factor

    while t <= 1:
        bezier_casteljau(pontos, t)
        t += plus_fator

    return globVector


# Calculo da curva de bezier usando o algoritmo de casteljau
def bezier_casteljau(pontos, t):
    global globVector
    num_points = len(pontos)

    if num_points == 1:
        globVector.append(pontos[0])
        glVertex2f(pontos[0].coord_x, pontos[0].coord_y)
    else:
        updated_points = []

        for i in range(0, num_points - 1):
            p = Ponto((t * (pontos[i + 1].coord_x) + (1 - t) * (pontos[i].coord_x)),(t * (pontos[i + 1].coord_y) + (1 - t) * (pontos[i].coord_y)))
            updated_points.append(p)

        bezier_casteljau(updated_points, t)