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
                            inspire_person=mongo.db.inspire_person.find().limit(6))

@app.route('/get_books')
def get_books():
    return render_template("books.html",
                            books=mongo.db.book_title.find(),
                            categories=mongo.db.categories.find(),
                            books_limit=mongo.db.book_title.find().limit(6))

@app.route('/get_people')
def get_people():
    return render_template('people.html',
                            books=mongo.db.book_title.find(),
                            work_categories=mongo.db.work_categories.find(),
                            books_limit=mongo.db.book_title.find().limit(6))

@app.route('/get_search')
def get_search():
    return render_template('search.html')

@app.route('/get_blog')
def get_blog():
    return render_template('blog.html')


@app.route('/get_submission')
def get_submission():
    return render_template('submission.html',
    categories=mongo.db.categories.find(),
    work_categories=mongo.db.work_categories.find())

@app.route('/insert_submission', methods=['POST'])
def insert_submission():
        submission = mongo.db.book_title
        submission.insert_one(request.form.to_dict())
        return redirect(url_for('get_books'))
        
        submission1 = mongo.db.categories
        submission1.insert_one(request.form.to_dict())
        return redirect(url_for('get_books'))

        submission2 = mongo.db.inspire_person
        submission2.insert_one(request.form.to_dict())
        return redirect(url_for('get_people'))

        submission3 = mongo.db.work_categories
        submission3.insert_one(request.form.to_dict())
        return redirect(url_for('get_people'))

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
