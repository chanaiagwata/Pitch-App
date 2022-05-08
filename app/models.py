from . import db

class User(db.model):
    __tablename__  = 'users'
    id = db.Column(db.Integer, primary_Key = True)
    username = db.Column(db.String(255))
    
    def __repr__(self):
        return f'User {self.username}'
    
class Category(db.model):
    __tablename__  ='categories'
    id = db.Column(db.Integer, primary_Key = True)
    