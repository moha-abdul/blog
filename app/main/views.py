from flask import render_template,request,redirect,url_for,abort,flash
from ..models import User, Blog
from . import main
from .forms import UpdateProfile, BlogForm, CommentForm
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
        blog = Blog(title = title, body = body)

        db.session.add(blog)
        db.session.commit()

        # blog.save_blog(blog)
        print('mohaaaaaaaaaaaaa')
        flash('Blog created!')
        return redirect(url_for('main.single_blog',id = blog.id))

    return render_template('newblog.html', title='New Post', blog_form=form)

# view one blog
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

@main.route('/comments/<int:id>', methods=['GET', 'POST'])
def comments(id):
    '''
    view comments
    '''
    comment = CommentForm()
    comment_is = Comments.query.filter_by(post_id=id)
    if comment.validate_on_submit():
        comments = Comments(comment=comment.comment.data, post_id=id, name=comment.name.data)
        comments.save_comments()

    post_commment = Post.query.all()

    return render_template('comment.html', comment=comment, post_comment=post_comment, commented=commented)

@main.route('/delete/<id>')
@login_required
def delete_blog(id):

    '''
     function to delete blog
    '''
    blog = Blog.query.filter_by(id=id).first()

    blog.delete_blog()
    return redirect(url_for('main.index'))

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

# @main.route('/blog/<int:blog_id>/',methods=["GET","POST"])
# def blog(blog_id):
#     blog = Blog.query.get(blog_id)
#     form = CommentForm()
#     if form.validate_on_submit():
#         comment = form.comment.data
#         blog_comment = Comment(post_comment = comment, blogs=blog_id, user = current_user)
#         # new_post_comment.save_post_comments()

#         db.session.add(blog_comment)
#         db.session.commit()
#     comments = Comment.query.all()
#     return render_template('blog_comment.html', title = blog.title, blog = blog, blog_form = form, comments = comments)

# main.route('/blog/comment/new/<int:id>', methods = ['GET','POST'])
# @login_required
# def new_comment(id):
#     '''
#     this view will render form to create a comment
#     '''
#     form = CommentForm()
#     blog = Blog.query.filter_by(id = id).first()

#     if form.validate_on_submit():
#         comment = form.comment.data

#         # comment instance
#         new_comment = Comment(blog_id = blog.id, post_comment = comment, title = title, user = current_user)

#         # save comment
#         new_comment.save_comment()

#         return redirect(url_for('.blogs', id = blog.id ))

#     title = f'{blog.title} comment'
#     return render_template('new_comment.html', title = title, comment_form = form, blog = blog)


