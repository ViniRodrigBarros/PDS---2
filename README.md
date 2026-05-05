# Estudo Dirigido - Parte 2: Convolução e Sistemas LTI

**Disciplina:** Processamento Digital de Sinais
**Professor:** Moacy Pereira da Silva
**Instituição:** IFPB - Campus Campina Grande

---

## Estrutura do Projeto

```
PDS - 2/
├── README.md           Relatório completo com respostas teóricas e análises
├── main.m              Script mestre que executa todas as atividades em sequência
├── atividade2.m        Verificação computacional do cálculo manual (Atv. 2)
├── atividade3.m        Resposta ao impulso por equação de diferenças (Atv. 3)
├── atividade4.m        Convolução com o comando conv (Atv. 4)
├── atividade5.m        Suavização com filtro de média (Atv. 5)
├── atividade6.m        Análise de estabilidade e causalidade (Atv. 6)
└── desafio.m           Filtro de média móvel sobre sinal ruidoso (Desafio)
```

### Como executar

Abra o Octave (ou MATLAB), navegue até a pasta do projeto e digite:

```octave
main
```

Cada script também pode ser executado individualmente.

---

## Atividade 1 - Interpretação Conceitual

### 1) O que significa afirmar que um sistema é linear e invariante no tempo?

Um sistema é **linear** quando obedece simultaneamente às propriedades de **superposição** (aditividade) e **homogeneidade** (escala): dadas as entradas `x1[n]` e `x2[n]` com saídas correspondentes `y1[n]` e `y2[n]`, o sistema linear satisfaz

```
T{a·x1[n] + b·x2[n]} = a·y1[n] + b·y2[n],   para quaisquer constantes a, b.
```

Um sistema é **invariante no tempo** quando um deslocamento na entrada produz exatamente o mesmo deslocamento na saída, sem alterar a forma da resposta:

```
se x[n] -> y[n], então x[n - n0] -> y[n - n0].
```

Em outras palavras, as propriedades internas do sistema não mudam ao longo do tempo: aplicar a mesma entrada hoje ou amanhã gera a mesma resposta, apenas deslocada.

### 2) Por que a resposta ao impulso é suficiente para caracterizar um sistema LTI?

Qualquer sequência discreta pode ser decomposta como uma soma ponderada de impulsos deslocados:

```
x[n] = Σ x[k]·δ[n - k]
```

Aplicando o sistema T{·} a essa decomposição e usando **linearidade**, podemos tirar a soma e os coeficientes `x[k]` para fora do operador. Usando **invariância no tempo**, a resposta a `δ[n-k]` é simplesmente `h[n-k]`. Daí:

```
y[n] = T{x[n]} = Σ x[k]·h[n - k] = x[n] * h[n]
```

Portanto, conhecer apenas a resposta ao impulso `h[n]` é suficiente para prever a saída do sistema para qualquer entrada possível. Essa é a razão pela qual `h[n]` é chamada de **assinatura** do sistema LTI.

### 3) Qual o significado físico da convolução em sistemas discretos?

A convolução `y[n] = x[n] * h[n]` representa a saída do sistema como uma **soma ponderada de cópias deslocadas e escaladas da resposta ao impulso**. Cada amostra da entrada `x[k]` excita o sistema e cria, na saída, uma réplica de `h[n-k]` com peso `x[k]`. A saída total no instante `n` é a superposição (soma) de todas essas réplicas no instante `n`.

Fisicamente, isto descreve a **memória do sistema**: o valor de saída em um determinado instante é uma "lembrança ponderada" das entradas presentes e passadas, com os pesos dados pela resposta ao impulso.

### 4) Qual a diferença entre resposta transitória e regime permanente?

- **Resposta transitória**: é a parcela da saída que decorre da energia inicial armazenada no sistema (memória) e das primeiras amostras da entrada. Em sistemas estáveis, ela decai ao longo do tempo até desaparecer.
- **Regime permanente**: é o comportamento da saída após a extinção do transitório. Para uma entrada periódica, por exemplo, o regime permanente também será periódico com a mesma frequência.

### 5) O que se entende por sistema causal?

Um sistema é **causal** quando, em qualquer instante `n0`, a saída depende apenas de valores **presentes e passados** da entrada (x[n] com n ≤ n0), nunca de valores futuros. Para um sistema LTI, isto equivale a:

```
h[n] = 0,   para todo n < 0.
```

