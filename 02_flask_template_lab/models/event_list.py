from models.event import Event

event1 = Event("01.06.2021", "Joseph's Stag Do", 10, "Conference Room", "It's a fun stag do.")
event2 = Event("01.07.2021", "Green Festival", 2, "MotherEarth Room", "GreenPeace conference.")
event3 = Event("01.06.2021", "Bob's & Brunhild's Wedding", 35, "Basement", "Begening of a beautiful journey. Also, everyone is getting wasted...")

events = [event1, event2, event3]

def add_new_event(event):
    events.append(event)