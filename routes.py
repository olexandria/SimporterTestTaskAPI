from flask import request, jsonify
from sqlalchemy import func, Integer

from models.models import db, Event

from models.schemas import validate_timeline_request


def get_filters(request_params):
    filters = {}
    for arg_key, arg_value in request_params.dict(exclude_none=True).items():
        if arg_key not in ['startDate', 'endDate', 'grouping', 'timelineType']:
            filters[arg_key] = arg_value
    return filters


def get_timeline_data(start_date, end_date, grouping, timeline_type, filters):
    query = db.session.query(Event).filter(Event.timestamp >= start_date, Event.timestamp < end_date)

    if filters is not None:
        for attr, val in filters.items():
            query = query.filter(getattr(Event, attr) == val)

    # Add the grouping and timeline type to the query
    if grouping == 'weekly':
        query = query.group_by(func.strftime('%m-%W', Event.timestamp))
        print(query)
    elif grouping == 'bi-weekly':
        query = query.group_by(func.cast(func.strftime('%W', Event.timestamp), Integer) / 2)
    elif grouping == 'monthly':
        query = query.group_by(func.strftime('%Y-%m', Event.timestamp))
    else:
        return {'error': 'Invalid grouping type'}

    # Apply the timeline type to the query
    if timeline_type == 'cumulative':
        timeline = query.with_entities(
            func.strftime('%Y-%m-%d', Event.timestamp).label('date'),
            func.sum(func.count(Event.id)).over(order_by=Event.timestamp.asc()).label('count')
        ).all()
        print(timeline)
    elif timeline_type == 'usual':
        query = query.order_by(Event.timestamp.asc())
        timeline = query.with_entities(
            func.strftime('%Y-%m-%d', Event.timestamp).label('date'),
            func.count(Event.id).label('count')
        ).all()
        print(timeline)
    else:
        return {'error': 'Invalid timeline type'}

    # Format the timeline data into a list of dictionaries
    timeline_data = []
    for point in timeline:
        date = point.date
        count = point.count
        timeline_data.append({'date': date, 'value': count})

    return {'timeline': timeline_data}


def register_routes(app):
    @app.route('/api/info')
    def info():
        # Get the list of available filters and their values from the database
        filters = ['asin', 'brand', 'source', 'stars']
        filter_values = {}

        for f in filters:
            values = Event.query.with_entities(getattr(Event, f)).distinct().all()
            filter_values[f] = [v[0] for v in values]
        return jsonify(filter_values)

    @app.route('/api/timeline')
    def timeline():
        # Extract and validate the request parameters
        request_params = validate_timeline_request(request)

        # Extract the validated parameters from the request_params object
        start_date = request_params.startDate
        end_date = request_params.endDate
        grouping = request_params.grouping
        timeline_type = request_params.timelineType
        filters = get_filters(request_params)

        # Get the timeline data from the database
        data = get_timeline_data(start_date, end_date, grouping, timeline_type, filters)
        return jsonify(data)
