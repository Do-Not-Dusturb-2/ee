from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    source_code = None
    url = None
    error = None

    if request.method == 'POST':
        url = request.form['url']
        try:
            response = requests.get(url)
            source_code = response.text
        except requests.RequestException as e:
            error = f"An error occurred: {str(e)}"

    return render_template('index.html', source_code=source_code, url=url, error=error)

if __name__ == '__main__':
    app.run(debug=True)
