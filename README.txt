Universidade Federal de Pernambuco - Campus Recife
Aluna: Paula Crislaine de Oliveira Souza Vaz
Login: pcosv
Matricula: 098.868.804-22
Professor: Silvio Melo
Projeto I - Processamento Grafico

Tema P1-13: Pintura de �rea delimitada por uma curva de B�zier Funcional

Descri��o: 

O usu�rio escolhe o grau da curva. O seu sistema deve apresentar num quadrado de tamanho fixo (dado pelo usu�rio) os pontos de controle inicialmente alinhados, igualmente espa�ados (ou seja, se o grau for n, ent�o os pontos de controle estar�o correspondendo aos valores de  t=i/n, i=0,1,...,n). O usu�rio ent�o move qualquer ponto de controle (verticalmente apenas, confinados ao quadrado) e o sistema pinta os pixels do quadrado que est�o abaixo ou  na curva de B�zier, de uma cor diferente da cor de cima). O algoritmo de de Casteljau dever� ser usado no c�mputo da curva. A pintura deve ser feita em tempo real, ou seja, se o usu�rio mudar o ponto, a pintura dever� ser feita imediatamente.


Temos 3 arquivos .py e um arquivo .txt:

- ponto.py � onde se encontra a classe Ponto
- bezier.py � onde se encontra o algoritmo de De Casteljau
- graph.py � o aquivo principal, onde est� toda a manipula��o OpenGL e fun��es necess�rias
- entrada.txt �, como o nome diz, o arquivo de entrada, onde devem-se colocar 3 valores, necessariamente nessa ordem: o grau da curva de bezier, o fator necess�rio para computo da curva e o tamanho do lado do quadrado a ser desenhado na tela

Como rodar: 

Abra o arquivo de entrada e coloque nele os seus valores de prefer�ncia, em seguida, execute o arquivo graph.py. Voc� ir� notar que aparecer� o quadrado com pontos igualmente alinhados, para interagir, voc� deve arrastar esses pontos verticalmente e observar a curva de bezier se formar na tela.