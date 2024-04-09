import pywhatkit
import pyautogui
import time

# Número de telefone para enviar a mensagem

numero_destino = "+5511911111111"
# Mensagem que você deseja enviar
mensagem = "Mensagem a ser enviada"

# Horário para enviar a mensagem (hora, minuto)
hora_envio = 15
minuto_envio = 36

# Tempo de espera em segundos (deve ser maior que 7 segundos)
tempo_espera = 8

# Função para enviar mensagem no horário desejado
def enviar_mensagem_no_horario(numero, mensagem, hora, minuto, tempo_espera):
    # Enviar mensagem
    pywhatkit.sendwhatmsg(numero, mensagem, hora, minuto, wait_time=tempo_espera)
    print(f"Mensagem digitada para {numero} às {hora}:{minuto}!")
    
    # Esperar um momento para a mensagem ser digitada
    time.sleep(10)  # Ajuste conforme necessário

    # Clicar no botão de envio (usando PyAutoGUI)


    pyautogui.click(3413,993, duration=3)
    print("Mensagem enviada!")

# Chamando a função para enviar a mensagem no horário especificado
enviar_mensagem_no_horario(numero_destino, mensagem, hora_envio, minuto_envio, tempo_espera)
