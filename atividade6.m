% =====================================================================
% Atividade 6 - Analise de estabilidade e causalidade
%
% Sistemas:
%   a) y[n] = x[n] + x[n-1]            (FIR de 2 amostras)
%   b) y[n] = x[n+1]                   (antecipa a entrada)
%   c) h[n] = (0.5)^n * u[n]           (IIR estavel)
%   d) h[n] = 2^n * u[n]               (IIR instavel)
%
% Para cada caso, gera h[n] e verifica numericamente:
%   - causalidade: h[n] = 0 para n < 0 ?
%   - estabilidade: soma |h[n]| finita ?
% =====================================================================

% Vetor de tempo amplo (cobre n negativo e positivo)
n = -5:25;
N = length(n);

% ---------- (a) y[n] = x[n] + x[n-1] ----------
% h[n] = delta[n] + delta[n-1]
ha = zeros(1, N);
ha(n == 0)  = 1;
ha(n == 1)  = 1;

% ---------- (b) y[n] = x[n+1] ----------
% h[n] = delta[n+1]
hb = zeros(1, N);
hb(n == -1) = 1;

% ---------- (c) h[n] = (0.5)^n u[n] ----------
hc = zeros(1, N);
mask = n >= 0;
hc(mask) = 0.5 .^ n(mask);

% ---------- (d) h[n] = 2^n u[n] ----------
hd = zeros(1, N);
hd(mask) = 2 .^ n(mask);

% ---------- Funcao de avaliacao ----------
nomes  = {'(a) x[n]+x[n-1]', '(b) x[n+1]', '(c) (0.5)^n u[n]', '(d) 2^n u[n]'};
sistemas = {ha, hb, hc, hd};

disp('Sistema                | Causal | Estavel | Soma |h[n]|');
disp('-----------------------+--------+---------+----------------');
for k = 1:length(sistemas)
    h = sistemas{k};
    causal = all(h(n < 0) == 0);
    soma = sum(abs(h));
    estavel = soma < 1e6;            % limite numerico para considerar finito

    if causal,  c = 'SIM   '; else, c = 'NAO   '; end
    if estavel, e = 'SIM    '; else, e = 'NAO    '; end
    fprintf('%-22s | %s | %s | %g\n', nomes{k}, c, e, soma);
end

disp(' ');
disp('Observacao: o sistema (d) cresce ilimitadamente -> a soma diverge.');
disp('Numericamente, sum(2^n) cresce explosivamente (>> 1e6).');

% ---------- Visualizacao ----------
figure('Name', 'Atividade 6 - Respostas ao impulso');

subplot(2,2,1);
stem(n, ha, 'filled'); grid on;
title('(a) h[n] = delta[n] + delta[n-1] -- causal, estavel');
xlabel('n'); ylabel('h[n]');

subplot(2,2,2);
stem(n, hb, 'filled'); grid on;
title('(b) h[n] = delta[n+1] -- NAO causal, estavel');
xlabel('n'); ylabel('h[n]');

subplot(2,2,3);
stem(n, hc, 'filled'); grid on;
title('(c) h[n] = (0.5)^n u[n] -- causal, estavel');
xlabel('n'); ylabel('h[n]');

subplot(2,2,4);
stem(n, hd, 'filled'); grid on;
title('(d) h[n] = 2^n u[n] -- causal, INSTAVEL');
xlabel('n'); ylabel('h[n]');
