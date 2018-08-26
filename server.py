from flask import (
    Flask,
    render_template
)

# Create the application instance
app = Flask(__name__, template_folder="templates")

# Create a URL route in our application for "/"
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

@app.route('/como-funciona')
def comofunciona():
    return render_template('como-funciona.html')

@app.route('/quem-somos')
def quemsomos():
    return render_template('quem-somos.html')

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=True)