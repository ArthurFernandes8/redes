import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from funcoes import *

output_device = 0
input_device = 0
sd.default.device = (input_device, output_device)

SAMPLE_RATE = 44100  # Taxa de amostragem do audio
BIT_DURATION = 1.0   # 1 segundo por bit
FREQ_LOW = 440       # bit '0' (Lá)
FREQ_HIGH = 880      # bit '1' (Lá oitava)

# Mensagem obtida na etapa 2 (decodificada a partir do arquivo .wav)
original_bits = "011010110000101001101000"

# Faixa de SNR a ser testada (de -50dB a 1dB)
snr_values = np.arange(-50, 1)

errors_per_snr = []   # Armazena a quantidade de erros para cada SNR testado

# Gera o sinal Manchester limpo (sem ruído)
clean_signal = encode_manchester(original_bits)

# Testa o impacto do ruído para cada valor de SNR
for snr in snr_values:
    noisy = adicionar_ruido(clean_signal, snr)  # Adiciona ruído gaussiano
    decoded = decode_manchester(noisy, len(original_bits))  # Decodifica o sinal ruidoso

    # Conta quantos bits foram decodificados incorretamente
    errors = sum(a != b for a, b in zip(original_bits, decoded))
    errors_per_snr.append(errors)

    print(f"SNR {snr} dB → Erros: {errors}")

# Gera o gráfico (SNR no eixo X e número de erros no eixo Y)
plt.plot(snr_values, errors_per_snr)
plt.xlabel("SNR (dB)")                   # Rotulo do eixo X
plt.ylabel("Número de Erros")            # Rotulo do eixo Y
plt.title("Ruído x Erros na Modulação Manchester")
plt.grid(True)
plt.show()
