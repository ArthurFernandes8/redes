import sounddevice as sd
from funcoes import *

output_device = 0
input_device = 0
sd.default.device = (input_device, output_device)

SAMPLE_RATE = 44100  # Taxa de amostragem do audio
BIT_DURATION = 1.0   # 1 segundo por bit
FREQ_LOW = 440       # bit '0' (Lá)
FREQ_HIGH = 880      # bit '1' (Lá oitava)

"""
===========================================================
ETAPA: COMPREENDENDO CODIFICAÇÃO E MODULAÇÃO DE DADOS
Nessa etapa pude testar diferentes entradas de bits para os 2 tipos de modulação
que estamos estudando. Pude perceber que a NRZ se caracteriza como cada bit virando um tom
contínuo. Já para Manchester, cada bit é representado por 2 tons: o bit 1 se transforma em uma
frequência alto -> baixo e o bit 0 se transforma em uma frequência baixo -> alto.
===========================================================
"""

test_bits = "1111"
print(f"Dados originais: {test_bits}\n")

# Testa cada modulação
print("1. NRZ:")
nrz_signal = encode_nrz(test_bits,debug=True)

print("\n3. Manchester:")
manchester_signal = encode_manchester(test_bits,debug=True)

#sd.play(manchester_signal, SAMPLE_RATE)
#sd.wait()

sd.play(nrz_signal, SAMPLE_RATE)
sd.wait()

plot_signal(nrz_signal,'NRZ',len(test_bits))