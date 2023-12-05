from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from datetime import date
import time as t


data_python = date.today()
global formata_data
formata_data = data_python.strftime( '%d/%m/%Y' )


def ramos_selecao(urls):
    lista_ramos= []
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Enable headless mode
    chrome_options.add_argument(f'user-agent={user_agent}')
    driver = webdriver.Chrome(options=chrome_options)
    #driver = webdriver.Chrome()
   
    

    for url in urls:
        driver.get(url)
        driver.implicitly_wait(10) 

        
        titulo = driver.find_element(By.CLASS_NAME, 'div-info-title')
        try:
            preco = driver.find_element(By.CLASS_NAME, 'div-info-price').find_element(By.TAG_NAME, 'i')
        except:
            preco = driver.find_element(By.CLASS_NAME, 'div-info-price').find_element(By.TAG_NAME, 'span')
        
        if titulo and preco:
            ramos2 = { 
                    'Data': formata_data,
                    'Produto': titulo.text, 
                    'Preco':  preco.text.replace("R$ ", "").replace(",", ".").replace("/Kg", "")
            }
                #conjunto = pd.DataFrame(mercadoliv)
            
            lista_ramos.append(ramos2)

    driver.quit()

    return lista_ramos


  