Sistemas físicos em tempo real são, por construção, causais — pois é impossível conhecer o valor da entrada em instantes que ainda não ocorreram.

### 6) O que se entende por sistema estável?

Um sistema é **estável no sentido BIBO** (Bounded Input - Bounded Output) se toda entrada limitada produzir uma saída também limitada. Para sistemas LTI, a condição necessária e suficiente para estabilidade BIBO é a **somabilidade absoluta** da resposta ao impulso:

```
Σ |h[n]| < ∞   (n de -∞ a +∞)
```

---

## Atividade 2 - Cálculo Manual de Convolução

**Dados:**
- `x[n] = {1, 2, 1}` para n = 0, 1, 2
- `h[n] = {1, 1}` para n = 0, 1

### Cálculo passo a passo

A convolução discreta é

```
y[n] = Σ x[k]·h[n - k]
```

O comprimento da saída é `N + M - 1 = 3 + 2 - 1 = 4` amostras.

Calculando termo a termo:

| n | Soma envolvida | Valor |
|---|----------------|-------|
| 0 | x[0]·h[0] = 1·1 | **1** |
| 1 | x[0]·h[1] + x[1]·h[0] = 1·1 + 2·1 | **3** |
| 2 | x[1]·h[1] + x[2]·h[0] = 2·1 + 1·1 | **3** |
| 3 | x[2]·h[1] = 1·1 | **1** |

### Resultado

```
y[n] = {1, 3, 3, 1}
```

### Significado do resultado

A resposta `y[n]` é simétrica e maior no centro porque:

1. `h[n] = {1, 1}` corresponde a um filtro que **soma duas amostras consecutivas** da entrada.
2. Nas extremidades do sinal `x[n]`, há "menos amostras" para somar (por isso `y[0] = 1` e `y[3] = 1`), enquanto no meio há sobreposição completa, gerando os valores maiores `y[1] = 3` e `y[2] = 3`.
3. O resultado também ilustra que a convolução **alarga o sinal**: a saída tem 4 amostras, embora a entrada tivesse 3.

---

## Atividade 3 - Sistema Descrito por Equação de Diferenças

**Sistema:** `y[n] = 0.8·y[n-1] + x[n]`, com `y[-1] = 0` e `x[n] = δ[n]`.

### 1) Resposta ao impulso h[n] para 0 ≤ n ≤ 5

Usando a recursão (lembrando que para `x[n] = δ[n]`, somente `x[0] = 1`; demais zero):

| n | Cálculo | h[n] |
|---|---------|------|
| 0 | 0.8·0 + 1 | **1.0000** |
| 1 | 0.8·1 + 0 | **0.8000** |
| 2 | 0.8·0.8 | **0.6400** |
| 3 | 0.8·0.64 | **0.5120** |
| 4 | 0.8·0.512 | **0.4096** |
| 5 | 0.8·0.4096 | **0.3277** |

Forma fechada: `h[n] = (0.8)^n · u[n]`.

### 2) Análise de estabilidade

A condição BIBO exige `Σ |h[n]| < ∞`. Como `h[n]` é uma série geométrica de razão `r = 0.8 < 1`:

```
Σ |h[n]| = Σ (0.8)^n = 1 / (1 - 0.8) = 5
```

A soma é finita, logo o sistema é **estável**. Observa-se que os valores de h[n] decaem exponencialmente — comportamento característico de sistemas estáveis com polo dentro do círculo unitário.

### 3) Análise de causalidade

A equação `y[n] = 0.8·y[n-1] + x[n]` calcula a saída em `n` a partir de:
- `y[n-1]`: saída passada (valor já calculado)
- `x[n]`: entrada presente

Não há dependência de `x[n+1]` ou valores futuros. Adicionalmente, `h[n] = 0` para `n < 0` (já que `u[n] = 0` para n negativo). Portanto o sistema é **causal**.

---

## Atividade 4 - Implementação Computacional da Convolução

O script [atividade4.m](atividade4.m) implementa a convolução em Octave.

### Comparação com cálculo manual

Para `x = [1 2 1]` e `h = [1 1]`:

```
y = conv(x, h) = [1  3  3  1]
```

Resultado **idêntico** ao cálculo manual da Atividade 2, validando o procedimento.

### Forma do sinal de saída

