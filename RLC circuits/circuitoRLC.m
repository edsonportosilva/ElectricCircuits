% Códigos para análise de resposta natural e ao degrau de circuitos RLC 
%
% clique na seção demarcada por %% e pressione CTRL+ENTER para rodar o caso de
% interesse
%
% Autor: Edson Porto da Silva
% Última Atualização: 08/10/2019
%
%% Caso1: Circuito RLC paralelo (resposta natural)

clear all 
close all

% parâmetros do circuito:
R  = 2e3;          % resistência
L  = 50e-3;        % indutância
C  = 0.2e-6;       % capacitância
V0 = 12;           % tensão inicial no capacitor
I0 = 90e-3;        % corrente inicial no indutor

w0    = 1/sqrt(L*C);  % frequência angular de ressonância
alpha = 1/(2*R*C);    % frequência de Neper

t = [0:0.0001:40]*1/w0; % discretização do intervalo de tempo 

% raízes da equação característica:
s1 = -alpha+sqrt(alpha^2-w0^2);
s2 = -alpha-sqrt(alpha^2-w0^2);

% coeficientes A1 e A2 da solução geral:
A = [1 1; s1 s2]\[V0; (-V0/R-I0)/C];

% solução da resposta natural  para v(t) 
% (tensão aplicada aos elementos do circuito):
v = A(1)*exp(s1*t)+A(2)*exp(s2*t);

v = real(v); % Caso o MATLAB retorne uma variável complexa com a parte imaginária muito pequena.

% cálculo das correntes a partir de v(t):
iL = 1/L*cumtrapz(t, v)+I0;             % corrente no indutor
iR = v/R;                               % corrente no resistor
iC = [-iR(1)-iL(1) C*diff(v)./diff(t)]; % corrente no capacitor

% plot das curvas:
figure, plot(t, real(v), 'k-', 'linewidth',1.5);
grid on; xlabel('tempo (s)')
ylabel ('v(t) (V)')
legend('v(t)')
title('Tensão circuito RLC em paralelo');

figure, plot(t, iL/1e-3, 'k', 'linewidth',1.5);
hold on, plot(t, iC/1e-3, 'r', 'linewidth',1.5);
plot(t, iR/1e-3, 'b', 'linewidth',1.5);
plot(t, (iR + iL + iC)/1e-3, 'g', 'linewidth',1.5);
grid on; xlabel('tempo (s)')
ylabel ('corrente (mA)')
legend('i_L(t)','i_C(t)','i_R(t)', 'i_L(t)+i_C(t)+i_R(t)')
title('Correntes circuito RLC em paralelo');

energiaL = (0.5*L*iL.^2)/1e-3;         % energia armazenada no indutor em função do tempo em mJ
energiaC = (0.5*C*v.^2)/1e-3;          % energia armazenada no capacitor em função do tempo em mJ
energiaR = cumtrapz(t, v.*iR)/1e-3;    % energia dissipada pelo resistor em função do tempo em mJ
figure, plot(t, energiaL, 'k', 'linewidth',1.5);
hold on, plot(t, energiaC, 'r', 'linewidth',1.5);
plot(t, energiaR, 'b', 'linewidth',1.5);
plot(t, energiaL + energiaC + energiaR, 'g', 'linewidth',1.5);
grid on; xlabel('tempo (s)')
ylabel ('Energia (mJ)')
legend('w_L(t)','w_C(t)', 'w_R(t)', 'w_L(t) + w_C(t) + w_R(t)');
title('Energia no circuito RLC em paralelo');


%% Caso2: Circuito RLC paralelo (resposta ao degrau)
clear all
close all

% parâmetros do circuito:
R = 1250;             % resistência
L = 640e-3;           % indutância
C = 6.25e-6;          % capacitância
V0 = 10;              % tensão inicial no capacitor
I0 = 50e-3;           % corrente inicial no indutor
Is = 0.2;             % valor da fonte de corrente
w0    = 1/sqrt(L*C);  % frequência angular de ressonância
alpha = 1/(2*R*C);    % frequência de Neper

