from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db

# Initialize the migrate and manager objects
migrate = Migrate(app, db)
manager = Manager(app)

# Add the 'db' command to the manager
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()