O sinal `y[n]` apresenta um perfil **triangular crescente-decrescente**: cresce porque mais amostras de `x[n]` participam da soma à medida que `h[n]` "desliza" sobre `x[n]`, atinge um máximo quando há sobreposição completa e decresce quando o filtro começa a "deixar" o sinal.

### Modificação para x[n] = {1, 1, 1, 1}

Com a nova entrada (4 amostras unitárias) e o mesmo `h = [1 1]`:

```
y = conv([1 1 1 1], [1 1]) = [1  2  2  2  1]
```

**Interpretação:**
- Saída tem `4 + 2 - 1 = 5` amostras.
- Os extremos (1 e 1) representam regiões de **sobreposição parcial** entre `x` e `h` (apenas uma das amostras de `h` "encontra" `x`).
- O patamar central (2, 2, 2) corresponde à **sobreposição completa**: ambas as amostras de `h` veem amostras de `x`, e a soma é `1 + 1 = 2`.
- Esse formato trapezoidal é típico da convolução entre dois pulsos retangulares de comprimentos diferentes.

---

## Atividade 5 - Suavização de Sinais

**Sinal de sensor:** `x[n] = {2, 5, 4, 6, 8, 7, 5, 4}`
**Filtro de média de 3 pontos:** `h[n] = (1/3)·{1, 1, 1}`

### Cálculo da convolução

Aplicando `y[n] = Σ x[k]·h[n-k]`:

| n | Janela ativa | Cálculo | y[n] |
|---|--------------|---------|------|
| 0 | x[0] | (1/3)·2 | 0.667 |
| 1 | x[0..1] | (1/3)·(2+5) | 2.333 |
| 2 | x[0..2] | (1/3)·(2+5+4) | 3.667 |
| 3 | x[1..3] | (1/3)·(5+4+6) | 5.000 |
| 4 | x[2..4] | (1/3)·(4+6+8) | 6.000 |
| 5 | x[3..5] | (1/3)·(6+8+7) | 7.000 |
| 6 | x[4..6] | (1/3)·(8+7+5) | 6.667 |
| 7 | x[5..7] | (1/3)·(7+5+4) | 5.333 |
| 8 | x[6..7] | (1/3)·(5+4) | 3.000 |
| 9 | x[7] | (1/3)·4 | 1.333 |

A implementação numérica e os gráficos estão em [atividade5.m](atividade5.m).

### Por que o filtro atua como suavizador?

1. **Atenuação de variações rápidas:** o filtro substitui cada amostra pela média das três amostras vizinhas; oscilações curtas (ruído) tendem a se cancelar nessa média, enquanto tendências mais lentas (o sinal de interesse) sobrevivem.
2. **Resposta em frequência passa-baixas:** o filtro de média móvel possui resposta em frequência do tipo sinc(ωM/2)/sinc(ω/2), que atenua altas frequências (onde tipicamente reside o ruído).
3. **Suavização da derivada discreta:** ao calcular médias locais, o filtro produz um sinal mais "macio", com transições menos abruptas — efeito visualizado claramente no gráfico do sinal filtrado em comparação com o original.

**Observação importante:** as primeiras e últimas amostras de `y[n]` (regiões de transição) apresentam valores artificialmente menores devido ao "preenchimento implícito com zeros" — efeito de borda típico em convolução linear.

---

## Atividade 6 - Análise de Estabilidade e Causalidade

### a) y[n] = x[n] + x[n-1]

A resposta ao impulso é `h[n] = δ[n] + δ[n-1]`.

- **Causal:** SIM. A saída depende apenas de `x[n]` e `x[n-1]` (presente e passado).
- **Estável:** SIM. `Σ |h[n]| = 1 + 1 = 2 < ∞`. Filtro FIR é sempre estável.

### b) y[n] = x[n+1]

Resposta ao impulso: `h[n] = δ[n+1]`.

- **Causal:** NÃO. A saída em `n` depende da entrada em `n+1` (instante futuro).
- **Estável:** SIM. `Σ |h[n]| = 1 < ∞`.

### c) h[n] = (0.5)^n · u[n]

- **Causal:** SIM. `h[n] = 0` para `n < 0` (presença do `u[n]`).
- **Estável:** SIM. Série geométrica de razão `0.5`:
  ```
  Σ (0.5)^n = 1/(1-0.5) = 2 < ∞
  ```

### d) h[n] = 2^n · u[n]

