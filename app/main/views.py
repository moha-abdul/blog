from flask import render_template,request,redirect,url_for,abort,flash
from ..models import Role, User, Blog
from . import main
from .forms import UpdateProfile, BlogForm
from .. import db,photos
from flask_login import login_required, current_user


@main.route('/')
def index():

    '''
    View of root page function that returns the index page and its data
    '''
    
    return render_template('index.html')

@main.route('/blogs')
@login_required
def blogs():
    return render_template('blogs.html')

# @main.route('/new_blog', methods = ['GET','POST'])
# @login_required
# def new_blog():
#     form = BlogForm()
#     if form.validate_on_submit():
#         blogs = Blog (title=form.title.data,body=form.body.data,user_id=current_user.id)
#         db.session.add (blogs)
#         db.session.commit ()

#         flash ( 'Your blog has been created' )
#         return redirect(url_for('.new_blog'))
#     blogs = Blog.query.all ()

#     return render_template('new_blog.html', blog_form = form)


@main.route('/blog/new', methods=['GET','POST'])
@login_required
def new_blog():
    form = BlogForm()

    if form.validate_on_submit():

        title=form.title.data
        body=form.body.data
        blog = Blog(title=title,
                    body = body,
                    user=current_user)
        db.session.add(blog)
        db.session.commit()

        # blog.save_blog(blog)
        print('kasambuli')
        flash('Blog created!')
        return redirect(url_for('main.single_blog',id=blog.id))

    return render_template('newblog.html', title='New Post', blog_form=form)

@main.route('/blog/new/<int:id>')
def single_blog(id):
    blog = Blog.query.get(id)
    return render_template('singleblog.html', blog = blog)

@main.route('/allblogs')
@login_required
def blog_list():
    # Function that renders the blogs and contents

    blogs = Blog.query.all()

    return render_template('blogs.html', blogs = blogs)

@main.route('/user/<username>')
def profile(username):

    '''
    View of page function that returns the the user's profile
    '''

    user = User.query.filter_by(username = username).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<username>/update',methods = ['GET','POST'])
@login_required
def update_profile(username):
    user = User.query.filter_by(username = username).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',username=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<username>/update/pic',methods= ['POST'])
@login_required
def update_pic(username):
    user = User.query.filter_by(username = username).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',username=username))




# @main.route('/blog/new/<int:id>', methods = ['GET','POST'])
# @login_required
# def new_blog(id):
#     form = BlogForm()
#     if form.validate_on_submit():
#         title = form.title.data
#         blog = form.blog.data

#         # Updated review instance
#         new_blog = Blog(title=title,movie_review=review,user=current_user)

#         # save blog method
#         new_blog.save_blog()
#         return redirect(url_for('.blog',id =blog.id ))

#     title = f'{blog.title} blog'
#     return render_template('new_blog.html',title = title, blog_form=form)
