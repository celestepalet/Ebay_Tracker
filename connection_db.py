import sqlite3

def user_table():
    con=sqlite3.connect('ebay_scraper.db')
    c=con.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users'\
        '(name VARCHAR(20) , password VARCHAR(20))')
    con.commit()
    con.close()

def save_products(search, order_porducts_list):
    con=sqlite3.connect('ebay_scraper.db')
    c=con.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS '+ search +\
        '(title VARCHAR(500), currency VARCHAR(500), price INTEGER, url_photo VARCHAR(500), url_product VARCHAR(500))')
    c.executemany("INSERT INTO " + search + " VALUES (?,?,?,?,?)", order_porducts_list)
    con.commit()
    con.close()


def save_tracking_product(product):
    con=sqlite3.connect('ebay_scraper.db')
    c=con.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS track'\
        '(title VARCHAR(500), currency VARCHAR(500), price INTEGER, url_photo VARCHAR(500), url_product VARCHAR(500), date VARCHAR(500))')
    c.execute("INSERT INTO track VALUES (?,?,?,?,?,?)", product)
    con.commit()
    con.close()
    
def compare():
    pass


