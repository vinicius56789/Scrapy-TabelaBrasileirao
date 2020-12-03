import time
import requests
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import chromedriver_binary

url = "https://www.cbf.com.br/futebol-brasileiro/competicoes/campeonato-brasileiro-serie-a/2020"
option = Options()
option.headless = True
driver = webdriver.Chrome(options=option)

driver.get(url)
element = driver.find_element_by_xpath("//table[@class='table m-b-20 tabela-expandir']")

html_content = element.get_attribute('outerHTML')
soup = BeautifulSoup(html_content, 'html.parser')
table = soup.find(name='table')
df_full = pd.read_html(str(table))[0].head(20)
df = df_full[['Posição', 'PTS', 'J', 'V', 'D', 'E', '%']]
df.columns = ['pos', 'pontos', 'J', 'V', 'D', 'E', 'aproveitamento']
brasileirao = {}
brasileirao['times'] = df.to_dict('records')
time.sleep(2)
driver.quit()

json = json.dumps(brasileirao)
fp = open('tabela2.json', 'w')
fp.write(json)
fp.close()