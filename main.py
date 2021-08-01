from flask import Flask, render_template
from forms import SignUpForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thecodex'

@app.route('/')
def home():
    return 'HelloWorld'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/blog')
def blog():
    posts = [
        {'title': 'Technology in 2021', 'author': 'Nate'},
        {'title': 'Building websites', 'author': 'Nathan'}
    ]
    return render_template('blog.html', author="Nathan", sunny=False, posts=posts)

@app.route('/blog/<string:blog_id>')
def blogpost(blog_id):
    return 'This is the blog post number ' + blog_id

@app.route('/signup')
def signup():
    form = SignUpForm()
    return render_template('signup.html', form=form)

if __name__ == '__main__':
    app.run()