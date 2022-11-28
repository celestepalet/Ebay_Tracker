import pandas as pd   
    
def order_products(pages_content):

    titles=[]
    prices=[]
    photos=[]
    url_products=[]

    for page in pages_content:
        for post in page.findAll('div',{'class':'s-item__wrapper clearfix'}):

            calification=post.find('span',{'class':'s-item__etrs'})
                        
            if calification is not None:
                title=post.find('div',{'class':'s-item__title'})
                url_photo=post.find('img').get('src') 
                url_product=post.find('a',{'class':'s-item__link'}).get('href')

                price=post.find('div',{'class':'s-item__detail s-item__detail--primary'})
                price=(price.text[:(price.text+' a').find(' a')])
                currency=[]
                price_number=[]
                for element in price:
                    if element.isnumeric() or element=='.':
                        price_number.append(element)
                    else:
                        currency.append(element)
                if price_number[0]== ".":
                    price_number=price_number[1:]
                currency=''.join(currency)
                price_number=float(''.join(price_number))

                titles.append(title.text)
                prices.append(price_number)
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
        product_info= [(articles_table.Title[article]), currency, (articles_table.Price[article]),articles_table.Picture[article],articles_table.URL[article],]
        order_products_list.append(product_info)

    return (order_products_list)

