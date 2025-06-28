from flask import Flask, render_template, request, redirect, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

conn = mysql.connector.connect(host='localhost', user='root', password='', database='bookstore')
cursor = conn.cursor(dictionary=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    # Registration logic
    pass

@app.route('/login', methods=['POST'])
def login():
    # Login logic
    pass

@app.route('/catalog')
def catalog():
    cursor.execute("SELECT * FROM books WHERE quantity > 0")
    books = cursor.fetchall()
    return render_template('catalog.html', books=books)

@app.route('/add_to_cart/<int:book_id>')
def add_to_cart(book_id):
    # Add book to cart and decrement quantity
    pass

@app.route('/checkout')
def checkout():
    # Generate bill and save order
    pass

if __name__ == '__main__':
    app.run(debug=True)
