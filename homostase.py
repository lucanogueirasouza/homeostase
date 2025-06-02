from time import sleep 
from random import uniform

# faixa ideal de temperatura (simulando a faixa corporal)
TEMP_MIN = 35
TEMP_MAX = 38

# temperatura inicial do sistema (temp. corporal)

def aquecer(temperatura): # aquecer sistema corporal, caso sua temp.
    # seja inferior a temp. min
    print("🧊 Temperatura baixa! Aquecendo.")
    return temperatura + 0.5

def esfriar(temperatura): # resfriar sistema corporal, caso a temp.
    # seja superior a temp. max
    print("🔥 Temperatura alta! Resfriando.")
    return temperatura - 0.5

def manter(temperatura): # caso a temperatura esteja na faixa
    # adequada, a temp seja mantida
    print("👍 Temperatura normal. Estado mantido...")
    return temperatura

def simular_homeostase():
    temperatura = 36.5 # temperatura inicial do corpo
    contador = 0       

    while contador < 10:  # 10 ciclos de simulacao do corpo em contato
        # com o ambiente
        contador += 1
        interferencia = uniform(-1.0, 1.0)
        temperatura += interferencia

        print(f"\n🕛 Ciclo {contador} | Temperatura atual: {temperatura:.2f}°C")

        if temperatura < TEMP_MIN: 
            temperatura = aquecer(temperatura)
        elif temperatura > TEMP_MAX:
            temperatura = esfriar(temperatura) # homeostase atuando para deixar o corpo em sua temperatura permitida
        else:
            temperatura = manter(temperatura)
        sleep(1)

simular_homeostase() # inicia o processo
