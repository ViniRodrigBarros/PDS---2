# Estudo Dirigido - Parte 2 (Implementacao em Python)

Versao em Python da implementacao computacional do Estudo Dirigido - Parte 2
(Convolucao e Sistemas LTI). A teoria, deducoes manuais e analises continuam
no [README.md principal](../README.md); este diretorio reproduz os mesmos
calculos numericos e graficos usando `numpy` e `matplotlib`.

## Estrutura

```
python impl/
├── README.md          este arquivo
├── main.py            executa todas as atividades em sequencia
├── atividade2.py      convolucao manual + verificacao com np.convolve
├── atividade3.py      resposta ao impulso por equacao de diferencas
├── atividade4.py      convolucao com np.convolve (dois casos)
├── atividade5.py      filtro de media de 3 pontos
├── atividade6.py      estabilidade e causalidade de 4 sistemas
└── desafio.py         filtro de media movel sobre sinal ruidoso
```

## Requisitos

- Python 3.10+
- `numpy`
- `matplotlib`

Instalacao das dependencias (caso ainda nao estejam disponiveis):

```bash
pip install numpy matplotlib
```

## Como executar

A partir da pasta `python impl/`:

```bash
python main.py
```

Cada script tambem pode ser executado individualmente, por exemplo:

```bash
python atividade4.py
```

## Equivalencias com a versao Octave/MATLAB

| Octave/MATLAB         | Python (numpy)                      |
|-----------------------|-------------------------------------|
| `conv(x, h)`          | `np.convolve(x, h)`                 |
| `zeros(1, N)`         | `np.zeros(N)`                       |
| `0:N-1`               | `np.arange(N)`                      |
| `a .^ n`              | `a ** n`                            |
| `randn(1, N)`         | `np.random.default_rng(seed).standard_normal(N)` |
| `stem(...)`           | `ax.stem(...)`                      |
| `figure / subplot`    | `plt.subplots(...)`                 |

Os resultados numericos sao identicos aos da versao Octave (consulte o
[README principal](../README.md) para as tabelas e analises detalhadas).
