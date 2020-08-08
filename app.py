import requests
from bs4 import BeautifulSoup
from flask import Flask, url_for, render_template

app = Flask(__name__)

URL = 'https://www.meteoplug.com/cgi-bin/meteochart.cgi?draw=eae4e1e0e3f1b4b4aeb383aeb2be75abbdbc83b2a9ffb6b2b1afbaa6a8'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
table_rows = soup.find_all('td')


@app.route('/')
def index():
    return render_template('index.html', table_rows=table_rows)


if __name__ == '__main__':
    app.run()
