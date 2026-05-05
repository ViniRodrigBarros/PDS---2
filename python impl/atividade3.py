"""
Atividade 3 - Sistema descrito por equacao de diferencas

y[n] = 0.8 * y[n-1] + x[n], com y[-1] = 0 e x[n] = delta[n].

Objetivos:
  1) Calcular h[n] para 0 <= n <= 5 via recursao.
  2) Discutir estabilidade BIBO (somabilidade absoluta de h).
  3) Verificar causalidade.
"""

import numpy as np
import matplotlib.pyplot as plt


def main():
    a = 0.8
    N = 6  # h[0]..h[5]

    # Entrada impulso e saida via recursao
    x = np.zeros(N)
    x[0] = 1.0  # delta[n]

    h = np.zeros(N)
    y_anterior = 0.0  # y[-1] = 0
    for n in range(N):
        h[n] = a * y_anterior + x[n]
        y_anterior = h[n]

    # Forma fechada: h[n] = (0.8)^n * u[n]
    n_vec = np.arange(N)
    h_fechada = a ** n_vec

    print("h[n] obtido pela recursao (n = 0..5):")
    print(h)
    print("h[n] pela forma fechada (0.8)^n:")
    print(h_fechada)

    # --- Estabilidade BIBO ---
    soma_truncada = np.sum(np.abs(h))
    soma_total = 1.0 / (1.0 - a)
    print(f"Soma |h[n]| (n = 0..5)  : {soma_truncada:.4f}")
    print(f"Soma total |h[n]| (n>=0): {soma_total:.4f}")
    print("Como a soma e finita -> sistema ESTAVEL no sentido BIBO.")

    # --- Causalidade ---
    print("h[n] = 0 para n < 0 (forma fechada usa u[n]) -> sistema CAUSAL.")

    # --- Visualizacao ---
    n_plot = np.arange(26)
    h_plot = a ** n_plot
    fig, ax = plt.subplots(num="Atividade 3 - Resposta ao impulso")
    ax.stem(n_plot, h_plot, basefmt=" ")
    ax.set_xlabel("n")
    ax.set_ylabel("h[n]")
    ax.set_title("Atividade 3: h[n] = (0.8)^n u[n] - decaimento exponencial")
    ax.grid(True)
    fig.tight_layout()


if __name__ == "__main__":
    main()
    plt.show()
