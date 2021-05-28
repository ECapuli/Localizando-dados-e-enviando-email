from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from time import sleep
import smtplib
from email.mime.text import MIMEText

url = "https://www.coronatracker.com/pt-br/"

driver = webdriver.Chrome(executable_path = r"C:\Users\NOTEBOOK\Desktop\raspagem\chromedriver.exe")
driver.get(url)
sleep(5)
curados = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/span')
casos = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/span')
mortos = driver.find_element_by_xpath('//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/span')
curados = curados.text
casos = casos.text
mortos = mortos.text

print('Os casos confirmados foram ',casos)
print('Os individuos curados somam ', curados)
print('O numero de mortos é de ',mortos)

def sendmail():
    # conexão com os servidores do google
    smtp_ssl_host = 'smtp.gmail.com'
    smtp_ssl_port = 465
# username ou email para logar no servidor
    username = 'teste@gmail.com'
    password = 'teste'

    from_addr = 'teste@gmail.com'
    to_addrs = ['teste2@gmail.com']

# a biblioteca email possuí vários templates
# para diferentes formatos de mensagem
# neste caso usaremos MIMEText para enviar
# somente texto
    message = MIMEText(f'ACABAMOS DE ATINGIR:\n{casos} DE CASOS CONFIRMADOS; \nO NUMERO DE MORTOS SAO {mortos}')
    message['subject'] = 'PANDEMIA ATINGIU NUMERO CRITICO'
    message['from'] = from_addr
    message['to'] = ', '.join(to_addrs) 

# conectaremos de forma segura usando SSL
    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
# para interagir com um servidor externo precisaremos
# fazer login nele
    server.login(username, password)
    server.sendmail(from_addr, to_addrs, message.as_string())
  
if casos >= "150000":
    sendmail()
    print('ALERTA DE EMIAL ENVIADO DEVIDO NUMERO DE CASOS AUMENTANDO')