t = [0.001, 0:0.0025:80]*1/w0; % discretização do intervalo de tempo

% raízes da equação característica:
s1 = -alpha+sqrt(alpha^2-w0^2);
s2 = -alpha-sqrt(alpha^2-w0^2);

% coeficientes A1 e A2 da solução geral:
A = [1 1; s1 s2]\[I0-Is; V0/L];

% solução da resposta natural  para v(t) 
% (tensão aplicada aos elementos do circuito):
iL = Is + A(1)*exp(s1*t)+A(2)*exp(s2*t);

iL = real(iL); % Caso o MATLAB retorne uma variável complexa com a parte imaginária muito pequena.

% cálculo das correntes a partir de v(t):
vL = [V0 L*diff(iL)./diff(t)];  % corrente no indutor (v = Ldi/dt)
iR = vL/R;                       % corrente no resistor (v = Ri)
iC = Is-iL-iR;                   % corrente no capacitor (LKC)
v = vL;

% cálculo das energias fornecidas e consumidas no circuito:
energiaL     = (0.5*L*iL.^2)/1e-3;      % energia armazenada no indutor em função do tempo em mJ
energiaC     = (0.5*C*v.^2)/1e-3;       % energia armazenada no capacitor em função do tempo em mJ
energiaR     = cumtrapz(t, v.*iR)/1e-3; % energia dissipada pelo resistor em função do tempo em mJ
energiaFonte = cumtrapz(t, v*Is)/1e-3;  % energia fornecida pela fonte de corrente em função do tempo em mJ
energiaInicial = (0.5*L*I0.^2+0.5*C*V0.^2)/1e-3; % energia inicial armazenada no circuito em mJ

% plot das curvas:
figure, plot(t, v, 'k-', 'linewidth',1.5);
grid on; xlabel('tempo (s)')
ylabel ('v(t) (V)')
legend('v(t)')
title('Tensão circuito RLC em paralelo');

figure, plot(t, iL, 'k', 'linewidth',1.5);
hold on, plot(t, iC, 'r', 'linewidth',1.5);
plot(t, iR, 'b', 'linewidth',1.5);
plot(t, iR+iL+iC, 'g', 'linewidth',1.5);
grid on; xlabel('tempo (s)')
ylabel ('corrente (A)')
legend('i_L(t)','i_C(t)','i_R(t)','i_L(t) + i_C(t) + i_R(t)')
title('Correntes circuito RLC em paralelo');

figure, plot(t, energiaL, 'k', 'linewidth',1.5);
hold on, plot(t, energiaC, 'r', 'linewidth',1.5);
plot(t, energiaR, 'b', 'linewidth',1.5);
plot(t, energiaFonte, 'linewidth',1.5);
plot(t, energiaL + energiaC + energiaR - energiaInicial, 'g--', 'linewidth',1.5);
grid on; xlabel('tempo (s)')
ylabel ('Energia (mJ)')
legend('w_L(t)','w_C(t)', 'w_R(t)', 'w_S(t)','w_L(t) + w_C(t) + w_R(t) - w_0');
title('Energia no circuito RLC em paralelo');


%% Caso3: Circuito RLC série (resposta natural)
clear all 
close all

% parâmetros do circuito:
R  = 0;          % resistência
L  = 100e-3;        % indutância
C  = 0.1e-6;       % capacitância
V0 = -100;           % tensão inicial no capacitor
I0 = 0;        % corrente inicial no indutor

w0    = 1/sqrt(L*C);  % frequência angular de ressonância
alpha = R/(2*L);      % frequência de Neper

t = [0:0.0001:40]*1/w0; % discretização do intervalo de tempo 

% raízes da equação característica:
s1 = -alpha+sqrt(alpha^2-w0^2);
s2 = -alpha-sqrt(alpha^2-w0^2);

