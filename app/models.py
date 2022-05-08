from . import db

class User(db.Model):
    __tablename__  = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    
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
    