import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'book_repo'
app.config["MONGO_URI"] = 'mongodb+srv://root:r00tUser@myfirstcluster-sknof.mongodb.net/book_repo?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_home')
def get_home():
    return render_template('home.html',
                           home=mongo.db.book_title.find().limit(6),
                           homes=mongo.db.book_title.find().limit(6))

#####################Books############################


@app.route('/get_books')
def get_books():
    return render_template("books.html",
                           books=mongo.db.book_title.find(),
                           categories=mongo.db.categories.find(),
                           books_limit=mongo.db.book_title.find().limit(6))

#####################People############################


@app.route('/get_people')
def get_people():
    return render_template('people.html',
                           books=mongo.db.book_title.find(),
                           work_categories=mongo.db.work_categories.find(),
                           books_limit=mongo.db.book_title.find().limit(6))

#####################Search############################


@app.route('/get_search')
def get_search():
    return render_template('search.html')

#####################Blog############################


@app.route('/get_blog')
def get_blog():
    return render_template('blog.html',
                           blog=mongo.db.blog.find(),
                           blog_post=mongo.db.blog.find())


@app.route('/get_add_blog')
def get_add_blog():
    return render_template('add_blog.html',
                           blog=mongo.db.blog.find())


@ app.route('/insert_blog', methods=['POST'])
def insert_blog():
    blog = mongo.db.blog
    blog.insert_one(request.form.to_dict())
    return redirect(url_for('get_blog'))


@ app.route('/delete_subject/<subject_id>')
def delete_subject(subject_id):
    mongo.db.blog.remove({'_id': ObjectId(subject_id)})
    return redirect(url_for('get_blog'))


@ app.route('/edit_blog/<subject_id>')
def edit_blog(subject_id):
    the_subject = mongo.db.blog.find_one({"_id": ObjectId(subject_id)})
    all_blog = mongo.db.blog.find()
    return render_template('edit_blog.html', subject=the_subject,
                           blog=all_blog)

#####################Add Comment############################


@app.route('/insert_comment/<subject_id>', methods=['POST'])
def insert_comment(subject_id):
    blog = mongo.db.blog
    blog.update_one({'_id': ObjectId(subject_id)},
                    {'$push': {'comments': request.form.get('comments')}
                     })
    return redirect(url_for('get_blog'))

# needs fixed


@ app.route('/delete_comment/<subject_id>')
def delete_comment(subject_id):
    mongo.db.blog.update({'_id': ObjectId(subject_id)},
                         {'$pull': {'comments': request.form.get('comments')}
                          })
    return redirect(url_for('get_blog'))


#####################Submission############################
@ app.route('/get_submission')
def get_submission():
    return render_template('submission.html',
                           categories=mongo.db.categories.find(),
                           work_categories=mongo.db.work_categories.find())


#####################Edit books and people############################
@ app.route('/edit_submission/<book_title_id>')
def edit_submission(book_title_id):
    the_book = mongo.db.book_title.find_one({"_id": ObjectId(book_title_id)})
    all_categories = mongo.db.book_title.find()
    all_cat = mongo.db.work_categories.find()
    return render_template('book_profile.html', book=the_book,
                           categories=all_categories, category=all_cat)


@ app.route('/update_submission/<book_title_id>', methods=["POST"])
def update_submission(book_title_id):
    book = mongo.db.book_title
    book.update({'_id': ObjectId(book_title_id)},
                {
        'book_title': request.form.get('book_title'),
        'author': request.form.get('author'),
        'book_cover': request.form.get('book_cover'),
        'book_link': request.form.get('book_link'),
        'category': request.form.get('category'),
        'synopsis': request.form.get('synopsis'),
        'inspire_person': request.form.get('inspire_person'),
        'work_cat': request.form.get('work_cat'),
        'img': request.form.get('img'),
        'born': request.form.get('born')
    })
    return redirect(url_for('get_books'))

#####################Delete books and people############################


@ app.route('/delete_submission/<book_title_id>')
def delete_submission(book_title_id):
    mongo.db.book_title.remove({'_id': ObjectId(book_title_id)})
    return redirect(url_for('get_books'))


@ app.route('/insert_submission', methods=['POST'])
def insert_submission():
    submission = mongo.db.book_title
    submission.insert_one(request.form.to_dict())
    return redirect(url_for('get_books'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