% coeficientes A1 e A2 da solução geral:
A = [1 1; s1 s2]\[I0; (-R*I0-V0)/L];

% solução da resposta natural  para i(t) 
% (corrente passando pelos elementos do circuito):
i = A(1)*exp(s1*t)+A(2)*exp(s2*t);

i = real(i); % Caso o MATLAB retorne uma variável complexa com a parte imaginária muito pequena.

% cálculo das correntes a partir de v(t):
vC = 1/C*cumtrapz(t, i)+V0;             % tensão no indutor
vR = R*i;                               % tensão no resistor
vL = [-I0*R-V0 L*diff(i)./diff(t)];     % tensão no capacitor

% plot das curvas:
figure, plot(t, i/1e-3, 'k-', 'linewidth',1.5);
grid on; xlabel('tempo (s)')
ylabel ('i(t) (mA)')
legend('i(t)')
title('Corrente circuito RLC em série');

figure, plot(t, vL, 'k', 'linewidth',1.5);
hold on, plot(t, vC, 'r', 'linewidth',1.5);
plot(t, vR, 'b', 'linewidth',1.5);
plot(t, (vR + vL + vC), 'g', 'linewidth',1.5);
grid on; xlabel('tempo (s)')
ylabel ('tensão (V)')
legend('v_L(t)','v_C(t)','v_R(t)', 'v_L(t)+v_C(t)+v_R(t)')
title('Tensões circuito RLC em série');

energiaL = (0.5*L*i.^2)/1e-3;         % energia armazenada no indutor em função do tempo em mJ
energiaC = (0.5*C*vC.^2)/1e-3;          % energia armazenada no capacitor em função do tempo em mJ
energiaR = cumtrapz(t, vR.*i)/1e-3;    % energia dissipada pelo resistor em função do tempo em mJ
figure, plot(t, energiaL, 'k', 'linewidth',1.5);
hold on, plot(t, energiaC, 'r', 'linewidth',1.5);
plot(t, energiaR, 'b', 'linewidth',1.5);
plot(t, energiaL + energiaC + energiaR, 'g', 'linewidth',1.5);
grid on; xlabel('tempo (s)')
ylabel ('Energia (mJ)')
legend('w_L(t)','w_C(t)', 'w_R(t)', 'w_L(t) + w_C(t) + w_R(t)');
title('Energia no circuito RLC em série');

%% Caso4: Circuito RLC série (resposta ao degrau)
clear all 
close all

% parâmetros do circuito:
R  = 10;          % resistência
L  = 100e-3;        % indutância
C  = 2e-3;       % capacitância
V0 = -90;           % tensão inicial no capacitor
I0 = -5;        % corrente inicial no indutor
Vs = 60;           % valor da fonte de tensão
w0    = 1/sqrt(L*C);  % frequência angular de ressonância
alpha = R/(2*L);      % frequência de Neper

t = [0:0.001:40]*1/w0; % discretização do intervalo de tempo 

% raízes da equação característica:
s1 = -alpha+sqrt(alpha^2-w0^2);
s2 = -alpha-sqrt(alpha^2-w0^2);

% coeficientes A1 e A2 da solução geral:
A = [1 1; s1 s2]\[V0-Vs; I0/C];

% solução da resposta ao degrau para vc(t) 
% (tensão nos terminais do capacitor):
vC = Vs + A(1)*exp(s1*t)+A(2)*exp(s2*t);

vC = real(vC); % Caso o MATLAB retorne uma variável complexa com a parte imaginária muito pequena.

% cálculo das tensões e da corrente partir de vc(t):
i  = [I0 C*diff(vC)./diff(t)];    % corrente no circuito
vR = R*i;                         % tensão no resistor
vL = Vs-vR-vC;                    % tensão no indutor(LKT)

