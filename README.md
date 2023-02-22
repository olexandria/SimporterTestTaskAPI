Flask Event Timeline API
This is a Flask API project that provides information about events and their timelines. The events data is stored in a SQLite database, and the API exposes two endpoints:

/api/info: returns information about the available filters and their values.
/api/timeline: returns a timeline of events within a specified date range and grouping.
Installation
Clone the repository: git clone https://github.com/your_username/flask-event-timeline-api.git.
Create a virtual environment: python -m venv env.
Activate the virtual environment: source env/bin/activate (Linux/Mac) or env\Scripts\activate (Windows).
Install the dependencies: pip install -r requirements.txt.
Initialize the database: python database.py.
Run the application: python app.py.
