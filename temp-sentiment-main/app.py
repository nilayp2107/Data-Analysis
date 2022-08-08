from flask import Flask, request, render_template
from textblob import TextBlob

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    flag="not entered"
    if request.method == 'POST':
        flag="entered"
        statement = request.form.get('statement')
        result = TextBlob(statement).sentiment
        polarity = result.polarity
        subjectivity = result.subjectivity
        return render_template('home.html', polarity=round(polarity, 4), subjectivity=round(subjectivity, 4))

    return render_template('home.html', polarity='none', subjectivity='none')

if __name__ == "__main__":
    app.run()