% cálculo das energias fornecidas e consumidas no circuito:
energiaL     = (0.5*L*i.^2)/1e-3;        % energia armazenada no indutor em função do tempo em mJ
energiaC     = (0.5*C*vC.^2)/1e-3;       % energia armazenada no capacitor em função do tempo em mJ
energiaR     = cumtrapz(t, vR.*i)/1e-3;  % energia total dissipada pelo resistor em função do tempo em mJ
energiaFonte = cumtrapz(t, Vs.*i)/1e-3;          % energia fornecida pela fonte de corrente em função do tempo em mJ
energiaInicial = (0.5*L*I0.^2+0.5*C*V0.^2)/1e-3; % energia inicial armazenada no circuito em mJ

% plot das curvas:
figure, plot(t, i/1e-3, 'k-', 'linewidth',1.5);
grid on; xlabel('tempo (s)')
ylabel ('i(t) (mA)')
legend('i(t)')
title('Corrente circuito RLC em série');

figure, plot(t, vL, 'k', 'linewidth',1.5);
hold on, plot(t, vC, 'r', 'linewidth',1.5);
plot(t, vR, 'b', 'linewidth',1.5);
plot(t, (vR + vL + vC), 'g', 'linewidth',1.5);
grid on; xlabel('tempo (s)')
ylabel ('tensão (V)')
legend('v_L(t)','v_C(t)','v_R(t)', 'v_L(t)+v_C(t)+v_R(t)')
title('Tensões circuito RLC em série');

figure, plot(t, energiaL, 'k', 'linewidth',1.5);
hold on, plot(t, energiaC, 'r', 'linewidth',1.5);
plot(t, energiaR, 'b', 'linewidth',1.5);
plot(t, energiaFonte, 'linewidth',1.5);
plot(t, energiaL + energiaC + energiaR - energiaInicial, 'g--', 'linewidth',1.5);
grid on; xlabel('tempo (s)')
ylabel ('Energia (mJ)')
legend('w_L(t)','w_C(t)', 'w_R(t)', 'w_S(t)','w_L(t) + w_C(t) + w_R(t) - w_0');
title('Energia no circuito RLC em série');



%% Caso5: Circuito RLC série (resposta a uma onda quadrada)
clear  
close all

% parâmetros do circuito:
R  = 600;         % resistência [ohms]
L  = 50e-3;       % indutância  [henrys]
C  = 0.2e-6;      % capacitância [farads]
V0 = 0;           % tensão inicial no capacitor [volts]
I0 = 0;           % corrente inicial no indutor [ampères]
fq = 500;         % frequência da onda quadrada [hertz]
Vq = 15;          % amplitude da onda quadrada [volts]
w0 = 1/sqrt(L*C); % frequência angular de ressonância [rad/segundo]

t  = [0:0.01:100]*1/w0;   % discretização do intervalo de tempo [segundos]

Vs = Vq*square(2*pi*fq*t);    % onda quadrada na entrada do circuito
% Vs = Vq*sawtooth(2*pi*fq*t);  % onda triangular na entrada do circuito
% Vs = Vq*diric(2*pi*fq*t, 16); % trem de sincs

vC    = nan(1,length(t));
x     = nan(1,length(t));

% EDO da tensão sobre o capacitor: vc''(t)+(R/L)vc'(t)+vc(t)/LC = vs/LC

% Solução numérica:
vC(1) = V0;       % condição incial de vc
x(1)  = I0/C;     % condição inicial da derivada vc'(t)

% Integração numérica via método de Euler:
deltaT = t(2)-t(1); % passo de integração
for kk = 1:length(t)-1
    vC(kk+1) = vC(kk)+x(kk)*deltaT;                                 % calcula vc(t+deltaT)
    x(kk+1)  = x(kk)+(-R/L*x(kk)-1/(L*C)*(vC(kk)-Vs(kk)))*deltaT;   % calcula vc'(t+deltaT)
end

% cálculo das tensões e da corrente partir de vc(t):
i  = [I0 C*diff(vC)./diff(t)];    % corrente no circuito
vR = R*i;                         % tensão no resistor
vL = Vs-vR-vC;                    % tensão no indutor(LKT)

