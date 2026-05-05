% =====================================================================
% Atividade 2 - Calculo manual de convolucao (verificacao numerica)
%
% x[n] = {1, 2, 1}
% h[n] = {1, 1}
%
% Resultado esperado (manual): y[n] = {1, 3, 3, 1}
% =====================================================================

x = [1 2 1];
h = [1 1];

% --- Convolucao "passo a passo" implementada na mao ---
N = length(x);
M = length(h);
L = N + M - 1;
y_manual = zeros(1, L);

for n = 1:L
    soma = 0;
    for k = 1:N
        idx = n - k + 1;          % equivalente a (n-k) na formulacao 0-indexed
        if idx >= 1 && idx <= M
            soma = soma + x(k) * h(idx);
        end
    end
    y_manual(n) = soma;
end

% --- Convolucao usando comando nativo ---
y_conv = conv(x, h);

disp('Sequencia x[n]:');
disp(x);
disp('Sequencia h[n]:');
disp(h);
disp('y[n] calculada manualmente (loop):');
disp(y_manual);
disp('y[n] via conv():');
disp(y_conv);

if isequal(y_manual, y_conv)
    disp('OK: resultado manual coincide com conv() -> {1, 3, 3, 1}');
else
    disp('ATENCAO: divergencia entre calculo manual e conv()');
end

% --- Visualizacao ---
n = 0:length(y_conv)-1;
figure('Name', 'Atividade 2 - Convolucao manual');
stem(n, y_conv, 'filled');
grid on;
xlabel('n');
ylabel('y[n]');
title('Atividade 2: y[n] = x[n] * h[n] = {1, 3, 3, 1}');
