from flask import Flask
from controller.home import home_controller
from controller.index import index_controller

app = Flask(__name__)

# Register controllers
app.register_blueprint(home_controller)
app.register_blueprint(index_controller)

if __name__ == '__main__':
    app.run(debug=True)