- **Causal:** SIM. `h[n] = 0` para `n < 0`.
- **Estável:** NÃO. Razão `r = 2 ≥ 1`, então a série geométrica diverge:
  ```
  Σ 2^n -> ∞
  ```
  Uma entrada limitada (por exemplo um degrau) produz saída ilimitada — sistema instável.

### Síntese (tabela comparativa)

| Sistema | Causal | Estável | Justificativa principal |
|---------|--------|---------|-------------------------|
| (a) y[n]=x[n]+x[n-1] | Sim | Sim | FIR finito, sem dependência futura |
| (b) y[n]=x[n+1]      | Não | Sim | Antecipa a entrada em uma amostra |
| (c) h[n]=(0.5)^n·u[n]| Sim | Sim | Razão < 1, decaimento exponencial |
| (d) h[n]=2^n·u[n]    | Sim | Não | Razão ≥ 1, crescimento exponencial |

---

## Desafio Proposto - Filtro de Média Móvel em Sinais Ruidosos

### Contexto
Sensores reais (temperatura, tensão, acelerômetros, etc.) frequentemente fornecem leituras contaminadas por ruído eletrônico ou perturbações ambientais de alta frequência. O filtro de média móvel de M pontos, com resposta ao impulso

```
h[n] = (1/M)·{1, 1, ..., 1}   (M coeficientes iguais)
```

é uma das ferramentas mais simples e eficazes para suavizar essas leituras antes de qualquer processamento posterior. A simulação está em [desafio.m](desafio.m).

### Papel da resposta ao impulso

A resposta ao impulso `h[n]` define **completamente** o comportamento do filtro: ao convoluí-la com a entrada, calcula-se em cada instante a média aritmética das `M` amostras mais recentes da entrada. Como `h[n]` tem todos os coeficientes iguais a `1/M`, cada amostra contribui com peso idêntico — daí o nome "média uniforme".

### Por que ocorre a suavização?

1. **Cancelamento estatístico do ruído:** se o ruído for aproximadamente de média nula e amostras consecutivas pouco correlacionadas, ao somar M amostras o ruído tende a `√M` enquanto o sinal de interesse continua com amplitude `M·s`. A relação sinal-ruído melhora aproximadamente por um fator `√M`.
2. **Característica passa-baixas:** o módulo da resposta em frequência do filtro é
   ```
   |H(e^jω)| = |sin(ωM/2) / (M·sin(ω/2))|
   ```
   essa função é máxima em ω = 0 (DC) e atenua progressivamente as altas frequências, onde o ruído rápido se concentra.
3. **Suavização visual:** os gráficos antes/depois mostram redução clara das oscilações de alta frequência, preservando a tendência do sinal.

### Limitações do procedimento

- **Atraso de grupo:** o filtro introduz um atraso de `(M-1)/2` amostras, deslocando o sinal no tempo. Em sistemas em tempo real isso pode ser crítico.
- **Atenuação de altas frequências legítimas:** se o sinal de interesse contiver componentes rápidas (ex.: bordas, transições, picos curtos), elas serão suavizadas junto com o ruído, perdendo informação.
- **Lobos secundários:** a resposta em frequência apresenta lobos laterais relevantes, ou seja, o filtro **não rejeita perfeitamente** as altas frequências; apenas atenua. Para rejeição mais agressiva são necessários filtros FIR projetados (Hamming, Hanning, Blackman, Kaiser) ou IIR (Butterworth, Chebyshev).
- **Efeitos de borda:** as primeiras e últimas amostras filtradas são pouco confiáveis por usarem janelas incompletas (sobre as quais a convolução implicitamente zera os valores fora do intervalo).
- **Compromisso M vs. fidelidade:** M maior reduz mais ruído mas distorce mais o sinal; M menor preserva o sinal mas filtra menos ruído. A escolha de M é um compromisso prático.

---

## Conclusão

Este estudo dirigido consolidou os fundamentos de sistemas LTI discretos: a resposta ao impulso `h[n]` foi apresentada como o "DNA" do sistema, capaz de prever a saída via convolução para qualquer entrada. A análise de causalidade e estabilidade BIBO foi exemplificada através de sistemas FIR (Atividade 6a, 6b) e IIR (Atividade 3, 6c, 6d), mostrando como propriedades algorítmicas se traduzem em comportamento dinâmico. Por fim, o desafio aplicado evidenciou o uso prático da convolução em filtragem digital, que é a base de inúmeras aplicações reais de instrumentação, áudio, controle e telecomunicações.
