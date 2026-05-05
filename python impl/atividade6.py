"""
Atividade 6 - Analise de estabilidade e causalidade

Sistemas:
  a) y[n] = x[n] + x[n-1]            (FIR de 2 amostras)
  b) y[n] = x[n+1]                   (antecipa a entrada)
  c) h[n] = (0.5)^n * u[n]           (IIR estavel)
  d) h[n] = 2^n * u[n]               (IIR instavel)

Para cada caso, gera h[n] e verifica numericamente:
  - causalidade: h[n] = 0 para n < 0 ?
  - estabilidade: soma |h[n]| finita ?
"""

import numpy as np
import matplotlib.pyplot as plt


def main():
    n = np.arange(-5, 26)

    # (a) y[n] = x[n] + x[n-1]  ->  h[n] = delta[n] + delta[n-1]
    ha = np.zeros_like(n, dtype=float)
    ha[n == 0] = 1.0
    ha[n == 1] = 1.0

    # (b) y[n] = x[n+1]  ->  h[n] = delta[n+1]
    hb = np.zeros_like(n, dtype=float)
    hb[n == -1] = 1.0

    # (c) h[n] = (0.5)^n u[n]
    hc = np.zeros_like(n, dtype=float)
    mask = n >= 0
    hc[mask] = 0.5 ** n[mask]

    # (d) h[n] = 2^n u[n]
    hd = np.zeros_like(n, dtype=float)
    hd[mask] = 2.0 ** n[mask]

    nomes = ["(a) x[n]+x[n-1]", "(b) x[n+1]", "(c) (0.5)^n u[n]", "(d) 2^n u[n]"]
    sistemas = [ha, hb, hc, hd]

    print("Sistema                | Causal | Estavel | Soma |h[n]|")
    print("-----------------------+--------+---------+----------------")
    for nome, h in zip(nomes, sistemas):
        causal = bool(np.all(h[n < 0] == 0))
        soma = float(np.sum(np.abs(h)))
        estavel = soma < 1e6  # limite numerico para considerar finito

        c = "SIM   " if causal else "NAO   "
        e = "SIM    " if estavel else "NAO    "
        print(f"{nome:<22} | {c} | {e} | {soma:g}")

    print()
    print("Observacao: o sistema (d) cresce ilimitadamente -> a soma diverge.")
    print("Numericamente, sum(2^n) cresce explosivamente (>> 1e6).")

    # --- Visualizacao ---
    fig, axes = plt.subplots(2, 2, num="Atividade 6 - Respostas ao impulso", figsize=(10, 7))

    axes[0, 0].stem(n, ha, basefmt=" ")
    axes[0, 0].set_title("(a) h[n] = d[n] + d[n-1] -- causal, estavel")
    axes[0, 0].set_xlabel("n"); axes[0, 0].set_ylabel("h[n]"); axes[0, 0].grid(True)

    axes[0, 1].stem(n, hb, basefmt=" ")
    axes[0, 1].set_title("(b) h[n] = d[n+1] -- NAO causal, estavel")
    axes[0, 1].set_xlabel("n"); axes[0, 1].set_ylabel("h[n]"); axes[0, 1].grid(True)

    axes[1, 0].stem(n, hc, basefmt=" ")
    axes[1, 0].set_title("(c) h[n] = (0.5)^n u[n] -- causal, estavel")
    axes[1, 0].set_xlabel("n"); axes[1, 0].set_ylabel("h[n]"); axes[1, 0].grid(True)

    axes[1, 1].stem(n, hd, basefmt=" ")
    axes[1, 1].set_title("(d) h[n] = 2^n u[n] -- causal, INSTAVEL")
    axes[1, 1].set_xlabel("n"); axes[1, 1].set_ylabel("h[n]"); axes[1, 1].grid(True)

    fig.tight_layout()


if __name__ == "__main__":
    main()
    plt.show()
