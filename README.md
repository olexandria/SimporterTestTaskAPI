# Flask Event Timeline API

This is a Flask API project that provides information about events and their timelines. The events data is stored in a SQLite database, and the API exposes two endpoints:

- /api/info: returns information about the available filters and their values.
- /api/timeline: returns a timeline of events within a specified date range and grouping.

## Installation
- Clone the repository: git clone https://github.com/your_username/SimporterTestTaskAPI.git
- Create a virtual environment: python -m venv env.
- Activate the virtual environment: source env/bin/activate (Linux/Mac) or env\Scripts\activate (Windows).
- Install the dependencies: pip install -r requirements.txt.
- Run the application: flask run

GET /api/info
Example:
http://127.0.0.1:5000/api/info

Returns: Information about possible filtering (list of attributes and list of values for each attribute)

GET /api/timeline
Example:
http://127.0.0.1:5000/api/timeline?startDate=2019-01-01&endDate=2020-01-01&Type=cumulative&Grouping=monthly&brand=Downy

Parameters:
- startDate
- endDate
- Type (cumulative or usual)
- Grouping (weekly, bi-weekly or monthly)
- Filters (attributes and values)

Grouping types: Aggregate data during the period (from startDate to endDate):
- weekly (data for each week)
- bi - weekly (data for each 2 weeks)
- monthly (data for each month)
Returns: JSON with timeline information according to input parameters:

Each point on the graph is in a format:
- data type - dict:
- - keys data type - str
- - values data type - int (number of events during this period)

The response has “timeline”(str) as a key, value - list of dicts with timeline data.
