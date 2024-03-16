import pickle
import tensorflow as tf
import numpy as np
from datetime import datetime


def get_day_of_week_numeric(date_str):
    # Convert the string to a datetime object
    date_object = datetime.strptime(date_str, '%d/%m/%Y')
    # Get the day of the week (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
    day_of_week_numeric = date_object.weekday()
    return day_of_week_numeric

def one_hot_encode(day_of_week_numeric):
    # Define the number of classes (days of the week)
    num_classes = 6
    # Create one-hot encoding
    one_hot = tf.one_hot(day_of_week_numeric, num_classes)
    return one_hot

def get_conference_room_number(conference_room):
    if conference_room == "Quick 8":
        return 0
    if conference_room == "Pit-Lane":
        return 1
    if conference_room == "Dry-Lane":
        return 2
    if conference_room == "Joker Lap":
        return 3
    if conference_room == "Pole Position":
        return 4
    if conference_room == "Cockpit":
        return 5


class ai_controller:
    def __init__(self):
        self.desks_morning = pickle.load(open("ai_component/models/desks-morning.pickle", "rb"))
        self.desks_evening = pickle.load(open("ai_component/models/desks-evening.pickle", "rb"))
        self.meeting_rooms_9_11 = tf.keras.models.load_model('ai_component/models/meeting-rooms-9-11-0.57.keras')
        self.meeting_rooms_11_13 = tf.keras.models.load_model('ai_component/models/meeting-rooms-11-13-0.57.keras')
        self.meeting_rooms_13_15 = tf.keras.models.load_model('ai_component/models/meeting-rooms-13-15-0.62.keras')
        self.meeting_rooms_15_17 = tf.keras.models.load_model('ai_component/models/meeting-rooms-15-17-0.56.keras')

    def get_desk_prediction_morning(self, desk, day):
        deskname = desk + " " + str(get_day_of_week_numeric(day))
        if self.desks_morning[deskname]/13 < 0.5:
            return 0
        else:
            return 1

    def get_desk_prediction_evening(self, desk, day):
        deskname = desk + " " + str(get_day_of_week_numeric(day))
        if self.desks_evening[deskname]/13 < 0.5:
            return 0
        else:
            return 1

    def get_conference_prediction_9_11(self, room, day):
        encoded_room = one_hot_encode(get_conference_room_number(room))
        encoded_day = one_hot_encode(get_day_of_week_numeric(day))
        array = np.array([[encoded_room, encoded_day]])
        array = np.array([data_entry.flatten() for data_entry in array])
        prediction = self.meeting_rooms_9_11.predict(array)
        if prediction[0] < 0.5:
            return 0
        else:
            return 1

    def get_conference_prediction_11_13(self, room, day):
        encoded_room = one_hot_encode(get_conference_room_number(room))
        encoded_day = one_hot_encode(get_day_of_week_numeric(day))
        array = np.array([[encoded_room, encoded_day]])
        array = np.array([data_entry.flatten() for data_entry in array])
        prediction = self.meeting_rooms_11_13.predict(array)
        if prediction[0] < 0.5:
            return 0
        else:
            return 1

    def get_conference_prediction_13_15(self, room, day):
        encoded_room = one_hot_encode(get_conference_room_number(room))
        encoded_day = one_hot_encode(get_day_of_week_numeric(day))
        array = np.array([[encoded_room, encoded_day]])
        array = np.array([data_entry.flatten() for data_entry in array])
        prediction = self.meeting_rooms_13_15.predict(array)
        if prediction[0] < 0.5:
            return 0
        else:
            return 1

    def get_conference_prediction_15_17(self, room, day):
        encoded_room = one_hot_encode(get_conference_room_number(room))
        encoded_day = one_hot_encode(get_day_of_week_numeric(day))
        array = np.array([[encoded_room, encoded_day]])
        array = np.array([data_entry.flatten() for data_entry in array])
        prediction = self.meeting_rooms_15_17.predict(array)
        if prediction[0] < 0.5:
            return 0
        else:
            return 1