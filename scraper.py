import requests 
from bs4 import BeautifulSoup as b    

def get_data(search):

    pages_content=[]

    for page in range(1,2):

        url='https://www.ebay.com/sch/'+search+'&_pgn='+str(page)
        html=requests.get(url)  
        content=html.content
        soup=b(content,'html.parser')
        pages_content.append(soup)
    
    return pages_content

        

                

 