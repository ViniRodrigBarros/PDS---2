"""
Estudo Dirigido - Parte 2: Convolucao e Sistemas LTI
Disciplina: Processamento Digital de Sinais
Professor:  Moacy Pereira da Silva
IFPB - Campus Campina Grande

Script mestre: executa todas as atividades em sequencia (versao Python).
"""

import matplotlib.pyplot as plt

import atividade2
import atividade3
import atividade4
import atividade5
import atividade6
import desafio


def secao(titulo):
    print()
    print(">>> " + titulo + " <<<")


def main():
    print("=====================================================")
    print("  ESTUDO DIRIGIDO - PARTE 2 - CONVOLUCAO E LTI")
    print("=====================================================")

    secao("Atividade 2 - Convolucao manual verificada")
    atividade2.main()

    secao("Atividade 3 - Resposta ao impulso (eq. de diferencas)")
    atividade3.main()

    secao("Atividade 4 - Convolucao com np.convolve()")
    atividade4.main()

    secao("Atividade 5 - Suavizacao com filtro de media")
    atividade5.main()

    secao("Atividade 6 - Estabilidade e causalidade")
    atividade6.main()

    secao("Desafio - Filtro de media movel em sinal ruidoso")
    desafio.main()

    print()
    print("=====================================================")
    print("  Execucao concluida.")
    print("=====================================================")

    plt.show()


if __name__ == "__main__":
    main()
