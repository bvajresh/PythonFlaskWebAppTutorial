from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'VB',
        'title': 'Post Title',
        'content': 'Text Text Text',
        'date_posted': 'July 1, 2020'
    },
    {
        'author': 'Jane Deo',
        'title': 'Post 2',
        'content': 'Text Text Post 2',
        'date_posted': 'June 1, 2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title="About")


if __name__ == '__main__':
    app.run(debug=True)
