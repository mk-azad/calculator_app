from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/math', methods = ['POST'])
def math_ops():
    if(request.method == 'POST'):  # Here 'POST' means if someone wants to send a some data through a form by using POST mehtod
        ops = request.form['operation']     # Used the id 'operation' from index.html file where the input from user will be stored     
        num1 = int(request.form['num1'])         # Used the id 'num1' from index.html file where the input from user will be stored
        num2 = int(request.form['num2'])       # Used the id 'num1' from index.html file where the input from user will be stored
        if ops == 'add':         # Through the 'operation' id, checking if the user has selected 'add' option
            r = num1 + num2
            result = "The sum of " + str(num1) + " and " + str(num2) + " is " + str(r)
        
        if ops == 'subtract':    # Through the 'operation' id, checking if the user has selected 'subtract' option
            r = num1 - num2
            result = "The subtraction of " + str(num1) + " and " + str(num2) + " is " + str(r)

        if ops == 'multiply':    # Through the 'operation' id, checking if the user has selected 'multiply' option
            r = num1 * num2
            result = "The multiplication of " + str(num1) + " and " + str(num2) + " is " + str(r)
        
        if ops == 'divide':      # Through the 'operation' id, checking if the user has selected 'divide' option
            r = num1 / num2
            result = "The divition of " + str(num1) + " and " + str(num2) + " is " + str(r)
        
        return render_template('results.html', result = result) # The result will be returned to another html file named 'result.html'









if __name__ == "__main__":
    app.run(port= 5001)