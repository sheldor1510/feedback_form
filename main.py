from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, url_for, flash, redirect, request, abort
from forms import PostForm
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = '8c95ca907af41d125536253accdf36b4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///file.db'
db = SQLAlchemy(app)




class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    rate = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    comments = db.Column(db.Text, nullable=False)


db.create_all()
db.session.commit()

@app.route("/", methods=['GET','POST'])
@app.route("/home", methods=['GET','POST'])
def home():
    form = PostForm()
    if form.validate_on_submit():
        info = Post(name=form.name.data,email=form.email.data,rate=form.rate.data, comments=form.comments.data)
        db.session.add(info)
        db.session.commit()
        flash('Thank You for your Feedback!', 'success')
        return render_template('finale.html')
    return render_template('layout.html', form=form)
    


@app.route("/about")
def about():
    return render_template('about.html')




if __name__ == '__main__':
    app.run(debug=True)