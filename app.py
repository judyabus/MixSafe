from flask import Flask, render_template, request
import easyocr
import io
from PIL import Image
import sqlite3

app = Flask(__name__)
reader = easyocr.Reader(['en'])

def ImageExtractor(image):
    image = Image.open(io.BytesIO(image.read()))
    result = reader.readtext(image)
    fulltext = ''
    for (_, text, _) in result:
        fulltext += text + ' '
    return fulltext.strip()

@app.route('/', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        Product1 = None
        Product2 = None
        Product1Text = request.form.get('Product1Text')
        Product2Text = request.form.get('Product2Text')
        Product1Image = request.files.get('Product1Image')
        Product2Image = request.files.get('Product2Image')

        if Product1Text:
            Product1 = Product1Text.split(',')
        elif Product1Image:
            Product1 = ImageExtractor(Product1Image)
        else:
            return 'Please enter image or text for Product 1'

        if Product2Text:
            Product2 = Product2Text.split(',')
        elif Product2Image:
            Product2 = ImageExtractor(Product2Image)

        # Connect to the database
        conn = sqlite3.connect("C:\Users\Judy Abusteit\MixSafe\MixSafe\reactions.db", check_same_thread=False)
        cur = conn.cursor()

        reactions = []

        for ingredient1 in Product1:
            for ingredient2 in Product2:
                cur.execute('''
                    SELECT reaction
                    FROM products
                    WHERE (product1 = ? AND product2 = ?) OR (product1 = ? AND product2 = ?)
                ''', (ingredient1, ingredient2, ingredient2, ingredient1))

                result = cur.fetchone()

                if result:
                    reactions.append(result[0])

        cur.close()
        conn.close()

        return render_template('results.html', reactions=reactions, Product1=Product1, Product2=Product2)
    return render_template('data.html')

if __name__ == "__main__":
    app.run(debug=True)