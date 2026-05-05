"""
Atividade 5 - Suavizacao de sinais com filtro de media

x[n] = {2, 5, 4, 6, 8, 7, 5, 4}
h[n] = (1/3) * {1, 1, 1}    (filtro de media simples de 3 pontos)
"""

import numpy as np
import matplotlib.pyplot as plt


def main():
    x = np.array([2, 5, 4, 6, 8, 7, 5, 4], dtype=float)
    h = (1.0 / 3.0) * np.array([1, 1, 1], dtype=float)

    y = np.convolve(x, h)

    print("Sinal original x[n]:", x)
    print("Filtro h[n] = (1/3)[1 1 1]:", h)
    print("Sinal suavizado y[n] = x * h:")
    print(np.round(y, 4))

    # --- Plot 1: sinal original ---
    fig1, ax1 = plt.subplots(num="Atividade 5 - Sinal original")
    ax1.stem(np.arange(len(x)), x, basefmt=" ")
    ax1.set_xlabel("n")
    ax1.set_ylabel("x[n]")
    ax1.set_title("Atividade 5: sinal original do sensor")
    ax1.set_ylim(0, 9)
    ax1.grid(True)
    fig1.tight_layout()

    # --- Plot 2: sinal suavizado ---
    fig2, ax2 = plt.subplots(num="Atividade 5 - Sinal filtrado")
    ax2.stem(np.arange(len(y)), y, basefmt=" ")
    ax2.set_xlabel("n")
    ax2.set_ylabel("y[n]")
    ax2.set_title("Atividade 5: sinal suavizado por convolucao com h[n]")
    ax2.set_ylim(0, 9)
    ax2.grid(True)
    fig2.tight_layout()

    # --- Plot 3: comparacao sobreposta ---
    fig3, ax3 = plt.subplots(num="Atividade 5 - Comparacao")
    ax3.stem(np.arange(len(x)), x, linefmt="b-", markerfmt="bo", basefmt=" ",
             label="x[n] original")
    ax3.stem(np.arange(len(y)), y, linefmt="r-", markerfmt="ro", basefmt=" ",
             label="y[n] filtrado")
    ax3.set_xlabel("n")
    ax3.set_ylabel("amplitude")
    ax3.set_title("Atividade 5: comparacao original x suavizado")
    ax3.grid(True)
    ax3.legend(loc="best")
    fig3.tight_layout()

    print()
    print("Observacoes:")
    print(" - Valores intermediarios de y[n] correspondem a media de 3 amostras consecutivas de x.")
    print(" - Valores das bordas (y[0], y[8], y[9]) sao reduzidos por efeito de borda da convolucao linear.")
    print(" - O filtro atua como passa-baixas: atenua oscilacoes rapidas, preserva tendencia.")


if __name__ == "__main__":
    main()
    plt.show()
