'''
Universidade Federal de Pernambuco - Campus Recife
Aluna: Paula Crislaine de Oliveira Souza Vaz
Login: pcosv
Matricula: 098.868.804-22
Professor: Silvio Melo
Projeto I - Processamento Grafico
'''

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from ponto import Ponto
import bezier
import sys

indice = 0
pontos = []
tamanho_ponto = 6.0


# lendo valores informados pelo usuario no arquivo de entrada
with open('entrada','r') as input:
    arquivo = input.readlines()
    grau = int(arquivo[1])
    fator = int(arquivo[3])
    tam_quad = float(arquivo[5])

# tratando o caso do usuario entrar com um valor muito grande para o quadrado
if tam_quad > 600:
    tam_quad = 600

# definindo tamanho da tela
window_h = 700
window_w = 700

# calculando a quantidade de pontos de controle da curva de bezier
qtd_pontos = grau + 1

# vértices do quadrado
ponto_a = Ponto(50.0, 50.0)
ponto_b = Ponto(ponto_a.coord_x + tam_quad, ponto_a.coord_y)
ponto_c = Ponto(ponto_a.coord_x + tam_quad, ponto_b.coord_y + tam_quad)
ponto_d = Ponto(ponto_a.coord_x, ponto_b.coord_y + tam_quad)
quadrado = [ponto_a, ponto_b, ponto_c, ponto_d]

limite = [ponto_a.coord_y, ponto_b.coord_y + tam_quad]

# esta funcao eh responsavel por calcular as coordenadas dos pontos de controle em funcao dos vertices do quadrado
def preencher_pontos():
    global pontos

    pontos = [Ponto(float("{0:.4f}".format((ponto_d.coord_x))),float("{0:.4f}".format((ponto_d.coord_y + (ponto_a.coord_y - ponto_d.coord_y)/2))))]
    i = 1
    while i < qtd_pontos:
        pontos.append(Ponto(float("{0:.4f}".format((pontos[i-1].coord_x + (ponto_c.coord_x - ponto_d.coord_x)/grau))), float("{0:.4f}".format((ponto_d.coord_y + (ponto_a.coord_y - ponto_d.coord_y)/2)))))
        i = i + 1

    return pontos

# funcao responsavel por redesenhar a janela sempre que necessario
def desenha():
    global globVector

    glClear(GL_COLOR_BUFFER_BIT)

    # desenho do quadrado
    glBegin(GL_QUADS)
    glColor3f(0.75, 0.75, 0.75)
    for ponto in quadrado:
        glVertex2f(ponto.coord_x, ponto.coord_y)
    glEnd()

    # desenho dos pontos de controle da curva
    if pontos.__len__() > 0:
        glPointSize(12.0)
        glBegin(GL_POINTS)
        glColor3f(1.0, 0.0, 0.0)
        for ponto in pontos:
            glVertex2f(ponto.coord_x, ponto.coord_y)
        glEnd()

        # desenho das linhas entre os pontos de controle
        if pontos.__len__() > 1:
            glBegin(GL_LINE_STRIP)
            glColor3f(0.0, 1.0, 1.0)
            for ponto in pontos:
                glVertex2f(ponto.coord_x, ponto.coord_y)
            glEnd()

            # desenho da curva de bezier (linhas conectando os pontos computados pelo De Casteljau
            glBegin(GL_LINE_STRIP)
            glColor3f(1.0, 1.0, 1.0)
            globVector = bezier.bezier(pontos, fator)
            glEnd()

            glPointSize(6.0)

            # desenho dos pontos
            glBegin(GL_POINTS)
            glColor3f(0.0, 1.0, 0.0)
            globVector.append(pontos[-1])
            for p in globVector:
               glVertex2d(p.coord_x, p.coord_y)
            glEnd()

            # pintura da area delimitada pela curva
            poligono = [ponto_b] + [ponto_a] + globVector
            glEnable(GL_BLEND)
            glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

            # pintura da area delimitada pela curva
            glBegin(GL_POLYGON)
            glColor4f(0.0,0.0,0.3,0.7)
            for p in poligono:
                glVertex2d(p.coord_x, p.coord_y)
            glEnd()

        else:
            aux = pontos[0]
            glVertex2d(aux.coord_x, aux.coord_y)

    glFlush()

# funcao que controla botoes do teclado
def teclado(tecla):
    # ao clicar esc a janela eh fechada
    if (tecla == 27):
        sys.exit(0)
    glutPostRedisplay()

# funcao que cuida das inicializacoes
def inicializa ():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluOrtho2D(0.0, window_w, window_h, 0.0)


# funcao que cuida do tratamento de cliques no mouse
def gerencia_mouse(botao, estado, x, y):
    global indice
    vector_size = len(pontos)

    # Verifica se o ponto clicado é um ponto de controle
    for p in range(0, vector_size):
        if (x >= pontos[p].coord_x - tamanho_ponto/2) and (x <= pontos[p].coord_x + tamanho_ponto/2):
            if (y >= pontos[p].coord_y - tamanho_ponto / 2) and (y <= pontos[p].coord_y + tamanho_ponto / 2):
                indice = p
                # print ("botao de controle"), p
                break

    glutPostRedisplay()

# funcao que controla o arraste dos pontos de controle confinados ao quadrado
def move_ponto(x, y):
    global indice

    if y < limite[1] and y > limite[0]:
        pontos[indice].coord_y = y
    else:
        pass

    glutPostRedisplay()

# funcao que impede o redimensionamento da janela, evitando deformacoes no desenho
def altera_janela(largura, altura):
    glutReshapeWindow(window_w, window_h)

# loop principal
if __name__ == '__main__':
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
    glutInitWindowPosition(300, 0)
    glutInitWindowSize(window_w, window_h)
    glutCreateWindow(b"Curva de Bezier")

    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    pontos = preencher_pontos()
    glutDisplayFunc(desenha)
    glutReshapeFunc(altera_janela)
    glutKeyboardFunc(teclado)
    glutMouseFunc(gerencia_mouse)
    glutMotionFunc(move_ponto)
    inicializa()
    glutMainLoop()

# fim do programa