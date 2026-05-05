% =====================================================================
% Estudo Dirigido - Parte 2: Convolucao e Sistemas LTI
% Disciplina: Processamento Digital de Sinais
% Professor:  Moacy Pereira da Silva
% IFPB - Campus Campina Grande
%
% Script mestre: executa todas as atividades em sequencia.
% =====================================================================

clc;
clear;
close all;

disp('=====================================================');
disp('  ESTUDO DIRIGIDO - PARTE 2 - CONVOLUCAO E LTI');
disp('=====================================================');

disp(' ');
disp('>>> Atividade 2 - Convolucao manual verificada <<<');
atividade2;

disp(' ');
disp('>>> Atividade 3 - Resposta ao impulso (eq. de diferencas) <<<');
atividade3;

disp(' ');
disp('>>> Atividade 4 - Convolucao com comando conv() <<<');
atividade4;

disp(' ');
disp('>>> Atividade 5 - Suavizacao com filtro de media <<<');
atividade5;

disp(' ');
disp('>>> Atividade 6 - Estabilidade e causalidade <<<');
atividade6;

disp(' ');
disp('>>> Desafio - Filtro de media movel em sinal ruidoso <<<');
desafio;

disp(' ');
disp('=====================================================');
disp('  Execucao concluida.');
disp('=====================================================');

% Mantem as figuras abertas quando o script e executado pela linha de
% comando (ex.: "octave main.m"). Sem isso, o processo termina e fecha
% todas as janelas. Dentro do GUI do Octave essa pausa nao atrapalha.
input('Pressione ENTER para fechar as figuras e sair...', 's');
close all;
