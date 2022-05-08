from . import db

class User(db.Model):
    __tablename__  = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True, index =True)
    password_hash=db.Column(db.String(255))
    
    def __repr__(self):
        return f'User {self.username}'
    
class Category(db.Model):
    __tablename__  ='categories'
    id = db.Column(db.Integer, primary_Key = True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
   
    #method that saves instance of Category model through adding and committing to database
    def save_category(self):
        db.session.add(self)
        db.session.commit()
    #class method that retrieves a particular category of pitches from the Category model 
    @classmethod
    def get_categories(cls,id):
        categories = Category.query.all()
        return categories

class Pitch(db.Model):
    __tablename__ = 'pitches'
    
    id = db.Column(db.Integer,primary_key = True)
    gist = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  #references primary key in user table
    categories_id = db.Column(db.Integer, db.ForeignKey('categories.id')) #references primary key in categories table
    vote = db.relationship("Votes", backref = "pitches", lazy = "dynamic")
    comment = db.relationship("Comments", backref = "pitches", lazy = "dynamic")
    
class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key = True)