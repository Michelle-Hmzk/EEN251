from machine import Pin
# 
import time

# Semaforo de carros
vermelho_carro = Pin(11, Pin.OUT)
amarelo_carro = Pin(12, Pin.OUT)
verde_carro = Pin(13, Pin.OUT)

# Semaforo dos pedestres
vermelho_pedestre = Pin(14, Pin.OUT)
verde_pedestre = Pin(15, Pin.OUT)

# Botão inteligente
botao = Pin(2, Pin.IN, Pin.PULL_UP)

# Estados do semaforo
VERDE_CARRO = 0
AMARELO_CARRO = 1
VERMELHO_CARRO = 2

estado_atual = VERDE_CARRO
tempo_estado = time.ticks_ms()
botao_pressionado = False

# Função para desligar todos os LEDs
def apagar_todos():
    vermelho_carro.off()
    amarelo_carro.off()
    verde_carro.off()
    vermelho_pedestre.off()
    verde_pedestre.off()

# Função para acender LEDs conforme o estado
def acender_estado(estado):
    apagar_todos()
    if estado == VERDE_CARRO:
        verde_carro.on()
        vermelho_pedestre.on()
    elif estado == AMARELO_CARRO:
        amarelo_carro.on()
        vermelho_pedestre.on()
    elif estado == VERMELHO_CARRO:
        vermelho_carro.on()
        verde_pedestre.on()

# Função principal
def loop():
    global estado_atual, tempo_estado, botao_pressionado

    while True:
        agora = time.ticks_ms()
        tempo_decorrido = time.ticks_diff(agora, tempo_estado)

        if botao.value() == 0 and not botao_pressionado:
            botao_pressionado = True

        if botao_pressionado and estado_atual == VERDE_CARRO:
            if tempo_decorrido >= 2000:
                estado_atual = AMARELO_CARRO
                acender_estado(estado_atual)
                tempo_estado = time.ticks_ms()
                botao_pressionado = "esperando_vermelho"

        elif botao_pressionado == "esperando_vermelho" and estado_atual == AMARELO_CARRO:
            if tempo_decorrido >= 3000:
                estado_atual = VERMELHO_CARRO
                acender_estado(estado_atual)
                tempo_estado = time.ticks_ms()
                botao_pressionado = False

        elif estado_atual == VERDE_CARRO and tempo_decorrido >= 6000:
            estado_atual = AMARELO_CARRO
            acender_estado(estado_atual)
            tempo_estado = time.ticks_ms()

        elif estado_atual == AMARELO_CARRO and tempo_decorrido >= 3000:
            estado_atual = VERMELHO_CARRO
            acender_estado(estado_atual)
            tempo_estado = time.ticks_ms()

        elif estado_atual == VERMELHO_CARRO and tempo_decorrido >= 5000:
            estado_atual = VERDE_CARRO
            acender_estado(estado_atual)
            tempo_estado = time.ticks_ms()

        time.sleep(0.10)  # Pequeno delay para evitar loop muito rápido

# Iniciar o semáforo
acender_estado(estado_atual)
loop()
