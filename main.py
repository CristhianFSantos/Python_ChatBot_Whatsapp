from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
# importar bibliotecas

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(15)
# Navegar até o whatsapp Web

contatos = ['Guilherme Irmão', 'Pai']
# Definir contatos e grupos para enviar mensagens

mensagem = 'Olá, essa é uma mensagem automatizada usando Python'
# Definir mensagem para envio automatizado


def buscar_contato(contato):
    campo_pesquisa = driver.find_element_by_xpath(
        '//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)


# Buscar contatos e grupos


def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath(
        '//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)


# Enviar mensagens para contatos e grupos

for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)
# Enviar mensagens para contatos e grupos
