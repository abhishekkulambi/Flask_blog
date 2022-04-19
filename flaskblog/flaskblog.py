from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'James Clear',
        'title': 'Atomic Habits',
        'content': 'Tiny Changes, Remarkable Results',
        'date_posted': 'April 14, 2021'
    },
    {
        'author': 'Prashanth Neel',
        'title': 'K.G.F Chapter 2',
        'content': "Voilence, Voilence, Voilence I don't like it, I avoid it but Voilence likes me",
        'date_posted': 'April 14, 2022'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)
