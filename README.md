# Tesouras Estruturais

Projeto em Python destinado à parametrização e representação gráfica de diferentes tipos de tesouras estruturais, utilizando estruturas baseadas em grafos para representar os nós e suas conexões.

## Estruturas implementadas

O programa contempla três tipos de tesouras:

| Classe | Tipo de estrutura | Status |
|---|---|---|
| `Tesoura_Pratt` | Tesoura Pratt | Concluída |
| `Tesoura_Fink` | Tesoura Fink | Em desenvolvimento |
| `Tesoura_Howe` | Tesoura Howe | Em desenvolvimento |

### Tesoura Pratt

A classe `Tesoura_Pratt` implementa a parametrização de uma tesoura do tipo Pratt, permitindo definir suas dimensões e construir sua estrutura a partir de relações entre nós.

### Tesoura Fink

A classe `Tesoura_Fink` tem como objetivo implementar a parametrização de uma tesoura do tipo Fink.

**Status:** Em desenvolvimento.

### Tesoura Howe

A classe `Tesoura_Howe` tem como objetivo implementar a parametrização de uma tesoura do tipo Howe.

**Status:** Em desenvolvimento.

## Estrutura do projeto

```text
.
├── classes.py
├── globals.py
└── README.md
```

## Utilização

As estruturas são representadas por classes independentes, permitindo a criação e manipulação de diferentes configurações de tesouras.

Exemplo conceitual de instanciação:

```python
tesoura = Tesoura_Pratt(largura_banzo_inferior, altura)
```

Os parâmetros devem ser definidos de acordo com as dimensões desejadas para a estrutura.

## Desenvolvimento

O projeto encontra-se em desenvolvimento. Atualmente, a implementação da tesoura Pratt está concluída, enquanto as classes Fink e Howe ainda estão sendo desenvolvidas.

Novas funcionalidades e melhorias poderão ser incorporadas ao longo do desenvolvimento.
