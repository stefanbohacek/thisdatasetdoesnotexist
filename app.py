# Import dependencies

from flask import Flask

# Set up main app

app = Flask(__name__)

# Import blueprints

from blueprints.generate import generate_blueprint
from blueprints.favicon import favicon_blueprint
from blueprints.index import index_blueprint
from blueprints.humans import humans_blueprint

app.register_blueprint(index_blueprint)
app.register_blueprint(generate_blueprint)
app.register_blueprint(favicon_blueprint)
app.register_blueprint(humans_blueprint)

if __name__ == '__main__':
    app.run()
