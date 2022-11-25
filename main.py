from flask import Flask, render_template, request
import scraper


app= Flask(__name__)

@app.route('/')
def index():                            
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def save_search():
     search=request.form['search']
     products=scraper.get_data(search) 
     return render_template('articles.html', products=products)

if __name__ == '__main__':
     app.run(debug=True)       
