import os

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask_sqlalchemy import SQLAlchemy
#import flask_whooshalchemy as wa

# ============ This is for Database Confiiguration ============= #
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "employeedatabase.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
#app.config["WHOOSH_BASE"] = "whoosh"

db = SQLAlchemy(app)

db.Model.metadata.reflect(db.engine)


class Employee(db.Model):

    #__searchable__ =['name']
    # --------- Add as many column as you want --------- #
    __tablename__ = 'employee'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False, primary_key=False)

    def __repr__(self):
        return "<Id: {}>".format(self.id), "<Name: {}>".format(self.name)

#wa.whoosh_index(app, Employee)


class Book_List(db.Model):

    # ----- this maps already created database table to read/SELECT ----- #
    __tablename__ = 'book'
    __table_args__ = {'extend_existing': True}
    # id = db.Column(db.Integer, unique=True, nullable=False, primary_key=True)
    # title = db.Column(db.String(80), unique=False, nullable=False, primary_key=False)

    def __repr__(self):
        return "<Id: {}>".format(self.id), "<Title: {}>".format(self.title)


@app.route('/search', methods=["GET", "POST"])
def search_info():

    # print("Total Employee: ", Employee.query.count())

    # ------- This Shows all the record from the Table Creating FROM flask------ #
    people = Employee.query.all()
    # ------- This Shows all the record from the Table WITHOUT creating from flask------ #
    books = Book_List.query.all()

    return render_template("search.html", people=people, books=books)
    #return 'Hello Search API'


@app.route('/result', methods=["GET", "POST"])
def result():

    if request.form:
        try:
            input_name = request.form.get("name")
            # print(input_name)
            # -------- This takes the search name from the Form ---- #
            person = Employee.query.filter_by(name=input_name).first()

            # print("search: ", person.name)
            db.session.commit()
        except Exception as e:
            print("Failed to find employee")
            print(e)

    #return redirect("/search")
    return render_template("result.html", result=person)
    #return 'Hello Search API'


if __name__ == '__main__':
    app.run(debug=True)

