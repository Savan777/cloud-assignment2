# This script is used to run commands and start the development server when in debug or development mode. For production using Gunicorn app:app
# This flask script also provides addtional functionality such as migrating and updating and other database realted commands.
import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app, db
from models import Music
from models import LikedSongs

app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()
