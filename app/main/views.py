from flask import render_template,request,redirect,url_for,abort,flash
from ..models import Role, User
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

@main.route('/new_blog')
@login_required
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        blog = form.blog.data

        #save blog method
        new_blog.save_blog()
        return redirect(url_for('.new_blog'))

    return render_template('blogs.html', blog_form = form)

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
