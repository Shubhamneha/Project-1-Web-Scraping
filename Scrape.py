import requests
from bs4 import BeautifulSoup
def get_latest():
    url="https://www.python.org/"
    response=requests.get(url)

    if response.status_code==200:
        soup=BeautifulSoup(response.text,"html.parser")
        latest=[]

        for article in soup.select('.blog-widget li'):
            title=article.a.text.strip()
            latest.append(title)

        return latest
    else:
        print(f'Failes to retrieve data.status code:{response.status_code}')
        return[]
        
if __name__=='__main__':
    python_articles= get_latest()

    if python_articles:
        print("Latest Articles in the Python Section : ")
    
        for index,article in enumerate(python_articles,1):
            print(f'\n{index}. {article}')
        
else:
    print('Failes to retrieve data')
        

