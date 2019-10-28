#............IMPORTANT..........#

# 1. Create project from PyCharm as a Flask project directly (automatically handle dependency)
# 2. Go to Project 'Settings' set Python interpreter as 3.7.x
# 3. Install SQLAlchemy from the project dependency in PyCharm
# 4. Instal Flask-sqlalchemy from the project dependency in PyCharm
# 5. Run this following two lines in the python console to create the database
#   >>> from app import db
#   >>> db.create_all()

#......................................#




import os
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

from flask_sqlalchemy import SQLAlchemy


# ============ This is for Database Confiiguration ============= #
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

# ============ This is for Database Table ============= #

class Book(db.Model):

    # --------- Add as many column as you want --------- #
    title = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return "<Title: {}>".format(self.title)

# ======= This is test of application at localhost:5000/ ======== #
@app.route('/')
def hello_world():
    return 'Hello World!'


# ======== This is the main Flask controller as http methods ========= #
@app.route('/welcome', methods=["GET", "POST"])
def welcome():
    books = Book.query.all()
    return render_template("welcome.html", books=books)


@app.route('/add', methods=["GET", "POST"])
def add():

    # ---- To Add entry to the 'Book' table from html form ------- #
    if request.form:
        try:
            book = Book(title=request.form.get("title"))
            db.session.add(book)
            db.session.commit()
        except Exception as e:
            print("Failed to add book")
            print(e)
    # books = Book.query.all()
    # return render_template("welcome.html", books=books)

    return redirect("/welcome")
    #return render_template("welcome.html")


@app.route("/update", methods=["POST"])
def update():
    # ---- To Update entry of 'Book' table column from html form ------- #
    try:
        newtitle = request.form.get("newtitle")
        oldtitle = request.form.get("oldtitle")
        book = Book.query.filter_by(title=oldtitle).first()
        book.title = newtitle
        db.session.commit()
    except Exception as e:
        print("Couldn't update book title")
        print(e)
    return redirect("/welcome")


@app.route("/delete", methods=["POST"])
def delete():
    # ---- To Delete entry from 'Book' table ------- #
    try:
        title = request.form.get("title")
        book = Book.query.filter_by(title=title).first()
        db.session.delete(book)
        db.session.commit()
    except Exception as e:
        print("Couldn't delete book")
        print(e)
    return redirect("/welcome")

if __name__ == '__main__':
    app.run(debug=True)
