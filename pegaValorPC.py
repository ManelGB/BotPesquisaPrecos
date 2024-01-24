import pyautogui as p
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

nav = webdriver.Chrome()

# Pega o valor do processador

nav.get("https://www.pichau.com.br/processador-amd-ryzen-5-5600-6-core-12-threads-3-5ghz-4-4ghz-turbo-cache-35mb-am4-100-100000927box?gclid=CjwKCAjw7oeqBhBwEiwALyHLM6xy7hAWTTBAlOCo-aLWB2-FYBjvVUi4Cd5hrOkTqR03gnJV5WMO0hoCckAQAvD_BwE")
time.sleep(2)
processador = nav.find_element(
    by='xpath', value='//*[@id="__next"]/main/div[2]/div/div[2]/div[4]/div[1]/div/div[1]/div[2]/div[2]')
processador = processador.text
print(processador)
time.sleep(2)

# Pega o valor do placa Mãe

nav.get("https://www.kabum.com.br/produto/114782/placa-mae-gigabyte-b550m-ds3h-amd-am4-micro-atx-ddr4?gclid=CjwKCAjw7oeqBhBwEiwALyHLM-z1PPZWw2xQ0q2dwVF28-wh3DWZyXZbHbNW2IpzjeQ6kYtECiwOpRoCIScQAvD_BwE")
time.sleep(2)
placaMae = WebDriverWait(nav, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'h4.finalPrice')))
placaMae = placaMae.text
print(placaMae)
time.sleep(2)

# Pega o valor do SSD

nav.get("https://www.kabum.com.br/produto/111637/ssd-1-tb-crucial-bx500-sata-leitura-540mb-s-e-gravacao-500mb-s-ct1000bx500ssd1?gad_source=1&gclid=Cj0KCQiA2KitBhCIARIsAPPMEhIxbpl9T26sxk1bUFtOXtcMnMpl7-41ZHb2z7tebo8YuYsxmwcwRAUaAsDiEALw_wcB")
time.sleep(2)
ssd = WebDriverWait(nav, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'h4.finalPrice')))
ssd = ssd.text
print(ssd)
time.sleep(2)

# Pega o valor da RAM

nav.get("https://www.kabum.com.br/produto/172366/memoria-kingston-fury-beast-16gb-3200mhz-ddr4-cl16-preto-kf432c16bb1-16?gad_source=1&gclid=CjwKCAiApuCrBhAuEiwA8VJ6JlQ3NMznBFxxc-cKSFbcgUAqFW2URfZgdhvmXzfyXb0Ke8G5fK46HxoCLU0QAvD_BwE")
time.sleep(2)
ram = WebDriverWait(nav, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'h4.finalPrice')))
ram = ram.text
print(ram)
time.sleep(2)

# Pega o valor da fonte

nav.get("https://www.kabum.com.br/produto/462815/fonte-msi-mag-a750gl-pcie5-atx-3-0-750w-80-plus-gold-modular-pfc-ativo-bivolt-preto?gad_source=1&gclid=Cj0KCQiAwbitBhDIARIsABfFYIJW0SeT8CgbIovJ7o44jB1vf_Yo_oqusGYSKEmg6PRmIYhniSikmKUaAp-EEALw_wcB")
time.sleep(2)
fonte = WebDriverWait(nav, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'h4.finalPrice')))
fonte = fonte.text
print(fonte)
time.sleep(2)

# Pega o valor do gabinete

time.sleep(2)
nav.get("https://www.kabum.com.br/produto/173227/gabinete-gamer-t-dagger-g25b-rgb-preto-mid-tower-black-tgc-g25b")
gabinete = WebDriverWait(nav, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'h4.finalPrice')))
gabinete = gabinete.text
print(gabinete)
time.sleep(2)


nav.quit()

p.hotkey('win', 'r')

time.sleep(1)

p.click(x=167, y=941, clicks=2, interval=0.2)

p.write('Chrome')
p.hotkey('enter')

time.sleep(4)

p.hotkey('ctrl', 't')
p.write('https://docs.google.com/spreadsheets/d/13te2ijh-TVbbODknZWrlF-Rxb0b3y0OL0bFnPsi6X5w/edit#gid=0')

time.sleep(2)

p.hotkey('enter')

time.sleep(3)

p.click(x=261, y=386, clicks=2, interval=0.2)

time.sleep(1)

p.write(processador)
p.hotkey('tab')

p.write(placaMae)
p.hotkey('tab')

p.write(ssd)
p.hotkey('tab')

p.write(ram)
p.hotkey('tab')

p.write(fonte)
p.hotkey('tab')

p.write(gabinete)

time.sleep(1)

p.click(x=1636, y=397, clicks=1, interval=0.2)

p.click(x=1067, y=397, clicks=1, interval=0.2)

time.sleep(10)
