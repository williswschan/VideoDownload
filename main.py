from flask import Flask

app = Flask(__name__)
access_count = 0

@app.route('/')
def home():
    global access_count
    access_count += 1
    return f'Page accessed {access_count} times.'

if __name__ == '__main__':
    app.run(debug=True)