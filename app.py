from flask import Flask, render_template
from routes.menu import menu_bp
from routes.orders import orders_bp

app = Flask(__name__)
app.secret_key = 'supersecretkey'

app.register_blueprint(menu_bp, url_prefix='/menu')
app.register_blueprint(orders_bp, url_prefix='/orders')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
