from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Post, User, Comment
from flask_wtf import FlaskForm
from . import db
import json
import mysql.connector

#Blueprint of the application
views = Blueprint('views', __name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="America!1324",
    database='user'
)

#User must be logged in successfully to access the home page
@views.route('/')
@views.route('/home')
@login_required
def home():
    posts = Post.query.all()
    #Check if user clicks on the initialize button, and the user does the rest of this function executes
    # if request.method == 'POST':
    #     flash('Initialized Database!', category='successful')
    #     cursor = mydb.cursor()
    #     #opens path to university.sql file and reads it
    #     fd = open('website/university.sql', 'r')
    #     sqlFile = fd.read()
    #     fd.close()
    #     sqlCommands = sqlFile.split(';')
    #     #iterates over the sql code to strip empty spaces and disregard semicolons
    #     for command in sqlCommands:
    #             if command.strip() != '':
    #                 cursor.execute(command)
    # mydb.commit()
    #keeps the user in the home page unless the user decides to logout
    return render_template("home.html", user=current_user, posts = posts)

@views.route("/create_post", methods=['GET','POST'])
@login_required
def create_post():
    if request.method == "POST":
        subject = request.form.get('subject')
        description = request.form.get('description')
        tag = request.form.get('tag')
        
        if not subject:
            flash('Subject cannot be empty', category='error')
        else:
            post = Post(subject=subject, description=description, tag=tag, author=current_user.id)
            db.session.add(post)
            db.session.commit()
            flash('Post created!', category='success')
            return redirect(url_for('views.home'))
    return render_template('create_post.html', user=current_user)

@views.route("/delete-post/<id>")
@login_required
def delete_post(id):
    post = Post.query.filter_by(id=id).first()
    
    if not post:
        flash("Post does not exist.", category='error')
    elif current_user.id != post.author:
        flash('You do not have permission to delete this post.', category='error')
    else:
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted.', category='success')
    return redirect(url_for('views.home'))

@views.route("/posts/<username>")
@login_required
def posts(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        flash('No user with that username exists.', category='error')
        return redirect(url_for('views.home'))
    posts = user.posts
    return render_template("posts.html", user=current_user, posts=posts, username=username)

@views.route("/create-comment/<post_id>", methods=['POST'])
@login_required
def create_comment(post_id):
    text = request.form.get('text')
    sentiment = request.form.get('sentiment')
    cursor = mydb.cursor()
    if not text:
        flash('Comment cannot be empty', category='error')
    else:
        post = Post.query.filter_by(id = post_id)
        if post:
            comment=Comment(text=text, author=current_user.id, sentiment=sentiment, post_id=post_id)
            db.session.add(comment)
            db.session.commit()
        else:
            flash('Post does not exist', category='error')
    return redirect(url_for('views.home'))

@views.route("/delete-comment/<comment_id>")
@login_required
def delete_comment(comment_id):
    comment= Comment.query.filter_by(id=comment_id).first()
    
    if not comment:
        flash('Comment does not exists', categor='error')
    elif current_user.id != comment.author and current_user.id != comment.post.author:
            flash('You do not have permission to delete this comment.', categor='error')
    else:
        db.session.delete(comment)
        db.session.commit()

    return redirect(url_for('views.home'))
    