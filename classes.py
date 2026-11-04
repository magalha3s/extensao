import globals

class Tesoura:
     def __init__(self,largura_banzo_inferior,altura):

        # Medidas Básicas
        self.largura_banzo_inferior = largura_banzo_inferior
        self.altura = altura
        self.metade_nos_banzo_inferior = round(self.largura_banzo_inferior/(2*globals.ESPACAMENTO_DOS_NOS)) + 1


        # Local de Armazenamento das relações entre as vigas
        self.vigas = []

        # Local de Armazenamento dos Nós
        self.estrutura = []

        # Cria Banzo Inferior
        self.estrutura.append([No(0,j) for j in range(2*self.metade_nos_banzo_inferior-1)])

class Tesoura_Pratt(Tesoura):
    NOME = "Tesoura Pratt"
    def __init__(self,largura_banzo_inferior,altura):
            super().__init__(largura_banzo_inferior,altura)

            self.vigas = set(())

            self.estrutura+=[[0]*len(self.estrutura[0])]*(self.metade_nos_banzo_inferior-1)

            self.build(self.metade_nos_banzo_inferior-1)

    def criar_viga(self,no_saida,no_chegada):
        self.vigas.add((no_saida.index, no_chegada.index))

    def build(self,center):
        n = 0
        level = 1

        # Crie Lado Esquerdo
        while n != center:

            try:
                # Cria Viga no Banzo Inferior
                self.criar_viga(self.estrutura[0][n],self.estrutura[0][n+1])

                
                # Cria Montante
                self.estrutura[level][n+1]=No(level,n+1)
                self.criar_viga(self.estrutura[0][n+1],self.estrutura[level][n+1])

                # Cria Diagonal
                self.criar_viga(self.estrutura[0][n],self.estrutura[level][n+1])

                n+=1
                level+=1

            except IndexError:
                self.estrutura.append([0] * len(self.estrutura[0]))

        # Cria Centro
        if n == center:
                self.criar_viga(self.estrutura[0][n],self.estrutura[level-1][n])     

        # Cria Lado Direito
        n = len(self.estrutura[0])-1
        level = 1
        while n != center:

            try:
                # Cria Viga no Banzo Inferior
                self.criar_viga(self.estrutura[0][n],self.estrutura[0][n-1])

                
                # Cria Montante
                self.estrutura[level][n-1]=No(level,n-1)
                self.criar_viga(self.estrutura[0][n-1],self.estrutura[level][n-1])

                # Cria Diagonal
                self.criar_viga(self.estrutura[0][n],self.estrutura[level][n-1])

                n-=1
                level+=1

            except IndexError:

                self.estrutura.append([0] * len(self.estrutura[0]))
        n == 0
        while n != center:
            self.criar_viga(self.estrutura[n][n],self.estrutura[n+1][n+1])
            n+=1

class No:
    def __init__(self,i,j): 
        self.index = (i,j)