from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
    # Pass variables to the template
    number1 = 42
    number2 = 87
    return render_template('index.html', number1=number1, number2=number2)

if __name__ == '__main__':
    app.run(debug=True)

