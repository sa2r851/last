from flask import Flask
from flask import render_template ,url_for ,Blueprint




app = Flask(__name__)


home = Blueprint('home', __name__,template_folder='templates' ,static_folder='static')

@home.route('/')
def home_page():
    return render_template('index.html')

about = Blueprint('about', __name__,template_folder='templates' ,static_folder='static')

@about.route('/about')
def skills():
    title = 'About'
    return render_template('about.html')




blog = Blueprint('blog', __name__,template_folder='templates' ,static_folder='static')

@blog.route('/blog')
def article():
    title = 'Blog'
    return render_template('blog.html')
about = Blueprint('about', __name__,template_folder='templates' ,static_folder='static')

@blog.route('/blog/myblog')
def posts():
    title = 'My blog'
    return render_template('blog-post.html', title=title)




contact = Blueprint('contact', __name__,template_folder='templates' ,static_folder='static')

@contact.route('/contact')
def emails():
    return render_template('content.html')



projects = Blueprint('projects', __name__,template_folder='templates' ,static_folder='static')

@projects.route('/projects')
def project():
    
    return render_template('projects.html')

app.register_blueprint(home)
app.register_blueprint(about)
app.register_blueprint(projects)
app.register_blueprint(blog)
app.register_blueprint(contact)





if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("5000"), debug=True)