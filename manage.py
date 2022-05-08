from app import create_app,db
from flask_script import Manager,Server
from app.models import User #importing User class from models.py

#creating app instance

app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)

#use shell decorator to create shell context and function for passing properties into shell

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User)
    pass

if __name__ == '__main__':
    manager.run()


