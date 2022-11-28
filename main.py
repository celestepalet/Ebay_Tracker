from flask import Flask, render_template, request
import scraper
import parser
import sqlite3
import time
import connection_db

app= Flask(__name__)

@app.route('/')
def index():
     return render_template('index.html')

@app.route('/index_in')
def index_in():
     return render_template('index_in.html')

@app.route('/search', methods=['POST'])
def save_search():
     search=request.form['search']
     pages_content=scraper.get_data(search)
     products=parser.order_products(pages_content)
     connection_db.save_products(search, products)
     return render_template('articles.html', products=products)

@app.route('/log_in', methods=['POST', 'GET'])
def log_in():
     connection_db.user_table()
     if request.method=='POST':
          user_name=request.form['name']
          password=request.form['password']
          con=sqlite3.connect('ebay_scraper.db')
          c=con.cursor()
          statement=f"SELECT * from users WHERE name='{user_name}' AND password='{password}';"
          c.execute(statement)
          if not c.fetchone():
               text='The data entered is not correct'
               return render_template('error.html', text=text)
          else:
               return render_template('index_in.html', name=user_name)
     else:
          request.method == 'GET'
          return render_template('log_in.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
     connection_db.user_table()
     con=sqlite3.connect('ebay_scraper.db')
     c=con.cursor()
     if request.method=='POST':
          if(request.form['name'])!=''and request.form['password']!='':
               name=request.form['name']
               password=request.form['password']
               statement=f"SELECT * from users WHERE name='{name}';"
               c.execute(statement)
               data=c.fetchone()
               if data:
                    text='Please try with a different user'
                    return render_template('error.html', text=text)
               else:
                    if not data:
                         c.execute('INSERT INTO users (name,password) VALUES (?,?)', (name,password))
                         con.commit()
                         con.close() 
                    text= "Succesfully registered, login please"   
                    return render_template('log_in.html', text=text)
               
     elif request.method=='GET':
          return render_template('register.html' )
@app.route('/search_in', methods=['POST'])
def save_search_in():
     search=request.form['search_in']
     pages_content=scraper.get_data(search)
     products=parser.order_products(pages_content)
     connection_db.save_products(search, products)
     return render_template('articles_in.html', products=products)

@app.route('/tracking', methods=['POST'])
def tracking():
     product_track=request.form['product_track']
     product_track=product_track.split("'")
     info_product=[]
     for element in product_track:
          if len(element)>2:
               if element==product_track[4]:
                    element=element[1:-2]          
               info_product.append(element)
     info_product[2][1:-1]
     info_product.append(time.strftime('%d/%m/%y'))
     tipo=type(info_product)
     connection_db.save_tracking_product(info_product)
     
     return render_template('funciona.html', product_track=info_product, tipo=tipo)    

if __name__ == '__main__':
     app.run(debug=True)       
