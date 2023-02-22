from models.models import db, Event
import pandas as pd
import datetime


def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///events.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()
        # Check if there are any rows in the Event table
        if db.session.query(Event).count() == 0:
            # If the table is empty, populate it with data from the CSV file
            # Read the CSV file into a pandas DataFrame
            df = pd.read_csv('data.csv', delimiter=';')

            # Convert the 'timestamp' column from Unix timestamps to datetime objects
            df['timestamp'] = df['timestamp'].apply(
                lambda x: datetime.datetime.fromtimestamp(int(x)).strftime('%Y-%m-%d'))

            # Populate the database with the events data
            for index, row in df.iterrows():
                event = Event(timestamp=row['timestamp'], asin=row['asin'], brand=row['brand'], source=row['source'],
                              stars=row['stars'])
                db.session.add(event)
            db.session.commit()
