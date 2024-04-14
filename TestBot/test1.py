from lib2to3.pgen2 import driver
import pywhatkit
import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Número de telefone para enviar a mensagem

numero_destino = "+5511977777777"
# Mensagem que você deseja enviar
mensagem = "Mensagem a ser enviada"

# Horário para enviar a mensagem (hora, minuto)
hora_envio = 16
minuto_envio = 17

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


    # pyautogui.click(3413,993, duration=3)
    # print("Mensagem enviada!")

    wait = WebDriverWait(driver, 20)

    elemento = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div')))
    elemento.click()


# Chamando a função para enviar a mensagem no horário especificado
enviar_mensagem_no_horario(numero_destino, mensagem, hora_envio, minuto_envio, tempo_espera)
