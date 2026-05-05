% =====================================================================
% Atividade 3 - Sistema descrito por equacao de diferencas
%
% y[n] = 0.8 * y[n-1] + x[n], com y[-1] = 0 e x[n] = delta[n].
%
% Objetivos:
%   1) Calcular h[n] para 0 <= n <= 5 via recursao.
%   2) Discutir estabilidade BIBO (somabilidade absoluta de h).
%   3) Verificar causalidade.
% =====================================================================

a = 0.8;
N = 6;                     % calcular h[0]..h[5]

% Entrada impulso e saida via recursao da equacao de diferencas
x = zeros(1, N);
x(1) = 1;                  % delta[n] -> x(1) corresponde a n = 0

h = zeros(1, N);
y_anterior = 0;            % condicao inicial y[-1] = 0
for n = 1:N
    h(n) = a * y_anterior + x(n);
    y_anterior = h(n);
end

% Forma fechada para comparacao: h[n] = (0.8)^n * u[n]
n_vec = 0:N-1;
h_fechada = a .^ n_vec;

disp('h[n] obtido pela recursao (n = 0..5):');
disp(h);
disp('h[n] pela forma fechada (0.8)^n:');
disp(h_fechada);

% --- Estabilidade BIBO ---
% Soma da serie geometrica completa: 1 / (1 - a) com |a| < 1
soma_truncada = sum(abs(h));
soma_total = 1 / (1 - a);
fprintf('Soma |h[n]| (n = 0..5)  : %.4f\n', soma_truncada);
fprintf('Soma total |h[n]| (n>=0): %.4f\n', soma_total);
disp('Como a soma e finita -> sistema ESTAVEL no sentido BIBO.');

% --- Causalidade ---
disp('h[n] = 0 para n < 0 (forma fechada usa u[n]) -> sistema CAUSAL.');

% --- Visualizacao ---
n_plot = 0:25;
h_plot = a .^ n_plot;
figure('Name', 'Atividade 3 - Resposta ao impulso');
stem(n_plot, h_plot, 'filled');
grid on;
xlabel('n');
ylabel('h[n]');
title('Atividade 3: h[n] = (0.8)^n u[n] - decaimento exponencial');
