from flask import render_template, request, Blueprint
from models.event_list import events, add_new_event
from models.event import Event

events_blueprint = Blueprint("events", __name__)

@events_blueprint.route('/events')
def index():
    return render_template('index.jinja', title='The Event List', events=events)

@events_blueprint.route('/events', methods=['POST'])
def add_event():
    date = request.form['date']
    name_of_event = request.form['name_of_event']
    number_of_guests = request.form['number_of_guests']
    room_location = request.form['room_location']
    description = request.form['description']
    new_event = Event(date, name_of_event, number_of_guests, room_location, description)
    add_new_event(new_event)

    return render_template('index.jinja', title='The Event List', events=events)