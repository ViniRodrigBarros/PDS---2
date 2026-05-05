% =====================================================================
% Desafio - Filtragem de sinal de sensor com filtro de media movel
%
% Cenario: sinal lento (senoide) corrompido por ruido gaussiano rapido.
% Aplicamos filtros de media movel com diferentes comprimentos M e
% comparamos visualmente (e numericamente, via SNR) o resultado.
% =====================================================================

% Reprodutibilidade
rand('state', 42);
randn('state', 42);

% Sinal "verdadeiro" (lento) e ruido (rapido)
N = 200;
n = 0:N-1;
sinal = 5 * sin(2*pi*0.02*n) + 2;        % senoide lenta + nivel DC
ruido = 1.5 * randn(1, N);               % ruido branco gaussiano
x = sinal + ruido;                       % leitura do sensor

% Filtros de media movel com M = 3, 7 e 15
Ms = [3 7 15];
cores = {'r', 'g', 'm'};

figure('Name', 'Desafio - Filtragem com media movel');
hold on;
plot(n, x, 'Color', [0.7 0.7 0.7], 'DisplayName', 'leitura ruidosa');
plot(n, sinal, 'b', 'LineWidth', 1.5, 'DisplayName', 'sinal verdadeiro');

disp('Comparativo: comprimento do filtro x reducao do ruido');
disp('M | RMS do erro (filtrado vs sinal verdadeiro)');
disp('--+-------------------------------------------');
for k = 1:length(Ms)
    M = Ms(k);
    h = (1/M) * ones(1, M);
    y = conv(x, h);

    % Compensar o atraso de grupo (M-1)/2 para alinhamento visual
    atraso = floor((M-1)/2);
    y_alinhado = y(1+atraso : N+atraso);

    erro_rms = sqrt(mean((y_alinhado - sinal).^2));
    fprintf('%d | %.4f\n', M, erro_rms);

    plot(n, y_alinhado, cores{k}, 'LineWidth', 1.2, ...
         'DisplayName', sprintf('media movel M = %d', M));
end

hold off;
grid on;
xlabel('n');
ylabel('amplitude');
title('Desafio: filtragem por media movel (varios M)');
legend('Location', 'best');

disp(' ');
disp('Observacoes:');
disp(' - M maior -> mais suavizacao, mas tambem mais distorcao do sinal lento.');
disp(' - M menor -> preserva detalhes, mas filtra menos ruido.');
disp(' - Em todos os casos ha atraso de grupo (M-1)/2 (compensado no plot).');
disp(' - Limitacoes: lobos secundarios na resposta em frequencia, atenuacao');
disp('   de altas freq. legitimas, efeitos de borda nas extremidades.');
