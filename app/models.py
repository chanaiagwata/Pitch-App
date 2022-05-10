from . import db
from werkzeug.security import generate_password_hash,check_password_hash  #provides generating and check password functionality
from datetime import datetime


#users
class User(db.Model):
    __tablename__  = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True, index =True)
    password_secure = db.Column(db.String(255))
    pitches = db.relationship("Pitch", backref ="user", lazy = "dynamic")
    vote = db.relationship("Votes", backref="user", lazy = "dynamic")
    comment =db.relationship("Comments", backref = "user", lazy = "dynamic")
    
     #securing our passwords
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    @password.setter
    def password(self,password):
        self.password_secure = generate_password_hash(password)
        
    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)
    
    
    def __repr__(self):
        return f'User {self.username}'
    
   

#Categories
class Category(db.Model):
    __tablename__  = 'categories'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
   
    #method that saves instance of Category model through adding and committing to database
    def save_category(self):
        db.session.add(self)
        db.session.commit()
    #class method that retrieves a particular category of pitches from the Category model 
    @classmethod
    def get_categories(cls):
        categories = Category.query.all()
        return categories


#Pitches
class Pitch(db.Model):
    __tablename__ = 'pitches'
    
    id = db.Column(db.Integer,primary_key = True)
    gist = db.Column(db.String)
    categories_id = db.Column(db.Integer, db.ForeignKey('categories.id')) #references primary key in categories table
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))  #references primary key in user table
    vote = db.relationship("Votes", backref = "pitches", lazy = "dynamic")
    comment = db.relationship("Comments", backref = "pitches", lazy = "dynamic")

#Votes
class Votes(db.Model):
    __tablename__ = 'votes'
    
    id = db.Column(db.Integer, primary_key = True)
    vote = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    pitches_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))


#Comments
class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key = True)
    remark = db.Column(db.String(255))
    time_stamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    pitches_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))