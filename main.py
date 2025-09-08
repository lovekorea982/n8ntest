from flask import Flask

app = Flask(__name__)

@app.route('/')
def sum_numbers():
    total = sum(range(1, 10))  # 1부터 9까지 더함
    return f'The sum of numbers from 1 to 9 is: {total}'

if __name__ == '__main__':
    app.run(debug=True)
