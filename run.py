from restaurant.routes import app,db
from restaurant.models import User

#checks if main.py has executed directly and not imported
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug = True)



