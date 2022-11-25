import requests 
from bs4 import BeautifulSoup as b    
import pandas as pd

def get_data(search):

    titles=[]
    prices=[]
    photos=[]
    url_products=[]

    for page in range(1,2):

        url='https://www.ebay.com/sch/'+search+'&_pgn='+str(page)
        html=requests.get(url)  
        content=html.content
        soup=b(content,'html.parser')

        for post in soup.findAll('div',{'class':'s-item__wrapper clearfix'}):
            title=post.find('div',{'class':'s-item__title'})
            price=post.find('div',{'class':'s-item__detail s-item__detail--primary'})
            calification=post.find('span',{'class':'s-item__etrs'})
            url_photo=post.find('img').get('src') 
            url_product=post.find('a',{'class':'s-item__link'}).get('href')
            
            if calification is not None:
                titles.append(title.text)
                prices.append(float(''.join((price.text[3:(price.text+' a').find(' a')]).split())))
                photos.append(url_photo)
                url_products.append(url_product)
    
    articles_table = pd.DataFrame({
                                    'Title':titles,
                                    'Price':prices,
                                    'Picture':photos,
                                    'URL': url_products
                                })
    articles_table = articles_table.sort_values(by=['Price'],ascending=[True])
        
    order_products_list=[]
    for article in articles_table.index:
        
        product_info= [(articles_table.Title[article]),(articles_table.Price[article]),articles_table.Picture[article],articles_table.URL[article]]
        order_products_list.append(product_info)

    return (order_products_list)


                

