from flask import Flask,render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author' : 'Krishna Mishra',
        'title': 'My demo',
        'content':'First F blog content',
        'date_posted':'April 20, 2003'
    },
    {
        'author' : 'Ramesh Agarwal',
        'title': 'My demo second',
        'content':'Second F blog content',
        'date_posted':'April 20, 2003'
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