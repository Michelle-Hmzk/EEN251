# Projeto Semáforo "Inteligente" com Raspberry Pi Pico

## Introdução  
O projeto propõe um sistema de semáforo inteligente usando o Raspberry Pi Pico, controlado por código em MicroPython.  
O sistema conta com dois conjuntos de semáforo: um para veículos e outro para pedestres.  
Um botão físico, conectado ao sistema, permite ao pedestre solicitar a travessia. Ao pressioná-lo, o sistema acelera a transição do sinal de veículos para vermelho, ativando o sinal verde para pedestres de forma coordenada e segura.

## Funcionalidades  
- Controle automático do semáforo de veículos com tempos definidos:  
  - Verde: 5 segundos  
  - Amarelo: 3 segundos  
  - Vermelho: 5 segundos  
- Controle sincronizado do semáforo de pedestres conforme o estado do semáforo de veículos  
- Detecção de botão pressionado e resposta dinâmica do sistema  
- Transição mais rápida para vermelho em caso de solicitação de pedestres  
- Retorno automático ao ciclo normal após o atendimento do botão

## Componentes Utilizados  
- Raspberry Pi Pico  
- 5 LEDs (2 vermelhos, 2 verdes, 1 amarelo)  
- 1 botão (conectado ao pino GP2)  
- Resistores 1k Ω  
- Placa para o sistema
- Fios 

## Simulação do Projeto

A montagem e simulação do circuito foram realizadas utilizando a plataforma online [Wokwi](https://wokwi.com/projects/new/pi-pico).


## Requisitos do Sistema

### Requisitos de Hardware
*Obrigatórios:*  
- O sistema deve utilizar um Raspberry Pi Pico como unidade de controle principal.
- Devem ser utilizados cinco LEDs, conectados aos seguintes pinos GPIO:
  - LED vermelho (veículos)
  - LED amarelo (veículos)
  - LED verde (veículos)
  - LED vermelho (pedestres)
  - LED verde (pedestres)
- Deve haver um botão de entrada conectado ao pino, com resistor de pull-up ativado via software.
- Cada LED deve ser protegido com um resistor de 1k Ω, totalizando cinco resistores.

### Requisitos de Software
*Obrigatórios:*
- A aplicação deve ser desenvolvida em MicroPython.
- O firmware do MicroPython deve estar corretamente instalado no Raspberry Pi Pico.
- O controle lógico do semáforo deve ser implementado por meio de uma máquina de estados, com gerenciamento de temporização e tratamento de eventos, como o acionamento do botão de pedestres.

## Autores
Michelle Hamazaki  
RA: 20.00539-3  
foto em <https://github.com/Michelle-Hmzk/EEN251/blob/main/IMG_8130.JPG>
