from flask import Flask, render_template

app = Flask(__name__, template_folder='t1')  # Set template folder to "t1"

@app.route('/')
def home():
    return render_template('index.html')  # Flask will now look inside "t1"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