% cálculo das potências fornecidas e consumidas por cada elemento do circuito:
PL = vL.*i;  % indutor
PC = vC.*i;  % capacitor
PR = vR.*i;  % resistor
PS = Vs.*i;  % fonte de alimentação

% cálculo das energias fornecidas e consumidas no circuito:
energiaL     = cumtrapz(t, PL)/1e-3;  % energia total consumida pelo indutor em função do tempo em mJ
energiaC     = cumtrapz(t, PC)/1e-3;  % energia total consumida pelo capacitor em função do tempo em mJ 
energiaR     = cumtrapz(t, PR)/1e-3;  % energia total consumida pelo resistor em função do tempo em mJ
energiaFonte = cumtrapz(t, PS)/1e-3;  % energia total fornecida pela fonte de corrente em função do tempo em mJ 

% plot das curvas:
figure, plot(t, i/1e-3, 'k-', 'linewidth',1.5);
grid on; xlabel('tempo (s)')
ylabel ('i(t) (mA)')
legend('i(t)')
title('Corrente circuito RLC em série');

figure, plot(t, vL, 'k', 'linewidth',1.5);
hold on, plot(t, vC, 'r', 'linewidth',1.5);
plot(t, vR, 'b', 'linewidth',1.5);
plot(t, (vR + vL + vC), 'g', 'linewidth',1.5);
plot(t, Vs, 'k--', 'linewidth',1.5);
grid on; xlabel('tempo (s)')
ylabel ('tensão (V)')
legend('v_L(t)','v_C(t)','v_R(t)', 'v_L(t)+v_C(t)+v_R(t)', 'V_s(t)')
title('Tensões circuito RLC em série');

figure, plot(t, energiaL, 'k', 'linewidth',1.5);
hold on, plot(t, energiaC, 'r', 'linewidth',1.5);
plot(t, energiaR, 'b', 'linewidth',1.5);
plot(t, energiaFonte, 'linewidth',1.5);
plot(t, energiaL + energiaC + energiaR - energiaFonte, 'g--', 'linewidth',1.5);
grid on; xlabel('tempo (s)')
ylabel ('Energia (mJ)')
legend('w_L(t)','w_C(t)', 'w_R(t)', 'w_S(t)','w_L(t) + w_C(t) + w_R(t) - w_S(t)');
title('Energia no circuito RLC em série');

figure, plot(t, PL, 'k', 'linewidth',1.5);
hold on, plot(t, PC, 'r', 'linewidth',1.5);
plot(t, PR, 'b', 'linewidth',1.5);
plot(t, PS, 'linewidth',1.5);
plot(t, PL+PR+PC-PS, 'g--', 'linewidth',1.5);
grid on; xlabel('tempo (s)')
ylabel ('potência (W)')
legend('P_L(t)','P_C(t)', 'P_R(t)', 'P_S(t)','P_L(t) + P_C(t) + P_R(t) - P_S(t)');
title('Potência no circuito RLC em série');

%% Caso6: Circuito RLC série (resposta a uma fonte de impulsos)

clear  
close all

% parâmetros do circuito:
R  = 500;          % resistência [ohms]
L  = 50e-3;       % indutância  [henrys]
C  = 0.2e-6;      % capacitância [farads]
V0 = 0;           % tensão inicial no capacitor [volts]
I0 = 0;           % corrente inicial no indutor [ampère]
fq = 500;         % frequência da onda quadrada [hertz]
Vq = 15;          % amplitude da onda quadrada [volts]
w0 = 1/sqrt(L*C); % frequência angular de ressonância [rad/segundo]

t  = [0:0.001:200]*1/w0;   % discretização do intervalo de tempo [segundos]

Vs = Vq*diric(2*pi*fq*t, 400); 
Vs = abs(Vs)>0.8*Vq;          % trem de impulsos

vC    = nan(1,length(t));
x     = nan(1,length(t));

