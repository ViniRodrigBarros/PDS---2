"""
Atividade 4 - Implementacao computacional da convolucao

1) Reproduz a Atividade 2 com np.convolve().
2) Modifica a entrada para x = {1, 1, 1, 1} e interpreta o resultado.
"""

import numpy as np
import matplotlib.pyplot as plt


def main():
    # --- Caso 1: replicacao da Atividade 2 ---
    x1 = np.array([1, 2, 1])
    h = np.array([1, 1])
    y1 = np.convolve(x1, h)

    print("--- Caso 1: x = [1 2 1], h = [1 1] ---")
    print("Sequencia x[n]:", x1)
    print("Sequencia h[n]:", h)
    print("Convolucao y[n] = x[n] * h[n]:", y1)

    n1 = np.arange(len(y1))
    fig1, ax1 = plt.subplots(num="Atividade 4 - Caso 1")
    ax1.stem(n1, y1, basefmt=" ")
    ax1.set_xlabel("n")
    ax1.set_ylabel("y[n]")
    ax1.set_title("Atividade 4 (caso 1): y[n] = x * h = [1 3 3 1]")
    ax1.grid(True)
    fig1.tight_layout()

    # --- Caso 2: x = {1, 1, 1, 1} ---
    x2 = np.array([1, 1, 1, 1])
    y2 = np.convolve(x2, h)

    print()
    print("--- Caso 2: x = [1 1 1 1], h = [1 1] ---")
    print("Sequencia x[n]:", x2)
    print("Convolucao y[n]:", y2)
    print("Forma trapezoidal: subida (1), patamar de soma maxima (2 2 2), descida (1).")
    print("Patamar central = soma da janela h sobre amostras inteiramente sobrepostas.")

    n2 = np.arange(len(y2))
    fig2, ax2 = plt.subplots(num="Atividade 4 - Caso 2")
    ax2.stem(n2, y2, basefmt=" ")
    ax2.set_xlabel("n")
    ax2.set_ylabel("y[n]")
    ax2.set_title("Atividade 4 (caso 2): y[n] = [1 2 2 2 1] (perfil trapezoidal)")
    ax2.grid(True)
    fig2.tight_layout()


if __name__ == "__main__":
    main()
    plt.show()
