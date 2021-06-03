import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import warnings
warnings.filterwarnings("ignore")
import json

chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-setuid-sandbox")
driver = webdriver.Chrome(chrome_options=chrome_options)
url="https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1"
driver.get(url)

content=driver.page_source
Soup=BeautifulSoup(content)
num=Soup.find_all('div',attrs={'id':'Div1','class':'product'})

output=[]
for x in num:
    p=(x.find('span',attrs={'class':'price'})).find('span')
    t=x.find('a',attrs={"class":"catalog-item-name"})
    s=x.find('span',attrs={"class":"status"})
    m=(x.find('a',attrs={'class':'catalog-item-brand'}))
    s=False if s.text=='Out of Stock' else True
    out={'price':float(p.text[1:]),'title':str(t.text),'stock':s,'maftr':str(m.text)}
    output.append(out)

    json_string=json.dumps(output)

    with open('Data.json', 'w') as f:
        json.dump(output, f, indent=4)