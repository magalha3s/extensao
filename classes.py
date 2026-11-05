import globals
import numpy as np
import matplotlib.pyplot as plt


class Tesoura:
    def __init__(self,largura_banzo_inferior: float, altura: float):

        # Medidas Básicas
        self.largura_banzo_inferior = largura_banzo_inferior
        self.altura = altura
        self.metade_nos_banzo_inferior = round(self.largura_banzo_inferior/(2*globals.ESPACAMENTO_DOS_NOS)) + 1


        # Local de Armazenamento das relações entre as vigas
        self.vigas = {}

        # Local de Armazenamento dos Nós
        self.estrutura = []

        # Numero de Identificadores
        self.id_no = 1
        self.id_viga = 1

        # Cria Banzo Inferior
        self.estrutura.append([0]*(2*self.metade_nos_banzo_inferior-1))
        self.criar_no(i = 0, j = 0)
        


    def criar_viga(self,no_saida,no_chegada):
        # Método para criar uma viga entre dois nós
        if (no_saida.index, no_chegada.index) not in self.vigas.values():
            self.vigas[self.id_viga] = ((no_saida.index, no_chegada.index))
            self.id_viga += 1

    def criar_no(self,i,j):
        self.estrutura[i][j]=No(i,j,self.id_no)

        self.id_no += 1

class Tesoura_Pratt(Tesoura):
    NOME = "Tesoura Pratt"
    def __init__(self,largura_banzo_inferior,altura):
            super().__init__(largura_banzo_inferior,altura)


            # Cria os Níveis da Tesoura
            self.estrutura+=[[0]*len(self.estrutura[0])]*(self.metade_nos_banzo_inferior-1)

            # Gera a Tesoura Parametrizada
            self.build(self.metade_nos_banzo_inferior-1)

    def build(self,center):
        n = 0
        level = 1

        # Crie Lado Esquerdo
        while n != center:
            # Cria Viga no Banzo Inferior
            self.criar_no(i = 0, j = n+1)
            self.criar_viga(self.estrutura[0][n],self.estrutura[0][n+1])

            
            # Cria Montante
            self.criar_no(i = level, j = n+1)
            self.criar_viga(self.estrutura[0][n+1],self.estrutura[level][n+1])

            # Cria Diagonal
            self.criar_viga(self.estrutura[0][n],self.estrutura[level][n+1])

            # Cria Lateral
            self.criar_viga(self.estrutura[n][n],self.estrutura[n+1][n+1])

            n+=1
            level+=1



        # Cria Centro
        if n == center:
                self.criar_viga(self.estrutura[0][n],self.estrutura[level-1][n])

    def calcular_posicoes(self):
        import numpy as np

        n = len(self.estrutura) - 1
        nb = len(self.estrutura[0])
        jc = (nb - 1) / 2

        H = np.array([0, self.altura])
        L = np.array([self.largura_banzo_inferior, 0])

        posicoes = {}

        for camada in self.estrutura:
            for no in camada:
                if no != 0:
                    posicoes[no.index] = (
                        H * no.index[0] / n +
                        L * (no.index[1] - jc) / (nb - 1)
                    )

        return posicoes


    def plotar(self):

        posicoes = self.calcular_posicoes()

        fig, ax = plt.subplots(figsize=(12, 7))

        for id_viga in self.vigas.keys():
            no_saida, no_chegada = self.vigas[id_viga]
            p1 = posicoes[no_saida]
            p2 = posicoes[no_chegada]

            ax.plot(
                [p1[0], p2[0]],
                [p1[1], p2[1]],
                color="black",
                linewidth=1.5
            )

            ax.annotate(
                str(id_viga),
                ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2),
                textcoords="offset points",
                xytext=(0, 3),
                fontsize=9,
                color="green",
                fontweight="bold",
                ha="center",
                va="bottom"
            )

        x = [p[0] for p in posicoes.values()]
        y = [p[1] for p in posicoes.values()]

        ax.scatter(x, y, color="red", s=35, zorder=3)

        for camada in self.estrutura:
            for elemento in camada:
                if elemento != 0:
                    p = posicoes[elemento.index]

                    ax.annotate(
                        str(elemento.id),
                        (p[0], p[1]),
                        textcoords="offset points",
                        xytext=(5, 5),
                        fontsize=8,
                        color="blue"
                    )

        ax.set_aspect("equal")
        ax.grid(True, linestyle="--", alpha=0.4)
        ax.set_xlabel("Largura")
        ax.set_ylabel("Altura")
        ax.set_title(self.NOME if hasattr(self, "NOME") else "Tesoura")

        plt.show()


class No:
    def __init__(self,i: int ,j: int ,id: int = 0): 

        # Posição do Nó na matriz
        self.index = (i,j)

        # Identificação numérica única do Nó
        self.id = id