from flask import Flask, render_template, request
import datetime


app = Flask(__name__, static_folder='static')

# Temp converter function
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0 / 9.0

# Route for index page
@app.route('/', methods=['GET'])
def index():
    current_time = datetime.datetime.now().strftime("%A %B %d, %Y at %I:%M %p")
    return render_template('index.html', current_time=current_time)

# Route for option1 page
@app.route('/option1', methods=['GET', 'POST'])
def index_option1():
    if request.method == 'POST':
        fahrenheit = float(request.form['fahrenheit'])
        celsius = fahrenheit_to_celsius(fahrenheit)
        return render_template('option1.html', fahrenheit=fahrenheit, celsius=celsius)
    return render_template('option1.html')


# Route for option2 page
@app.route('/option2', methods=['GET', 'POST'])
def index_option2():
    if request.method == 'POST':
        fahrenheit = float(request.form['fahrenheit'])
        celsius = fahrenheit_to_celsius(fahrenheit)
        return render_template('option2.html', fahrenheit=fahrenheit, celsius=celsius)
    return render_template('option2.html')

if __name__ == '__main__':
    app.run(debug=True)