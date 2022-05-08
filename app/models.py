from . import db

class User(db.model):
    __table__  = 'users'
    id = db.Column(db.Integer, primary_Key = True)
    username = db.Column(db.String(255))
    
    def __repr__(self):
        return f'User {self.username}'