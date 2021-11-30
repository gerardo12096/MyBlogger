from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Post, Users, Comment, Tag
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
    database='project_db'
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
    return render_template("home.html", users=current_user, posts = posts)

@views.route("/create_post", methods=['GET','POST'])
@login_required
def create_post():
    cursor = mydb.cursor()
    query = "SELECT COUNT(post.author) FROM post WHERE post.date_created = current_date AND post.author = %s"
    cursor.execute(query,[current_user.id])
    number_of_posts = cursor.fetchone()[0] + 1
    mydb.commit()
    cursor.close()
    print(current_user.id)
    print(number_of_posts)
    if(number_of_posts > 2):
        flash("Can not post more than twice in one day!", category='error')
        return redirect(url_for('views.home'))
    elif request.method == "POST":
        print()
        subject = request.form.get('subject')
        description = request.form.get('description')
        tag_list = request.form.get('tag')
        tags = tag_list.split("#")
        print(tags)
        if not subject:
            flash('Subject cannot be empty', category='error')
        else:
            post = Post(subject=subject, description=description, author=current_user.id)
            db.session.add(post)
            db.session.commit()
            for tag in tags:
                tags = Tag(text=tag, author=current_user.id,post_id=post.id)
                db.session.add(tags)
                db.session.commit()
            flash('Post created!', category='success')
            return redirect(url_for('views.home'))
    return render_template('create_post.html', users=current_user)

@views.route("/initialize", methods=['GET','POST'])
@login_required
def initialize():
    cursor=mydb.cursor()
    if request.method=='POST':
        flash("Initialized the database!", category='success')
        fd = open('projectDB.sql', 'r')
        sqlFile = fd.read()
        fd.close()
        sqlCommands = sqlFile.split(';')
        for command in sqlCommands:
                if command.strip() != '':
                    print(command)
                    cursor.execute(command)
                    mydb.commit()
        # sqlfile = open('university.sql', 'r')
        # query = "".join(sqlfile.readlines())
        # cursor.execute(query, multi=True)
        # mydb.commit()
        # print(query)
        # cursor.close()
        # sqlfile.close()
    return render_template('initialize.html', users=current_user)

@views.route("/delete-post/<id>")
@login_required
def delete_post(id):
    post = Post.query.filter_by(id=id).first()
    

    if current_user.id != post.author:
        flash('You do not have permission to delete this post.', category='error')
    else:
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted.', category='success')
    return redirect(url_for('views.home'))

@views.route("/posts/<username>")
@login_required
def posts(username):
    users = Users.query.filter_by(username=username).first()
    if not users:
        flash('No user with that username exists.', category='error')
        return redirect(url_for('views.home'))
    posts = users.posts
    return render_template("posts.html", users=current_user, posts=posts, username=username)

@views.route("/create-comment/<post_id>", methods=['GET','POST'])
@login_required
def create_comment(post_id):
    text = request.form.get('text')
    sentiment = request.form.get('sentiment')
    cursor = mydb.cursor()
    query = "SELECT COUNT(comment.id) FROM comment INNER JOIN post ON comment.post_id = post.id WHERE post.id = (%s) AND comment.author = (%s)"
    cursor.execute(query,(post_id,current_user.id))
    result = cursor.fetchone()[0] + 1
    # mydb.commit()
    # cursor.close()
    # cursor = mydb.cursor()
    query2 = "SELECT COUNT(*) FROM comment WHERE comment.date_created = CURRENT_DATE AND comment.author = %s"
    cursor.execute(query2,[current_user.id])
    commented_today = cursor.fetchone()[0] + 1
    query3 = "SELECT DISTINCT post.author FROM post WHERE post.id = %s"
    cursor.execute(query3,[post_id])
    current_author = cursor.fetchone()[0]
    mydb.commit()
    cursor.close()
    print(current_user.id)
    print(result)
    if current_user.id == current_author:
        flash("Can't comment on own post!", category='error')
    elif result > 1:
        flash("Cannot comment more than once on the same post!", category='error')
    elif(commented_today > 3):
        flash("Cannot comment more than 3x a day!", category='error')
    else:
        if not text:
            flash('Comment cannot be empty!', category='error')
        else:
            post = Post.query.filter_by(id = post_id)
            if post:
                comment=Comment(text=text,sentiment=sentiment, author=current_user.id, post_id=post_id)
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
            flash('You do not have permission to delete this comment.', category='error')
    else:
        db.session.delete(comment)
        db.session.commit()
    return redirect(url_for('views.home'))
    