% =====================================================================
% Atividade 4 - Implementacao computacional da convolucao
%
% 1) Reproduz a Atividade 2 com conv().
% 2) Modifica a entrada para x = {1, 1, 1, 1} e interpreta o resultado.
% =====================================================================

% --- Caso 1: replicacao da Atividade 2 ---
x1 = [1 2 1];
h  = [1 1];
y1 = conv(x1, h);

disp('--- Caso 1: x = [1 2 1], h = [1 1] ---');
disp('Sequencia x[n]:');
disp(x1);
disp('Sequencia h[n]:');
disp(h);
disp('Convolucao y[n] = x[n] * h[n]:');
disp(y1);

n1 = 0:length(y1)-1;
figure('Name', 'Atividade 4 - Caso 1');
stem(n1, y1, 'filled');
grid on;
xlabel('n');
ylabel('y[n]');
title('Atividade 4 (caso 1): y[n] = x * h = [1 3 3 1]');

% --- Caso 2: x = {1, 1, 1, 1} ---
x2 = [1 1 1 1];
y2 = conv(x2, h);

disp(' ');
disp('--- Caso 2: x = [1 1 1 1], h = [1 1] ---');
disp('Sequencia x[n]:');
disp(x2);
disp('Convolucao y[n]:');
disp(y2);
disp('Forma trapezoidal: subida (1), patamar de soma maxima (2 2 2), descida (1).');
disp('Patamar central = soma da janela h sobre amostras inteiramente sobrepostas.');

n2 = 0:length(y2)-1;
figure('Name', 'Atividade 4 - Caso 2');
stem(n2, y2, 'filled');
grid on;
xlabel('n');
ylabel('y[n]');
title('Atividade 4 (caso 2): y[n] = [1 2 2 2 1] (perfil trapezoidal)');
