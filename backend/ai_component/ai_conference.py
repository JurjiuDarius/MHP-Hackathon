from datetime import datetime

from numpy import loadtxt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf
import numpy as np

def convert_to_int(value):
    return 0

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
    return 6
def one_hot_encode_conference(conference_room_number):
    # Define the number of classes (days of the week)
    num_classes = 6
    # Create one-hot encoding
    one_hot = tf.one_hot(conference_room_number, num_classes)
    return one_hot

workspace_data = loadtxt('meeting-rooms.csv', delimiter=",", skiprows=1, dtype=str)
label_encoder = LabelEncoder()

conference_data = np.array([[one_hot_encode_conference(get_conference_room_number(workspace_data[i,1])), one_hot_encode(get_day_of_week_numeric(workspace_data[i, 3]))] for i in range(workspace_data.shape[0])])
conference_nineToEleven = label_encoder.fit_transform(workspace_data[:, 4])
conference_elevenToOne = label_encoder.fit_transform(workspace_data[:, 6])
conference_oneToThree = label_encoder.fit_transform(workspace_data[:, 8])
conference_threeToFive = label_encoder.fit_transform(workspace_data[:, 10])

X = np.array([data_entry.flatten() for data_entry in conference_data])
y = conference_nineToEleven
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

print("Conference data shape:", np.array(X_train).shape)

val = tf.keras.Input(shape=(12,))
model = tf.keras.Sequential([
    tf.keras.layers.Dense(24 , activation='linear'),
    tf.keras.layers.Dense(44 , activation='gelu'),
    tf.keras.layers.Dense(32 , activation='relu'),
    tf.keras.layers.Dense(32 , activation='relu'),
    tf.keras.layers.Dense(16 , activation='relu'),
    tf.keras.layers.Dense(13 , activation='relu'),
    tf.keras.layers.Dense(8 , activation='gelu'),
    tf.keras.layers.Dense(1 , activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(X_train, y_train, epochs=500, batch_size=1)

loss, accuracy = model.evaluate(X_test, y_test)
print("Test Accuracy:", accuracy)

predictions = model.predict(X_test)
# print("Predictions:", predictions)

formatted_accuracy="{:.2f}".format(accuracy)

model.save(f"C:/Users/Mihai/PycharmProjects/ai/mhp hackathon/backend/ai_component/meeting-rooms-9-11-{formatted_accuracy}.keras")

y = conference_elevenToOne
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

model.fit(X_train, y_train, epochs=50, batch_size=2)

loss, accuracy = model.evaluate(X_test, y_test)
print("Test Accuracy:", accuracy)

predictions = model.predict(X_test)
# print("Predictions:", predictions)

formatted_accuracy="{:.2f}".format(accuracy)

model.save(f"C:/Users/Mihai/PycharmProjects/ai/mhp hackathon/backend/ai_component/meeting-rooms-11-13-{formatted_accuracy}.keras")

y = conference_oneToThree
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

model.fit(X_train, y_train, epochs=50, batch_size=2)

loss, accuracy = model.evaluate(X_test, y_test)
print("Test Accuracy:", accuracy)

predictions = model.predict(X_test)
# print("Predictions:", predictions)

formatted_accuracy="{:.2f}".format(accuracy)

model.save(f"C:/Users/Mihai/PycharmProjects/ai/mhp hackathon/backend/ai_component/meeting-rooms-13-15-{formatted_accuracy}.keras")

y = conference_threeToFive
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33)

model.fit(X_train, y_train, epochs=50, batch_size=2)

loss, accuracy = model.evaluate(X_test, y_test)
print("Test Accuracy:", accuracy)

predictions = model.predict(X_test)
# print("Predictions:", predictions)

formatted_accuracy="{:.2f}".format(accuracy)

model.save(f"C:/Users/Mihai/PycharmProjects/ai/mhp hackathon/backend/ai_component/meeting-rooms-15-17-{formatted_accuracy}.keras")

