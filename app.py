
from flask import Flask, render_template, url_for, request, redirect
import TwitterScraper as ts

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        twe = ts.tweetsFromUser(task_content)
        print(twe)

        return render_template('index.html', tables=[twe.to_html(classes='data')], titles=twe.columns.values)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
