from flask import render_template, Blueprint
from models.event_list import events
from models.event import Event

events_blueprint = Blueprint("events", __name__)

@events_blueprint.route('/events')
def index():
    return render_template('index.jinja', title='The Event list', events=events)