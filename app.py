from flask import Flask
from database import init_db
from routes import register_routes

app = Flask(__name__)

# Initialize the database
init_db(app)

# Register the API routes
register_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
