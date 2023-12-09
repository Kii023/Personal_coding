from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    numbers = [1,2,3,4]
    numbers.append(100)
    num_check = 4 in numbers
    return str(numbers) + str(num_check)

if __name__ == '__main__':
    app.run(debug=True)