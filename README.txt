Universidade Federal de Pernambuco - Campus Recife
Aluna: Paula Crislaine de Oliveira Souza Vaz
Login: pcosv
Matricula: 098.868.804-22
Professor: Silvio Melo
Projeto I - Processamento Grafico

Tema P1-13: Pintura de área delimitada por uma curva de Bézier Funcional

Descrição: 

O usuário escolhe o grau da curva. O seu sistema deve apresentar num quadrado de tamanho fixo (dado pelo usuário) os pontos de controle inicialmente alinhados, igualmente espaçados (ou seja, se o grau for n, então os pontos de controle estarão correspondendo aos valores de  t=i/n, i=0,1,...,n). O usuário então move qualquer ponto de controle (verticalmente apenas, confinados ao quadrado) e o sistema pinta os pixels do quadrado que estão abaixo ou  na curva de Bézier, de uma cor diferente da cor de cima). O algoritmo de de Casteljau deverá ser usado no cômputo da curva. A pintura deve ser feita em tempo real, ou seja, se o usuário mudar o ponto, a pintura deverá ser feita imediatamente.


Temos 3 arquivos .py e um arquivo .txt:

- ponto.py é onde se encontra a classe Ponto
- bezier.py é onde se encontra o algoritmo de De Casteljau
- graph.py é o aquivo principal, onde está toda a manipulação OpenGL e funções necessárias
- entrada.txt é, como o nome diz, o arquivo de entrada, onde devem-se colocar 3 valores, necessariamente nessa ordem: o grau da curva de bezier, o fator necessário para computo da curva e o tamanho do lado do quadrado a ser desenhado na tela

Como rodar: 

Abra o arquivo de entrada e coloque nele os seus valores de preferência, em seguida, execute o arquivo graph.py. Você irá notar que aparecerá o quadrado com pontos igualmente alinhados, para interagir, você deve arrastar esses pontos verticalmente e observar a curva de bezier se formar na tela.