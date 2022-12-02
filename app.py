from flask import Flask, render_template
import requests

app = Flask(__name__)
app.secret_key = "secret key"

@app.route('/')
def index():
    # https://newsapi.org/v2/top-headlines?country=in&apiKey=f18e65153a9547ca9f8cb04ea3844e00
    url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=f18e65153a9547ca9f8cb04ea3844e00"
    r = requests.get(url).json()

    context = {
        'articles': r['articles'] 
    }
    
    return render_template('index.html',data=context)
if __name__ == '__main__':
    app.run(debug=True)
