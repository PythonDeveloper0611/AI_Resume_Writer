from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_resume():
    data = request.form
    return render_template('resume.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)