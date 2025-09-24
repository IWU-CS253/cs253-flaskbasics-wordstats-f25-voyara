from flask import Flask, render_template,request

app = Flask(__name__)

word_count = 0
char_count = 0
avg_leng = 0

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result")
def results():
    words = request.form.get("words")
    word_count = len(words.split())
    char_count = len(words)
    avg_leng = char_count/word_count
    return render_template("result.html", word_count, char_count, avg_leng)