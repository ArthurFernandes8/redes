import soundfile as sf
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
ETAPA: DECODIFICAÇÃO
O arquivo para minha matrícula possui 24 segundos de áudio.
Sabendo que cada bit corresponde a exatamente 1 segundo,
podemos deduzir que a mensagem contém 24 bits.
===========================================================
"""

# LEITURA DO ÁUDIO QUE CORRESPONDE À MINHA MATRÍCULA
audio_signal, sr = sf.read("dados_122210175_44100hz.wav")

# PROCESSO DE DECODIFICAÇÃO MANCHESTER
decoded = decode_manchester(audio_signal, 24, sr, debug=True)

# EXIBIÇÃO DO RESULTADO
print("Bits decodificados:", decoded)
print("Quantidade de bits:", len(decoded))