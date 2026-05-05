"""
Atividade 2 - Calculo manual de convolucao (verificacao numerica)

x[n] = {1, 2, 1}
h[n] = {1, 1}

Resultado esperado (manual): y[n] = {1, 3, 3, 1}
"""

import numpy as np
import matplotlib.pyplot as plt


def conv_manual(x, h):
    x = np.asarray(x, dtype=float)
    h = np.asarray(h, dtype=float)
    N, M = len(x), len(h)
    L = N + M - 1
    y = np.zeros(L)
    for n in range(L):
        for k in range(N):
            idx = n - k
            if 0 <= idx < M:
                y[n] += x[k] * h[idx]
    return y


def main():
    x = np.array([1, 2, 1])
    h = np.array([1, 1])

    y_manual = conv_manual(x, h)
    y_np = np.convolve(x, h)

    print("Sequencia x[n]:", x)
    print("Sequencia h[n]:", h)
    print("y[n] calculada manualmente (loop):", y_manual)
    print("y[n] via np.convolve():           ", y_np)

    if np.array_equal(y_manual, y_np):
        print("OK: resultado manual coincide com np.convolve() -> {1, 3, 3, 1}")
    else:
        print("ATENCAO: divergencia entre calculo manual e np.convolve()")

    n = np.arange(len(y_np))
    fig, ax = plt.subplots(num="Atividade 2 - Convolucao manual")
    ax.stem(n, y_np, basefmt=" ")
    ax.set_xlabel("n")
    ax.set_ylabel("y[n]")
    ax.set_title("Atividade 2: y[n] = x[n] * h[n] = {1, 3, 3, 1}")
    ax.grid(True)
    fig.tight_layout()


if __name__ == "__main__":
    main()
    plt.show()
