from flask import Flask, render_template, request
import easyocr
import io
from PIL import Image
import sqlite3
import os

app = Flask(__name__, static_folder='static')
reader = easyocr.Reader(['en'])


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/data')
def data():
    return render_template('data.html')

@app.route('/', methods=['POST'])
def results():
    if request.method == 'POST':
        Product1 = None
        Product2 = None
        Product1Text = request.form.get('Product1Text')
        Product2Text = request.form.get('Product2Text')


        if Product1Text:
            Product1 = Product1Text.split(',')
        else:
            return 'Please enter image or text for Product 1'

        if Product2Text:
            Product2 = Product2Text.split(',')
        else:
            return 'Please enter text for Product 2'

        with sqlite3.connect("C:\\Users\\Judy Abusteit\\Projects\\MixSafe\\reactions.db", check_same_thread=False) as conn:
            cur = conn.cursor()
            Product1 = [ingredient.strip() for ingredient in Product1]
            Product2 = [ingredient.strip() for ingredient in Product2]
            reactions = []
            for ingredient1 in Product1:
                for ingredient2 in Product2:
                    cur.execute('''
                        SELECT reaction
                        FROM reactions
                        WHERE (product1 = ? AND product2 = ?) OR (product1 = ? AND product2 = ?)
                    ''', (ingredient1, ingredient2, ingredient2, ingredient1))

                    result = cur.fetchone()

                    if result:
                        reactions.append(result[0])
            if reactions:
                cur.close()
                return render_template('results.html', reactions=reactions, Product1=Product1, Product2=Product2)

            cur.close()

    return render_template('data.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
