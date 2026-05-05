"""
Desafio - Filtragem de sinal de sensor com filtro de media movel

Cenario: sinal lento (senoide) corrompido por ruido gaussiano rapido.
Aplicamos filtros de media movel com diferentes comprimentos M e
comparamos visualmente (e numericamente, via RMS do erro) o resultado.
"""

import numpy as np
import matplotlib.pyplot as plt


def main():
    rng = np.random.default_rng(42)

    # Sinal "verdadeiro" (lento) e ruido (rapido)
    N = 200
    n = np.arange(N)
    sinal = 5 * np.sin(2 * np.pi * 0.02 * n) + 2  # senoide lenta + nivel DC
    ruido = 1.5 * rng.standard_normal(N)          # ruido branco gaussiano
    x = sinal + ruido                              # leitura do sensor

    # Filtros de media movel com M = 3, 7 e 15
    Ms = [3, 7, 15]
    cores = ["r", "g", "m"]

    fig, ax = plt.subplots(num="Desafio - Filtragem com media movel", figsize=(10, 5))
    ax.plot(n, x, color=(0.7, 0.7, 0.7), label="leitura ruidosa")
    ax.plot(n, sinal, "b", linewidth=1.5, label="sinal verdadeiro")

    print("Comparativo: comprimento do filtro x reducao do ruido")
    print("M | RMS do erro (filtrado vs sinal verdadeiro)")
    print("--+-------------------------------------------")
    for M, cor in zip(Ms, cores):
        h = (1.0 / M) * np.ones(M)
        y = np.convolve(x, h)

        # Compensar o atraso de grupo (M-1)/2 para alinhamento visual
        atraso = (M - 1) // 2
        y_alinhado = y[atraso:atraso + N]

        erro_rms = float(np.sqrt(np.mean((y_alinhado - sinal) ** 2)))
        print(f"{M} | {erro_rms:.4f}")

        ax.plot(n, y_alinhado, cor, linewidth=1.2, label=f"media movel M = {M}")

    ax.set_xlabel("n")
    ax.set_ylabel("amplitude")
    ax.set_title("Desafio: filtragem por media movel (varios M)")
    ax.grid(True)
    ax.legend(loc="best")
    fig.tight_layout()

    print()
    print("Observacoes:")
    print(" - M maior -> mais suavizacao, mas tambem mais distorcao do sinal lento.")
    print(" - M menor -> preserva detalhes, mas filtra menos ruido.")
    print(" - Em todos os casos ha atraso de grupo (M-1)/2 (compensado no plot).")
    print(" - Limitacoes: lobos secundarios na resposta em frequencia, atenuacao")
    print("   de altas freq. legitimas, efeitos de borda nas extremidades.")


if __name__ == "__main__":
    main()
    plt.show()
