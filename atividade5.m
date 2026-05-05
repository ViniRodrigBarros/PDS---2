% =====================================================================
% Atividade 5 - Suavizacao de sinais com filtro de media
%
% x[n] = {2, 5, 4, 6, 8, 7, 5, 4}
% h[n] = (1/3) * {1, 1, 1}    (filtro de media simples de 3 pontos)
% =====================================================================

x = [2 5 4 6 8 7 5 4];
h = (1/3) * [1 1 1];

y = conv(x, h);

disp('Sinal original x[n]:');
disp(x);
disp('Filtro h[n] = (1/3)[1 1 1]:');
disp(h);
disp('Sinal suavizado y[n] = x * h:');
disp(y);

% --- Plot 1: sinal original ---
figure('Name', 'Atividade 5 - Sinal original');
stem(0:length(x)-1, x, 'filled');
grid on;
xlabel('n');
ylabel('x[n]');
title('Atividade 5: sinal original do sensor');
ylim([0 9]);

% --- Plot 2: sinal suavizado ---
figure('Name', 'Atividade 5 - Sinal filtrado');
stem(0:length(y)-1, y, 'filled');
grid on;
xlabel('n');
ylabel('y[n]');
title('Atividade 5: sinal suavizado por convolucao com h[n]');
ylim([0 9]);

% --- Plot 3: comparacao sobreposta (original x filtrado) ---
figure('Name', 'Atividade 5 - Comparacao');
hold on;
stem(0:length(x)-1, x, 'b', 'filled', 'DisplayName', 'x[n] original');
stem(0:length(y)-1, y, 'r', 'filled', 'DisplayName', 'y[n] filtrado');
hold off;
grid on;
xlabel('n');
ylabel('amplitude');
title('Atividade 5: comparacao original x suavizado');
legend('Location', 'best');

disp(' ');
disp('Observacoes:');
disp(' - Valores intermediarios de y[n] correspondem a media de 3 amostras consecutivas de x.');
disp(' - Valores das bordas (y[0], y[8], y[9]) sao reduzidos por efeito de borda da convolucao linear.');
disp(' - O filtro atua como passa-baixas: atenua oscilacoes rapidas, preserva tendencia.');
