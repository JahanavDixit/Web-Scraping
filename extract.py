import pandas as pd
import requests
from bs4 import BeautifulSoup

df = pd.read_csv('Input.csv')

url_list = list(df['URL'])

result = pd.DataFrame(columns=['Id','Content'])

for url in url_list:
    id = df[df['URL'] == url]['URL_ID'].values[0]
    response = requests.get(url)
    content = ""
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        content_div = soup.find('div', class_='td-post-content tagdiv-type') or soup.find('div', class_='tdb-block-inner td-fix-index')

        if content_div:
            entry_title = soup.find('h1', class_='entry-title') or soup.find('h1', class_='tdb-title-text')
            if entry_title:
                entry_title.get_text(strip=True)
                content += str(entry_title.text)
            else:
                print(url)
                print("Entry Title not found")
            elements_to_exclude = content_div.find_all('pre', class_='wp-block-preformatted')
            for el in elements_to_exclude:
                el.decompose()
            content_div.get_text(strip=True)
            content += str(content_div.text)
            result.loc[len(result)] = {'Id': id, 'Content': content}
        else:
            print(url)
            print("Content div not found")
    else:
        print(url)
        print("Failed to retrieve the webpage")

result.to_csv('content.csv')