% EDO da tensão sobre o capacitor: vc''(t)+(R/L)vc'(t)+vc(t)/LC = vs/LC

% Solução numérica:
vC(1) = V0;       % condição incial de vc
x(1)  = I0/C;     % condição inicial da derivada vc'(t)

% Integração numérica via método de Euler:
deltaT = t(2)-t(1); % passo de integração
for kk = 1:length(t)-1
    vC(kk+1) = vC(kk) + x(kk)*deltaT;                                 % calcula vc(t+deltaT)
    x(kk+1)  = x(kk) + (-R/L*x(kk)-1/(L*C)*(vC(kk)-Vs(kk)))*deltaT;   % calcula vc'(t+deltaT)
end

% cálculo das tensões e da corrente partir de vc(t):
i  = [I0 C*diff(vC)./diff(t)];    % corrente no circuito
vR = R*i;                         % tensão no resistor
vL = Vs-vR-vC;                    % tensão no indutor(LKT)

% cálculo das potências fornecidas e consumidas por cada elemento do circuito:
PL = vL.*i;  % indutor
PC = vC.*i;  % capacitor
PR = vR.*i;  % resistor
PS = Vs.*i;  % fonte de alimentação

% cálculo das energias fornecidas e consumidas no circuito:
energiaL     = cumtrapz(t, PL)/1e-3;  % energia total consumida pelo indutor em função do tempo em mJ
energiaC     = cumtrapz(t, PC)/1e-3;  % energia total consumida pelo capacitor em função do tempo em mJ 
energiaR     = cumtrapz(t, PR)/1e-3;  % energia total consumida pelo resistor em função do tempo em mJ
energiaFonte = cumtrapz(t, PS)/1e-3;  % energia total fornecida pela fonte de corrente em função do tempo em mJ 

% plot das curvas:
figure, plot(t, i/1e-3, 'k-', 'linewidth',1.5);
grid on; xlabel('tempo (s)')
ylabel ('i(t) (mA)')
legend('i(t)')
title('Corrente circuito RLC em série');

figure, plot(t, vL, 'k', 'linewidth',1.5);
hold on, plot(t, vC, 'r', 'linewidth',1.5);
plot(t, vR, 'b', 'linewidth',1.5);
plot(t, (vR + vL + vC), 'g', 'linewidth',1.5);
plot(t, Vs, 'k--', 'linewidth',1.5);
grid on; xlabel('tempo (s)')
ylabel ('tensão (V)')
legend('v_L(t)','v_C(t)','v_R(t)', 'v_L(t)+v_C(t)+v_R(t)', 'V_s(t)')
title('Tensões circuito RLC em série');

figure, plot(t, energiaL, 'k', 'linewidth',1.5);
hold on, plot(t, energiaC, 'r', 'linewidth',1.5);
plot(t, energiaR, 'b', 'linewidth',1.5);
plot(t, energiaFonte, 'linewidth',1.5);
plot(t, energiaL + energiaC + energiaR - energiaFonte, 'g--', 'linewidth',1.5);
grid on; xlabel('tempo (s)')
ylabel ('Energia (mJ)')
legend('w_L(t)','w_C(t)', 'w_R(t)', 'w_S(t)','w_L(t) + w_C(t) + w_R(t) - w_S(t)');
title('Energia no circuito RLC em série');

figure, plot(t, PL, 'k', 'linewidth',1.5);
hold on, plot(t, PC, 'r', 'linewidth',1.5);
plot(t, PR, 'b', 'linewidth',1.5);
plot(t, PS, 'linewidth',1.5);
plot(t, PL+PR+PC-PS, 'g--', 'linewidth',1.5);
grid on; xlabel('tempo (s)')
ylabel ('potência (W)')
legend('P_L(t)','P_C(t)', 'P_R(t)', 'P_S(t)','P_L(t) + P_C(t) + P_R(t) - P_S(t)');
title('Potência no circuito RLC em série');
