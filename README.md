# Simulador de Homeostase Térmica  
Simulação de regulação automática da temperatura corporal frente a interferências externas.

## Português

Simulador criado utilizando apenas **Python**.  
Funcionalidades:
- Faixa ideal de temperatura entre **35 °C e 38 °C**.
- A cada ciclo, uma **interferência ambiental aleatória** afeta a temperatura do corpo.
- Mecanismos de autorregulação:
  - `aquecer()` → aumenta a temperatura em **+0,5 °C** se estiver abaixo de 35 °C;
  - `esfriar()` → reduz a temperatura em **–0,5 °C** se estiver acima de 38 °C;
  - `manter()` → mantém a temperatura caso esteja entre 35 °C e 38 °C.
- Simulação em **10 ciclos** com pausa de **1 segundo** entre cada etapa.
- Exibição de mensagens e temperatura no terminal a cada ciclo.
!!CÓDIGO FEITO PARA APRENSENTAÇÃO DE ATIVIDADE CURRICULAR DO CURSO DE DESENVOLVIMENTO DE SISTEMAS EM MINHA ESCOLA!!

## English

Simulator created using only **Python**.  
Functionalities:
- Ideal temperature range between **35 °C and 38 °C**.
- Each cycle simulates an **external disturbance** affecting the body temperature.
- Self-regulation mechanisms:
  - `aquecer()` → increases temperature by **+0.5 °C** if below 35 °C;
  - `esfriar()` → decreases temperature by **–0.5 °C** if above 38 °C;
  - `manter()` → keeps the temperature if within the ideal range.
- **10-cycle simulation** with **1-second delay** between each cycle.
- Terminal output shows cycle number and current body temperature.
!!CODE MADE FOR LEARNING CURRICULAR ACTIVITY OF SYSTEMS DEVELOPMENT COURSE IN MY SCHOOL!!
