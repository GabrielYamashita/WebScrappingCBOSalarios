
import string
import requests
import pandas as pd
from lxml import html

letters = list(string.ascii_uppercase)

CBO = []
mediaSalarial = []

for letter in letters:
    url = f"https://www.salario.com.br/tabela-salarial/?cargos={letter}"  # Replace with the URL of the website you want to scrape
    response = requests.get(url)


    # Parse the HTML content
    html_content = response.content
    tree = html.fromstring(html_content)

    # Example: Suppose the items are inside a <ul> element
    items_container = tree.xpath('/html/body/div[5]/div[2]/div[1]/div[2]/div/div[2]/div[3]/table/tbody')


    if items_container == []:
        print(f"Sem dados de {letter}")

    else:
        print(f"Puxando dados de {letter}...")
        items_container = items_container[0]
        # Example: Iterate over <li> elements inside the <ul> element
        items = items_container.xpath('.//td[contains(@data-label, "CBO")]')
        for item in items:
            # Extract data from each item
            item_text = item.text_content().strip()
            CBO.append(item_text)
            # data['CBO'] = item_text

        items = items_container.xpath('.//td[contains(@data-label, "dia Salarial")]')
        for item in items:
            # Extract data from each item
            item_text = item.text_content().strip()
            mediaSalarial.append(item_text)
            # print("")
            # data['Média Salarial'] = item_text

data = {}

data['CBO'] = CBO
data['Média Salarial'] = mediaSalarial

# print(data)


df = pd.DataFrame(data, index=None)
df.to_excel('./CBO Salário.xlsx')
